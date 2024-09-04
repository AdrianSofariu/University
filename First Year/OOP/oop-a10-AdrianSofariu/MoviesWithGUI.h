#pragma once

#include <qpushbutton.h>
#include "ui_MoviesWithGUI.h"
#include "TextFileRepository.h"
#include "Service.h"
#include "UserService.h"
#include "CSVWatchlist.h"
#include "HTMLWatchlist.h"
#include "FileWatchlist.h"
#include <iostream>

class MoviesWithGUI : public QMainWindow
{
private:
	Ui::MoviesWithGUIClass ui;
	//QMainWindow* newWindow;
	QWidget* centralWidget;

    QPushButton* csvButton;
	QPushButton* htmlButton;

	Repository* repo;
	Service* serv;
	UserService* userv;
	FileWatchlist* watchlist;

public:
	MoviesWithGUI();
private:
	void buildGUI();
	void csvButtonHandler();
	void htmlButtonHandler();
};
