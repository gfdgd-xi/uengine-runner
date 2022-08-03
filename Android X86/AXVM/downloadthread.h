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
    DownloadThread(QProgressDialog *dialog, QString url, QString save);
    QProgressDialog *dialog;
    QString fileUrl;
    QString savePath;

protected:
    void run(); // 核心

signals:
    void ChangeValue();
};

#endif // DOWNLOADTHREAD_H
