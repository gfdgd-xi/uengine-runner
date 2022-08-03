#include "downloadthread.h"
#include <QProgressDialog>
#include <QFile>
#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QEventLoop>
#include <QTimer>
#include <QNetworkReply>
#include <QMessageBox>


DownloadThread::DownloadThread(QProgressDialog *progressDialog, QString url, QString save){
    dialog = progressDialog;
    fileUrl = url;
    savePath = save;
}

// 文件下载
void DownloadThread::run(){
    int timeout = 0;
    QFile f(savePath);
    if(!f.open(QIODevice::WriteOnly)){

    }
    QNetworkAccessManager m;
    QNetworkRequest req;
    // 响应 https
    QSslConfiguration conf = req.sslConfiguration();
    /*conf.setPeerVerifyMode(QSslSocket::VerifyNone);
    conf.setProtocol(QSsl::TlsV1SslV3);
    req.setSslConfiguration(conf);
    req.setUrl(QUrl(fileUrl));*/
    conf.setPeerVerifyMode(QSslSocket::VerifyNone);
    conf.setProtocol(QSsl::TlsV1SslV3);
    req.setSslConfiguration(conf);
    req.setUrl(QUrl(fileUrl));
    //QNetworkRequest request ;

    //request.setAttribute(QNetworkRequest::HttpPipeliningAllowedAttribute, true);
    //QNetworkReply* reply = QNetworkAccessManager::createRequest(op, request, outgoingData);
    //QNetworkRequest request(req);
    QNetworkReply *reply = m.get(req);
    QEventLoop loop;
    QTimer t;
    //QMessageBox::information(this, "", QString::number(reply->rawHeader(QString("Content-Length").toUtf8())));
    qDebug() << reply->rawHeader(QString("Content-Length").toUtf8());
    connect(reply, &QNetworkReply::finished, &loop, &QEventLoop::quit);
    connect(reply, &QNetworkReply::downloadProgress, [=, &f, &t](qint64 bytesRead, qint64 totalBytes){
        f.write(reply->readAll());
        dialog->setValue(bytesRead / totalBytes * 100);
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

    }
    f.close();
    delete reply;
    dialog->close();
}
