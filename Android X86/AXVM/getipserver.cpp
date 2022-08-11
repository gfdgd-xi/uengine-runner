#include "getipserver.h"
#include <QTcpServer>
#include <mainwindow.h>
#include <QtNetwork>
#include <QHostAddress>
#include <QMessageBox>

GetIPServer::GetIPServer(QLabel *localIp)
{
    lock = false;
    tcp = new QTcpServer();
    QHostAddress ip("0.0.0.0");
    tcp->listen(QHostAddress::Any, 30201);
    // 获取 IP 地址
    QString IpAddress;
    foreach (QHostAddress address, QNetworkInterface::allAddresses())
    {
        if(address.protocol() == QAbstractSocket::IPv4Protocol && address.toString() != "127.0.0.1" && address.toString() != "192.168.250.1"){
            IpAddress = address.toString();
        }
    }
    qDebug() << "服务器IP：" << IpAddress;
    qDebug() << "服务器端口：" << tcp->serverPort();
    localIp->setText("访问：http://" + IpAddress + ":" + QString::number(tcp->serverPort()) + " 连接");
    connect(tcp, &QTcpServer::newConnection, this, [this](){

        tcpSocket = tcp->nextPendingConnection();
        QString ipAddress = QHostAddress(tcpSocket->peerAddress().toIPv4Address()).toString();
        qDebug() << ipAddress;
        qDebug() << tcpSocket->peerPort();
        tcpSocket->write("HTTP/1.1 200 OK"\
                         "Content-Type: text/html;charset=utf-8"\
                         "\n\n");
        tcpSocket->write(QString("<html><body><p>IP Address: " + ipAddress + "</p><p>Get Port: " + QString::number(tcpSocket->peerPort()) + "</p></body></html>").toLocal8Bit());
        tcpSocket->close();
        if(lock){
            return;
        }
        lock = true;
        QMessageBox::question(NULL, "提示", "IP地址为“" + ipAddress + "”想要连接，是否连接？");
        lock = false;
    });
    qDebug() << "a";
}
