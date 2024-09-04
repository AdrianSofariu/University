/********************************************************************************
** Form generated from reading UI file 'Overview.ui'
**
** Created by: Qt User Interface Compiler version 6.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_OVERVIEW_H
#define UI_OVERVIEW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_OverviewClass
{
public:
    QListWidget *overviewList;

    void setupUi(QWidget *OverviewClass)
    {
        if (OverviewClass->objectName().isEmpty())
            OverviewClass->setObjectName("OverviewClass");
        OverviewClass->resize(600, 400);
        overviewList = new QListWidget(OverviewClass);
        overviewList->setObjectName("overviewList");
        overviewList->setGeometry(QRect(50, 30, 281, 271));

        retranslateUi(OverviewClass);

        QMetaObject::connectSlotsByName(OverviewClass);
    } // setupUi

    void retranslateUi(QWidget *OverviewClass)
    {
        OverviewClass->setWindowTitle(QCoreApplication::translate("OverviewClass", "Overview", nullptr));
    } // retranslateUi

};

namespace Ui {
    class OverviewClass: public Ui_OverviewClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_OVERVIEW_H
