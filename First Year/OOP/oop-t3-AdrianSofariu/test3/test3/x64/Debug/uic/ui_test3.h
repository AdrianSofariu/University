/********************************************************************************
** Form generated from reading UI file 'test3.ui'
**
** Created by: Qt User Interface Compiler version 6.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_TEST3_H
#define UI_TEST3_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_test3Class
{
public:
    QWidget *centralWidget;
    QListView *medList;
    QLineEdit *searchBar;
    QListWidget *seList;
    QLineEdit *medEdit;
    QPushButton *seButton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *test3Class)
    {
        if (test3Class->objectName().isEmpty())
            test3Class->setObjectName("test3Class");
        test3Class->resize(600, 400);
        centralWidget = new QWidget(test3Class);
        centralWidget->setObjectName("centralWidget");
        medList = new QListView(centralWidget);
        medList->setObjectName("medList");
        medList->setGeometry(QRect(20, 10, 271, 331));
        searchBar = new QLineEdit(centralWidget);
        searchBar->setObjectName("searchBar");
        searchBar->setGeometry(QRect(320, 30, 221, 24));
        seList = new QListWidget(centralWidget);
        seList->setObjectName("seList");
        seList->setGeometry(QRect(330, 220, 231, 111));
        medEdit = new QLineEdit(centralWidget);
        medEdit->setObjectName("medEdit");
        medEdit->setGeometry(QRect(320, 180, 131, 24));
        seButton = new QPushButton(centralWidget);
        seButton->setObjectName("seButton");
        seButton->setGeometry(QRect(470, 180, 111, 24));
        test3Class->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(test3Class);
        menuBar->setObjectName("menuBar");
        menuBar->setGeometry(QRect(0, 0, 600, 21));
        test3Class->setMenuBar(menuBar);
        mainToolBar = new QToolBar(test3Class);
        mainToolBar->setObjectName("mainToolBar");
        test3Class->addToolBar(Qt::ToolBarArea::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(test3Class);
        statusBar->setObjectName("statusBar");
        test3Class->setStatusBar(statusBar);

        retranslateUi(test3Class);

        QMetaObject::connectSlotsByName(test3Class);
    } // setupUi

    void retranslateUi(QMainWindow *test3Class)
    {
        test3Class->setWindowTitle(QCoreApplication::translate("test3Class", "test3", nullptr));
        seButton->setText(QCoreApplication::translate("test3Class", "Show side effects", nullptr));
    } // retranslateUi

};

namespace Ui {
    class test3Class: public Ui_test3Class {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_TEST3_H
