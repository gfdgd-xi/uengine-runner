#ifndef GETIPSERVER_H
#define GETIPSERVER_H

#include <mainwindow.h>
#include <QTcpServer>
#include <QLabel>

class GetIPServer : public QMainWindow
{
public:
    GetIPServer(QLabel *localIp);
    void ConnectClient();

private:
    bool lock;
    QTcpServer *tcp;
    QTcpSocket *tcpSocket;
};

#endif // GETIPSERVER_H
