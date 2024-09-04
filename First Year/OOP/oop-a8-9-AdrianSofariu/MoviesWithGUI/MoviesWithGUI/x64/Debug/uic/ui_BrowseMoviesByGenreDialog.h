/********************************************************************************
** Form generated from reading UI file 'BrowseMoviesByGenreDialog.ui'
**
** Created by: Qt User Interface Compiler version 6.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BROWSEMOVIESBYGENREDIALOG_H
#define UI_BROWSEMOVIESBYGENREDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_BrowseMoviesByGenreDialogClass
{
public:
    QLabel *titleLabel;
    QLabel *genreLabel;
    QLabel *movieLabel;
    QPushButton *addButton;
    QPushButton *nextButton;

    void setupUi(QDialog *BrowseMoviesByGenreDialogClass)
    {
        if (BrowseMoviesByGenreDialogClass->objectName().isEmpty())
            BrowseMoviesByGenreDialogClass->setObjectName("BrowseMoviesByGenreDialogClass");
        BrowseMoviesByGenreDialogClass->resize(600, 400);
        titleLabel = new QLabel(BrowseMoviesByGenreDialogClass);
        titleLabel->setObjectName("titleLabel");
        titleLabel->setGeometry(QRect(10, 20, 211, 16));
        genreLabel = new QLabel(BrowseMoviesByGenreDialogClass);
        genreLabel->setObjectName("genreLabel");
        genreLabel->setGeometry(QRect(210, 20, 101, 16));
        QSizePolicy sizePolicy(QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(genreLabel->sizePolicy().hasHeightForWidth());
        genreLabel->setSizePolicy(sizePolicy);
        movieLabel = new QLabel(BrowseMoviesByGenreDialogClass);
        movieLabel->setObjectName("movieLabel");
        movieLabel->setGeometry(QRect(10, 50, 581, 101));
        sizePolicy.setHeightForWidth(movieLabel->sizePolicy().hasHeightForWidth());
        movieLabel->setSizePolicy(sizePolicy);
        movieLabel->setScaledContents(false);
        movieLabel->setWordWrap(true);
        addButton = new QPushButton(BrowseMoviesByGenreDialogClass);
        addButton->setObjectName("addButton");
        addButton->setGeometry(QRect(299, 340, 161, 24));
        nextButton = new QPushButton(BrowseMoviesByGenreDialogClass);
        nextButton->setObjectName("nextButton");
        nextButton->setGeometry(QRect(480, 340, 80, 24));

        retranslateUi(BrowseMoviesByGenreDialogClass);

        QMetaObject::connectSlotsByName(BrowseMoviesByGenreDialogClass);
    } // setupUi

    void retranslateUi(QDialog *BrowseMoviesByGenreDialogClass)
    {
        BrowseMoviesByGenreDialogClass->setWindowTitle(QCoreApplication::translate("BrowseMoviesByGenreDialogClass", "BrowseMoviesByGenreDialog", nullptr));
        titleLabel->setText(QCoreApplication::translate("BrowseMoviesByGenreDialogClass", "You are browsing movies of genre:", nullptr));
        genreLabel->setText(QString());
        movieLabel->setText(QString());
        addButton->setText(QCoreApplication::translate("BrowseMoviesByGenreDialogClass", "add to watchlist", nullptr));
        nextButton->setText(QCoreApplication::translate("BrowseMoviesByGenreDialogClass", "next", nullptr));
    } // retranslateUi

};

namespace Ui {
    class BrowseMoviesByGenreDialogClass: public Ui_BrowseMoviesByGenreDialogClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BROWSEMOVIESBYGENREDIALOG_H
