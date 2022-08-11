#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QStringListModel>
#include <QStandardItem>
#include <QThread>
#include <QInputDialog>
#include <QFileDialog>
// 用于镜像信息获取
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
// 用于解析 JSON 数据
#include <QJsonObject>
#include <QJsonDocument>
#include <QJsonArray>
// 用于下载文件
#include <QProgressDialog>
#include "downloadthread.h"
#include <QLoggingCategory>
// 用于执行命令
#include <QProcess>
// 用于 Mini HTTP 服务器搭建
#include <getipserver.h>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QLoggingCategory::defaultCategory()->setEnabled(QtDebugMsg, true);
    // 获取网络镜像列表
    QEventLoop loop;
    QNetworkAccessManager manager;
    QNetworkReply *reply = manager.get(QNetworkRequest(QUrl("http://120.25.153.144/AXVM/list.json")));
    connect(reply, SIGNAL(finished()), &loop, SLOT(quit()));
    loop.exec();
    // 解析获取数据并显示
    QString imageJsonList = reply->readAll();
    QJsonDocument imageList = QJsonDocument::fromJson(imageJsonList.toUtf8());
    name = imageList.array();
    QStringList nameList;
    QStandardItemModel *nameListModel = new QStandardItemModel(this);
    int size = name.size();
    qDebug() << size;
    for (int i = 0; i < size; ++i) {
        QJsonValue value = name.at(i);
        QJsonArray obj = value.toArray();
        QStandardItem *item = new QStandardItem(obj.at(0).toString());
        nameListModel->appendRow(item);
    }
    ui->urlImageList->setModel(nameListModel);
    // 允许 qDebug() 输出
    QLoggingCategory::defaultCategory()->setEnabled(QtDebugMsg, true);
    GetIPServer *ip = new GetIPServer(ui->localIP);
}

MainWindow::~MainWindow()
{
    delete ui;
}
// 安装事件
void MainWindow::on_pushButton_2_clicked()
{
    if(ui->urlImageList->selectionModel()->currentIndex().row() == -1){  // 未选择任何选项
        QMessageBox::information(this, "提示", "您未选择任何项");
        return;
    }
    downloadDialog = new QProgressDialog("", "无用的按钮", 0, 100, this);
    downloadDialog->setWindowTitle("正在下载“" + name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(0).toString() + "”");
    downloadDialog->show();
    if(name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(3).isArray()){
        if(QMessageBox::question(this, "提示", "推荐您手动下载格式包，是否手动获取链接并下载？") == QMessageBox::Yes){
            QJsonArray urlList = name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(3).toArray();
            QString urlThings = "";
            for(int i = 0; i < urlList.size(); i=i+2){
                urlThings += urlList.at(i).toString() + "：" + urlList.at(i + 1).toString();
            }

            QString choose = QInputDialog::getMultiLineText(this,
                                           "“" + name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(0).toString() + "”下载链接",
                                           "请在下面任选一个链接复制到浏览器地址栏进行下载，下载完成后按下“OK”按钮选择下载的 OVA 文件，如果想要取消操作请按“Cancal”",
                                           urlThings);
            if(choose == ""){  // 忽略取消
                downloadDialog->close();
                delete downloadDialog;
                return;
            }
            QString path = QFileDialog::getOpenFileName(this, "浏览 OVA 文件", "~", "OVA文件(*.ova);;全部文件(*.*)");
            if(path == ""){  // 忽略取消
                downloadDialog->close();
                delete downloadDialog;
                return;
            }
            thread = new DownloadThread(downloadDialog,
                                        path,
                                        name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(0).toString(),
                                        name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(2).toString(),
                                        true);
            //connect(thread, &DownloadThread::MessageBoxInfo, this, [this](QString info){QMessageBox::information(this, "提示", info);});
            //connect(thread, &DownloadThread::MessageBoxError, this, [this](QString info){QMessageBox::critical(this, "错误", info);});
            /*connect(thread, &DownloadThread::MessageBoxOpenVM, this, [this](QString vmName){
                if(QMessageBox::question(this, "提示", "安装成功！是否现在马上启动虚拟机？") == QMessageBox::Yes){
                    QProcess process;
                    QStringList command;
                    command << "startvm" << vmName;
                    process.start("VBoxManage", command);
                    process.waitForFinished();
                    qDebug() << process.readAllStandardError();
                    qDebug() << process.readAllStandardOutput();
                }});*/
            thread->start();
            return;
        }
    }
    thread = new DownloadThread(downloadDialog,
                                name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(1).toString(),
                                name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(0).toString(),
                                name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(2).toString(),
                                false);
    //connect(thread, &DownloadThread::MessageBoxInfo, this, &MainWindow::MessageBoxInfo);
    //connect(thread, &DownloadThread::MessageBoxError, this, &MainWindow::MessageBoxError);

    //connect(thread, &DownloadThread::MessageBoxOpenVM, this, &MainWindow::OpenVM);
    thread->start();
}
void DownloadThread::MessageBoxInfo(QString info){
    QMessageBox::information(NULL, "提示", info);
}
void DownloadThread::MessageBoxError(QString info){
    QMessageBox::critical(NULL, "错误", info);
}
void DownloadThread::MessageBoxOpenVM(QString vmName)
    {
            if(QMessageBox::question(NULL, "提示", "安装成功！是否现在马上启动虚拟机？") == QMessageBox::Yes){
                QProcess process;
                QStringList command;
                command << "startvm" << vmName;
                process.start("VBoxManage", command);
                process.waitForFinished();
                qDebug() << process.readAllStandardError();
                qDebug() << process.readAllStandardOutput();
            }
}

void MainWindow::on_centralWidget_destroyed()
{

}
