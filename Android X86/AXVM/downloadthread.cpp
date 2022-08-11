#define SETTINGSTEP 6
#include "downloadthread.h"
#include <QProgressDialog>
#include <QFile>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QEventLoop>
#include <QTimer>
#include <QNetworkReply>
#include <QMessageBox>
#include <QCoreApplication>
// 文件操作
#include <QDir>
// 命令执行
#include <QProcess>
// 获取内存总量
#if defined(Q_OS_LINUX) // 区分系统平台
#include "sys/statfs.h" // Linux 上
#else // Windows 上
#pragma comment(lib, "Kernel32.lib")
#pragma comment(lib, "Psapi.lib")
#include <windows.h>
#include <tlhelp32.h>
#endif

DownloadThread::DownloadThread(QProgressDialog *progressDialog, QString url, QString name, QString mouse, bool NotDownload){
    dialog = progressDialog;
    fileUrl = url;
    vmName = name;
    setMouse = mouse;
    notDownload = NotDownload;
}

// 文件下载
void DownloadThread::run(){
    // 创建文件夹
    QDir dir;
    QString configDir = QCoreApplication::applicationDirPath() + "/VM";
    if(!dir.exists(configDir)){
        // 文件不存在
        dir.mkpath(configDir);
    }
    configDir = QCoreApplication::applicationDirPath() + "/VM/" + vmName;
    if(!dir.exists(configDir)){
        // 文件不存在
        dir.mkpath(configDir);
    }
    QString savePath = configDir + "/vm.ova";
    // 文件下载
    int timeout = 0;
    QFile f(savePath);
    if(!f.open(QIODevice::WriteOnly)){
        emit MessageBoxError("文件无法写入");
        f.close();
        delete dialog;
        dialog->close();
        return;
    }
    if(notDownload){
        qDebug() << "b";
        SettingVirtualMachine(savePath);
        return;
    }
    QNetworkAccessManager m;
    QNetworkRequest req;
    // 响应 https（就是不行）
    QSslConfiguration conf = req.sslConfiguration();
    conf.setPeerVerifyMode(QSslSocket::VerifyNone);
    conf.setProtocol(QSsl::TlsV1_0);
    req.setSslConfiguration(conf);
    req.setUrl(QUrl(fileUrl));
    // 下载文件
    QNetworkReply *reply = m.get(req);
    QEventLoop loop;
    QTimer t;
    qDebug() << reply->rawHeader(QString("Content-Length").toUtf8());
    connect(reply, &QNetworkReply::finished, &loop, &QEventLoop::quit);
    connect(reply, &QNetworkReply::downloadProgress, [=, &f, &t](qint64 bytesRead, qint64 totalBytes){
        f.write(reply->readAll());
        dialog->setValue((float)bytesRead / totalBytes * 100);
        dialog->setLabelText(QString::number(bytesRead / 1024 / 1024) + "MB/" + QString::number(totalBytes / 1024 / 1024) + "MB");
        if(t.isActive()){
            t.start(timeout);
        }
    });
    if(timeout > 0){
        connect(&t, &QTimer::timeout, &loop, &QEventLoop::quit);
        t.start(timeout);
    }
    loop.exec();
    if(reply->error() != QNetworkReply::NoError){
        emit MessageBoxError("下载失败");
        f.close();
        delete reply;
        delete dialog;
        dialog->close();
        return;
    }
    f.close();
    delete reply;
    SettingVirtualMachine(savePath);
}

void DownloadThread::SettingVirtualMachine(QString savePath){
    // 设置虚拟机
    dialog->setLabelText("设置虚拟机");
    dialog->setWindowTitle("正在设置“" + vmName + "”");
    dialog->setValue(100 / SETTINGSTEP * 0);
    dialog->show();
    // 拷贝 OVA 文件
    if(notDownload){
        if(QFile::exists(savePath)){
            QFile::remove(savePath);
        }
        if(!QFile::copy(fileUrl, savePath)){
            emit MessageBoxError("文件复制错误，无法继续");
        }
    }
    // 导入 OVA 镜像
    QProcess progress;
    QStringList command;
    dialog->setValue(100 / SETTINGSTEP * 1);
    command << "import" << savePath;
    progress.start("VBoxManage", command);
    progress.waitForFinished();
    qDebug() << "正常信息：\n";
    qDebug() << progress.readAllStandardOutput();
    qDebug() << "错误信息：\n";
    qDebug() << progress.readAllStandardError();
    // 获取内存
    dialog->setValue(100 / SETTINGSTEP * 2);
    int memtotal = 0;
#if defined (Q_OS_LINUX)  // 在 Linux 下读取总内存
    progress.start("free -m");
    progress.waitForFinished();
    progress.readLine(); // 忽略第一行
    QString memoryInfo = progress.readLine();  // 只读取第 2 行
    qDebug() << memoryInfo;
    memoryInfo.replace("\n", ""); // 忽略换行符
    memoryInfo.replace(QRegExp("( ){1,}"), " ");  // 将连续的空格换为单个空格
    auto memoryList = memoryInfo.split(" ");  // 根据空格切割内容
    qDebug() << memoryList;
    if(memoryList.size() >= 2){  // 保证至少有两个
        // 理论上列表应该出现的是如下的内容
        // ["Mem:", "13998", "9622", "197", "803", "4179", "3331"]
        // 因此要读[1]
        memtotal = memoryList[1].toDouble();
    }
    else{
        emit MessageBoxError("内存读取错误，请自行打开 VirtualBox 设置内存");
        return;
    }
#endif
    // 设置内存
    // 示例命令：VBoxManage modifyvm [name] --memory 4096
    command.clear();  // 清空参数列表
    command << "modifyvm" << vmName << "--memory" << QString::number(memtotal / 2);
    progress.start("VBoxManage", command);
    progress.waitForFinished();
    // 设置显卡，默认的 VMSVGA 在 Android X86 上运行有很多问题，应设为 VBoxVGA
    // 示例命令：VBoxManage modifyvm [name] --graphicscontroller vboxvga
    dialog->setValue(100 / SETTINGSTEP * 3);
    command.clear();  // 清空参数列表
    command << "modifyvm" << vmName << "--graphicscontroller" << "vboxvga";
    qDebug() << command;
    progress.start("VBoxManage", command);
    progress.waitForFinished();
    // 设置声卡
    // VBoxManage modifyvm [name] --audio pulse --audiocontroller hda --audioin on --audioout on
    dialog->setValue(100 / SETTINGSTEP * 4);
    command.clear();  // 清空参数列表
    command << "modifyvm" << vmName << "--audio" << "pulse" << "--audiocontroller" << "hda" << "--audioin" << "on" << "--audioout" << "on";
    progress.start("VBoxManage", command);
    progress.waitForFinished();
    // 设置显存
    // VBoxManage modifyvm [name] --vram 128
    dialog->setValue(100 / SETTINGSTEP * 5);
    command.clear();  // 清空参数列表
    command << "modifyvm" << vmName << "--vram" << "128";
    progress.start("VBoxManage", command);
    progress.waitForFinished();
    // 设置鼠标
    // VBoxManage modifyvm [name] --mouse ps2
    dialog->setValue(100 / SETTINGSTEP * 6);
    if(setMouse == "ps2"){
        command.clear();  // 清空参数列表
        command << "modifyvm" << vmName << "--mouse" << "ps2";
        progress.start("VBoxManage", command);
        progress.waitForFinished();
    }
    // 结束
    dialog->setValue(100);
    emit MessageBoxOpenVM(vmName);
    dialog->close();
    delete dialog;
}
