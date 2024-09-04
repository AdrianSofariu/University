/********************************************************************************
** Form generated from reading UI file 'LikeMovieDialog.ui'
**
** Created by: Qt User Interface Compiler version 6.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LIKEMOVIEDIALOG_H
#define UI_LIKEMOVIEDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_LikeMovieDialogClass
{
public:
    QLabel *message;
    QPushButton *likeButton;
    QPushButton *closeButton;

    void setupUi(QDialog *LikeMovieDialogClass)
    {
        if (LikeMovieDialogClass->objectName().isEmpty())
            LikeMovieDialogClass->setObjectName("LikeMovieDialogClass");
        LikeMovieDialogClass->resize(453, 277);
        message = new QLabel(LikeMovieDialogClass);
        message->setObjectName("message");
        message->setGeometry(QRect(30, 40, 381, 131));
        likeButton = new QPushButton(LikeMovieDialogClass);
        likeButton->setObjectName("likeButton");
        likeButton->setGeometry(QRect(250, 230, 80, 24));
        closeButton = new QPushButton(LikeMovieDialogClass);
        closeButton->setObjectName("closeButton");
        closeButton->setGeometry(QRect(340, 230, 80, 24));
        closeButton->setFocusPolicy(Qt::FocusPolicy::TabFocus);

        retranslateUi(LikeMovieDialogClass);

        QMetaObject::connectSlotsByName(LikeMovieDialogClass);
    } // setupUi

    void retranslateUi(QDialog *LikeMovieDialogClass)
    {
        LikeMovieDialogClass->setWindowTitle(QCoreApplication::translate("LikeMovieDialogClass", "LikeMovieDialog", nullptr));
        message->setText(QCoreApplication::translate("LikeMovieDialogClass", "Would you like to leave a postive review?", nullptr));
        likeButton->setText(QCoreApplication::translate("LikeMovieDialogClass", "Like", nullptr));
        closeButton->setText(QCoreApplication::translate("LikeMovieDialogClass", "Later", nullptr));
    } // retranslateUi

};

namespace Ui {
    class LikeMovieDialogClass: public Ui_LikeMovieDialogClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LIKEMOVIEDIALOG_H
