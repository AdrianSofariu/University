#pragma once
#include "ui_MoviesWithGUI.h"
#include "AdminWidget.h"
#include "UserWidget.h"
#include "Service.h"
#include "UserService.h"
#include <qpushbutton.h>
#include <qstackedwidget.h>
#include <qwindow.h>
#include "MenuOptionWidget.h"
#include <qstackedlayout.h>


class MenuSelectGUI : public QWidget
{
private:
	//sevices
	Service& service;
	UserService& userService;

	//ui content

	QStackedLayout* stackedLayout;
	QWidget* centralWidget;

	MenuOptionWidget* menuOptionWidget;
	AdminWidget* adminWidget;
	UserWidget* userWidget;

public:
	MenuSelectGUI(Service& serv, UserService& userv);
private:
	void buildGUI();
	void adminButtonHandler();
	void userButtonHandler();
	void backButtonHandler();
};