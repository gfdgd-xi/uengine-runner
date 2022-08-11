#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "downloadthread.h"

#include <QMainWindow>
#include <QNetworkReply>
#include <QProgressDialog>
#include <QJsonArray>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_2_clicked();
    //void OpenVM(QString vmName);
    //void MessageBoxInfo(QString info);
    //void MessageBoxError(QString info);

    void on_centralWidget_destroyed();

private:
    Ui::MainWindow *ui;
    DownloadThread *thread;
    QProgressDialog *downloadDialog;
    QJsonArray name;
};

#endif // MAINWINDOW_H
