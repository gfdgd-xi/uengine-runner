#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QStringListModel>
#include <QStandardItem>
#include <QThread>
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

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    // 获取网络镜像列表
    QEventLoop loop;
    QNetworkAccessManager manager;
    QNetworkReply *reply = manager.get(QNetworkRequest(QUrl("http://127.0.0.1/list.json")));
    connect(reply, SIGNAL(finished()), &loop, SLOT(quit()));
    loop.exec();
    // 解析获取数据并显示
    QString imageJsonList = reply->readAll();
    QJsonDocument imageList = QJsonDocument::fromJson(imageJsonList.toUtf8());
    name = imageList.array();
    QStringList nameList;
    QStandardItemModel *nameListModel = new QStandardItemModel(this);
    int size = name.size();
    for (int i = 0; i < size; ++i) {
        QJsonValue value = name.at(i);
        QJsonArray obj = value.toArray();
        QStandardItem *item = new QStandardItem(obj.at(0).toString());
        nameListModel->appendRow(item);
    }
    ui->urlImageList->setModel(nameListModel);
    // 允许 qDebug() 输出
    QLoggingCategory::defaultCategory()->setEnabled(QtDebugMsg, true);
}

MainWindow::~MainWindow()
{
    delete ui;
}
// 安装事件
void MainWindow::on_pushButton_2_clicked()
{
    QNetworkAccessManager *manager = new QNetworkAccessManager(this);
    qDebug() << QSslSocket::supportsSsl();
    qDebug() << QSslSocket::sslLibraryBuildVersionString();
    qDebug() << QSslSocket::sslLibraryVersionString();
    qDebug() << manager->supportedSchemes();
    qDebug() << name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(1).toString();
    downloadDialog = new QProgressDialog("文件下载", "文件下载", 0, 100, this);
    downloadDialog->setWindowTitle("下载文件ing……");
    downloadDialog->show();
    thread = new DownloadThread(downloadDialog, name.at(ui->urlImageList->selectionModel()->currentIndex().row()).toArray().at(1).toString(), "/tmp/1.exe");
    thread->start();
}

void MainWindow::ChangeValue(){
    //downloadDialog->setValue(thread->value);
}
