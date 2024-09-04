/********************************************************************************
** Form generated from reading UI file 'VolunteerWindow.ui'
**
** Created by: Qt User Interface Compiler version 6.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_VOLUNTEERWINDOW_H
#define UI_VOLUNTEERWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_VolunteerWindowClass
{
public:
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QLabel *description;
    QHBoxLayout *horizontalLayout;
    QListWidget *volunteerList;
    QListWidget *unassignedList;
    QWidget *verticalLayoutWidget_2;
    QVBoxLayout *verticalLayout_2;
    QGridLayout *gridLayout;
    QLineEdit *lineEdit_2;
    QLabel *email;
    QLineEdit *lineEdit;
    QLabel *name;
    QLineEdit *lineEdit_3;
    QLabel *interests;
    QPushButton *addButton;
    QPushButton *mostSuitedButton;
    QPushButton *assignButton;

    void setupUi(QWidget *VolunteerWindowClass)
    {
        if (VolunteerWindowClass->objectName().isEmpty())
            VolunteerWindowClass->setObjectName("VolunteerWindowClass");
        VolunteerWindowClass->resize(600, 400);
        verticalLayoutWidget = new QWidget(VolunteerWindowClass);
        verticalLayoutWidget->setObjectName("verticalLayoutWidget");
        verticalLayoutWidget->setGeometry(QRect(20, 30, 321, 351));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        description = new QLabel(verticalLayoutWidget);
        description->setObjectName("description");

        verticalLayout->addWidget(description);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName("horizontalLayout");
        volunteerList = new QListWidget(verticalLayoutWidget);
        volunteerList->setObjectName("volunteerList");

        horizontalLayout->addWidget(volunteerList);

        unassignedList = new QListWidget(verticalLayoutWidget);
        unassignedList->setObjectName("unassignedList");

        horizontalLayout->addWidget(unassignedList);


        verticalLayout->addLayout(horizontalLayout);

        verticalLayoutWidget_2 = new QWidget(VolunteerWindowClass);
        verticalLayoutWidget_2->setObjectName("verticalLayoutWidget_2");
        verticalLayoutWidget_2->setGeometry(QRect(360, 50, 160, 331));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget_2);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName("verticalLayout_2");
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName("gridLayout");
        lineEdit_2 = new QLineEdit(verticalLayoutWidget_2);
        lineEdit_2->setObjectName("lineEdit_2");

        gridLayout->addWidget(lineEdit_2, 1, 1, 1, 1);

        email = new QLabel(verticalLayoutWidget_2);
        email->setObjectName("email");

        gridLayout->addWidget(email, 1, 0, 1, 1);

        lineEdit = new QLineEdit(verticalLayoutWidget_2);
        lineEdit->setObjectName("lineEdit");

        gridLayout->addWidget(lineEdit, 0, 1, 1, 1);

        name = new QLabel(verticalLayoutWidget_2);
        name->setObjectName("name");

        gridLayout->addWidget(name, 0, 0, 1, 1);

        lineEdit_3 = new QLineEdit(verticalLayoutWidget_2);
        lineEdit_3->setObjectName("lineEdit_3");

        gridLayout->addWidget(lineEdit_3, 2, 1, 1, 1);

        interests = new QLabel(verticalLayoutWidget_2);
        interests->setObjectName("interests");

        gridLayout->addWidget(interests, 2, 0, 1, 1);


        verticalLayout_2->addLayout(gridLayout);

        addButton = new QPushButton(verticalLayoutWidget_2);
        addButton->setObjectName("addButton");

        verticalLayout_2->addWidget(addButton);

        mostSuitedButton = new QPushButton(verticalLayoutWidget_2);
        mostSuitedButton->setObjectName("mostSuitedButton");

        verticalLayout_2->addWidget(mostSuitedButton);

        assignButton = new QPushButton(verticalLayoutWidget_2);
        assignButton->setObjectName("assignButton");

        verticalLayout_2->addWidget(assignButton);


        retranslateUi(VolunteerWindowClass);

        QMetaObject::connectSlotsByName(VolunteerWindowClass);
    } // setupUi

    void retranslateUi(QWidget *VolunteerWindowClass)
    {
        VolunteerWindowClass->setWindowTitle(QCoreApplication::translate("VolunteerWindowClass", "VolunteerWindow", nullptr));
        description->setText(QCoreApplication::translate("VolunteerWindowClass", "TextLabel", nullptr));
        email->setText(QCoreApplication::translate("VolunteerWindowClass", "email", nullptr));
        name->setText(QCoreApplication::translate("VolunteerWindowClass", "name", nullptr));
        interests->setText(QCoreApplication::translate("VolunteerWindowClass", "interests", nullptr));
        addButton->setText(QCoreApplication::translate("VolunteerWindowClass", "add", nullptr));
        mostSuitedButton->setText(QCoreApplication::translate("VolunteerWindowClass", "mostSuited", nullptr));
        assignButton->setText(QCoreApplication::translate("VolunteerWindowClass", "assign", nullptr));
    } // retranslateUi

};

namespace Ui {
    class VolunteerWindowClass: public Ui_VolunteerWindowClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_VOLUNTEERWINDOW_H
