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
    void ChangeValue();

private:
    Ui::MainWindow *ui;
    DownloadThread *thread;
    QProgressDialog *downloadDialog;
    QJsonArray name;
};

#endif // MAINWINDOW_H
