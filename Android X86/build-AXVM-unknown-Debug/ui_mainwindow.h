/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout_2;
    QTabWidget *tabWidget;
    QWidget *tab;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_3;
    QComboBox *comboBox;
    QPushButton *pushButton_7;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label;
    QLineEdit *lineEdit;
    QPushButton *pushButton_3;
    QGridLayout *gridLayout_2;
    QPushButton *pushButton_11;
    QPushButton *pushButton_8;
    QPushButton *pushButton_10;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton_9;
    QPushButton *pushButton_12;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_6;
    QPushButton *pushButton_5;
    QPushButton *pushButton_4;
    QHBoxLayout *horizontalLayout_2;
    QLabel *localIP;
    QSpacerItem *verticalSpacer;
    QWidget *tab_2;
    QHBoxLayout *horizontalLayout;
    QListView *listView;
    QVBoxLayout *verticalLayout;
    QSpacerItem *verticalSpacer_3;
    QPushButton *pushButton_2;
    QPushButton *pushButton;
    QSpacerItem *verticalSpacer_2;
    QListView *urlImageList;
    QWidget *tab_3;
    QLabel *label_4;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(683, 416);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        verticalLayout_2 = new QVBoxLayout(centralWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setTabPosition(QTabWidget::West);
        tabWidget->setElideMode(Qt::ElideNone);
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        gridLayout = new QGridLayout(tab);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        label_3 = new QLabel(tab);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(label_3->sizePolicy().hasHeightForWidth());
        label_3->setSizePolicy(sizePolicy);

        horizontalLayout_5->addWidget(label_3);

        comboBox = new QComboBox(tab);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        horizontalLayout_5->addWidget(comboBox);

        pushButton_7 = new QPushButton(tab);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));
        sizePolicy.setHeightForWidth(pushButton_7->sizePolicy().hasHeightForWidth());
        pushButton_7->setSizePolicy(sizePolicy);

        horizontalLayout_5->addWidget(pushButton_7);


        gridLayout->addLayout(horizontalLayout_5, 3, 0, 1, 1);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        label = new QLabel(tab);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_3->addWidget(label);

        lineEdit = new QLineEdit(tab);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        horizontalLayout_3->addWidget(lineEdit);

        pushButton_3 = new QPushButton(tab);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        horizontalLayout_3->addWidget(pushButton_3);


        gridLayout->addLayout(horizontalLayout_3, 0, 0, 1, 1);

        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        pushButton_11 = new QPushButton(tab);
        pushButton_11->setObjectName(QString::fromUtf8("pushButton_11"));

        gridLayout_2->addWidget(pushButton_11, 0, 4, 1, 1);

        pushButton_8 = new QPushButton(tab);
        pushButton_8->setObjectName(QString::fromUtf8("pushButton_8"));

        gridLayout_2->addWidget(pushButton_8, 0, 0, 1, 1);

        pushButton_10 = new QPushButton(tab);
        pushButton_10->setObjectName(QString::fromUtf8("pushButton_10"));

        gridLayout_2->addWidget(pushButton_10, 0, 2, 1, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 0, 5, 1, 1);

        pushButton_9 = new QPushButton(tab);
        pushButton_9->setObjectName(QString::fromUtf8("pushButton_9"));

        gridLayout_2->addWidget(pushButton_9, 0, 1, 1, 1);

        pushButton_12 = new QPushButton(tab);
        pushButton_12->setObjectName(QString::fromUtf8("pushButton_12"));

        gridLayout_2->addWidget(pushButton_12, 0, 3, 1, 1);


        gridLayout->addLayout(gridLayout_2, 4, 0, 1, 1);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        label_2 = new QLabel(tab);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_4->addWidget(label_2);

        lineEdit_2 = new QLineEdit(tab);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        horizontalLayout_4->addWidget(lineEdit_2);

        pushButton_6 = new QPushButton(tab);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));

        horizontalLayout_4->addWidget(pushButton_6);

        pushButton_5 = new QPushButton(tab);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));

        horizontalLayout_4->addWidget(pushButton_5);

        pushButton_4 = new QPushButton(tab);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        horizontalLayout_4->addWidget(pushButton_4);


        gridLayout->addLayout(horizontalLayout_4, 2, 0, 1, 1);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        localIP = new QLabel(tab);
        localIP->setObjectName(QString::fromUtf8("localIP"));

        horizontalLayout_2->addWidget(localIP);


        gridLayout->addLayout(horizontalLayout_2, 1, 0, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 5, 0, 1, 1);

        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        horizontalLayout = new QHBoxLayout(tab_2);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        listView = new QListView(tab_2);
        listView->setObjectName(QString::fromUtf8("listView"));

        horizontalLayout->addWidget(listView);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_3);

        pushButton_2 = new QPushButton(tab_2);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        verticalLayout->addWidget(pushButton_2);

        pushButton = new QPushButton(tab_2);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        verticalLayout->addWidget(pushButton);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer_2);


        horizontalLayout->addLayout(verticalLayout);

        urlImageList = new QListView(tab_2);
        urlImageList->setObjectName(QString::fromUtf8("urlImageList"));

        horizontalLayout->addWidget(urlImageList);

        tabWidget->addTab(tab_2, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QString::fromUtf8("tab_3"));
        tabWidget->addTab(tab_3, QString());

        verticalLayout_2->addWidget(tabWidget);

        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        verticalLayout_2->addWidget(label_4);

        MainWindow->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "\351\200\211\346\213\251\350\231\232\346\213\237\346\234\272\357\274\232", nullptr));
        pushButton_7->setText(QCoreApplication::translate("MainWindow", "PushButton", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "IP\345\234\260\345\235\200\357\274\232", nullptr));
        pushButton_3->setText(QCoreApplication::translate("MainWindow", "\350\277\236\346\216\245", nullptr));
        pushButton_11->setText(QCoreApplication::translate("MainWindow", "\351\207\215\347\275\256\350\231\232\346\213\237\346\234\272", nullptr));
        pushButton_8->setText(QCoreApplication::translate("MainWindow", "\345\274\200\345\220\257\350\231\232\346\213\237\346\234\272", nullptr));
        pushButton_10->setText(QCoreApplication::translate("MainWindow", "\350\256\276\347\275\256\350\231\232\346\213\237\346\234\272", nullptr));
        pushButton_9->setText(QCoreApplication::translate("MainWindow", "\345\205\263\351\227\255\350\231\232\346\213\237\346\234\272", nullptr));
        pushButton_12->setText(QCoreApplication::translate("MainWindow", "\351\207\215\347\275\256\350\231\232\346\213\237\346\234\272\351\205\215\347\275\256", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "\345\256\211\350\243\205/\345\215\270\350\275\275\345\272\224\347\224\250\357\274\232", nullptr));
        pushButton_6->setText(QCoreApplication::translate("MainWindow", "\345\256\211\350\243\205", nullptr));
        pushButton_5->setText(QCoreApplication::translate("MainWindow", "\346\265\217\350\247\210", nullptr));
        pushButton_4->setText(QCoreApplication::translate("MainWindow", "\345\215\270\350\275\275", nullptr));
        localIP->setText(QCoreApplication::translate("MainWindow", "\350\256\277\351\227\256\357\274\232http://127.0.0.1:30201 \350\277\236\346\216\245", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("MainWindow", "\346\223\215\344\275\234", nullptr));
        pushButton_2->setText(QCoreApplication::translate("MainWindow", "<<", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", ">>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QCoreApplication::translate("MainWindow", "\346\226\260\345\273\272\346\250\241\346\213\237\345\231\250", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QCoreApplication::translate("MainWindow", "\345\205\263\344\272\216", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "\302\2512022~Now\357\274\214gfdgd xi\343\200\201\344\270\272\344\273\200\344\271\210\346\202\250\344\270\215\345\226\234\346\254\242\347\206\212\345\207\272\346\262\241\345\222\214\351\230\277\345\270\203\345\221\242", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
