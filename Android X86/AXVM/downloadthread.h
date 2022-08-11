/*
 * 重写 QThread 以实现多线程下载功能
 */
#ifndef DOWNLOADTHREAD_H
#define DOWNLOADTHREAD_H

#include <QObject>
#include <QThread>
#include <QProgressDialog>

class DownloadThread : public QThread  // 继承 QThread
{
public:
    DownloadThread(QProgressDialog *dialog, QString url, QString save, QString mouse, bool NotDownload);
    void SettingVirtualMachine(QString savePath);
    QProgressDialog *dialog;
    QString fileUrl;
    QString vmName;
    QString setMouse;
    bool notDownload;
    QString notDownloadPath;

protected:
    void run(); // 核心

signals:
    // 防止非主线程刷新控件导致程序退出
    void MessageBoxInfo(QString info);
    void MessageBoxError(QString info);
    void MessageBoxOpenVM(QString vmName);
};

#endif // DOWNLOADTHREAD_H
