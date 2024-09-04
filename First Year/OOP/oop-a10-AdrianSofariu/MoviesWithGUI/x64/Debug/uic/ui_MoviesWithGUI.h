/********************************************************************************
** Form generated from reading UI file 'MoviesWithGUI.ui'
**
** Created by: Qt User Interface Compiler version 6.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MOVIESWITHGUI_H
#define UI_MOVIESWITHGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MoviesWithGUIClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MoviesWithGUIClass)
    {
        if (MoviesWithGUIClass->objectName().isEmpty())
            MoviesWithGUIClass->setObjectName("MoviesWithGUIClass");
        MoviesWithGUIClass->resize(600, 400);
        menuBar = new QMenuBar(MoviesWithGUIClass);
        menuBar->setObjectName("menuBar");
        MoviesWithGUIClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MoviesWithGUIClass);
        mainToolBar->setObjectName("mainToolBar");
        MoviesWithGUIClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(MoviesWithGUIClass);
        centralWidget->setObjectName("centralWidget");
        MoviesWithGUIClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(MoviesWithGUIClass);
        statusBar->setObjectName("statusBar");
        MoviesWithGUIClass->setStatusBar(statusBar);

        retranslateUi(MoviesWithGUIClass);

        QMetaObject::connectSlotsByName(MoviesWithGUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *MoviesWithGUIClass)
    {
        MoviesWithGUIClass->setWindowTitle(QCoreApplication::translate("MoviesWithGUIClass", "MoviesWithGUI", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MoviesWithGUIClass: public Ui_MoviesWithGUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MOVIESWITHGUI_H
