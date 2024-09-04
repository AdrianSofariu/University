#pragma once

#include <QDialog>
#include "ui_LikeMovieDialog.h"
#include "UserService.h"

class LikeMovieDialog : public QDialog
{
	Q_OBJECT

public:
	LikeMovieDialog(QWidget *parent = nullptr, std::string t = "", UserService* us = nullptr);
	~LikeMovieDialog();

private:
	Ui::LikeMovieDialogClass ui;
	std::string title;
	UserService* userv;
	
	void closeButtonHandler();
	void likeButtonHandler();
};
