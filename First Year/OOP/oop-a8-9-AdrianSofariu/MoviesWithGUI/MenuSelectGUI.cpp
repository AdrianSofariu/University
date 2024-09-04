#include "MenuSelectGUI.h"
#include <qlayout.h>


MenuSelectGUI::MenuSelectGUI(Service& serv, UserService& userv) : service{ serv }, userService{ userv }
{
	this->buildGUI();

	//connect menu buttons
	QObject::connect(this->menuOptionWidget->getAdminButton(), &QPushButton::clicked, this, &MenuSelectGUI::adminButtonHandler);
	QObject::connect(this->menuOptionWidget->getUserButton(), &QPushButton::clicked, this, &MenuSelectGUI::userButtonHandler);

	//connect back buttons from admin & user widgets
	QObject::connect(this->adminWidget->getBackButton(), &QPushButton::clicked, this, &MenuSelectGUI::backButtonHandler);
	QObject::connect(this->userWidget->getBackButton(), &QPushButton::clicked, this, &MenuSelectGUI::backButtonHandler);
}

void MenuSelectGUI::buildGUI()
{
	//set size
	this->setMinimumSize(800, 600);

	//create the central widget
	//this->centralWidget = new QWidget;
	this->stackedLayout = new QStackedLayout;

	//create the menu, admin and user widgets 
	this->menuOptionWidget = new MenuOptionWidget;
	this->adminWidget = new AdminWidget{ this->service };
	this->userWidget = new UserWidget{ this->service, this->userService };

	//add the widgets to the stacked layout
	//this->stackedLayout->addWidget(this->menuOptionWidget);
	this->stackedLayout->addWidget(this->menuOptionWidget);
	this->stackedLayout->addWidget(this->adminWidget);
	this->stackedLayout->addWidget(this->userWidget);

	//set the central widget
	//this->centralWidget->setLayout(this->stackedLayout);
	//this->setCentralWidget(this->centralWidget);
	this->setLayout(this->stackedLayout);
	
	//set menu widget as the default widget
	this->stackedLayout->setCurrentWidget(this->menuOptionWidget);
}

void MenuSelectGUI::adminButtonHandler()
{
	this->adminWidget->populateList();
	this->stackedLayout->setCurrentWidget(this->adminWidget);
}

void MenuSelectGUI::userButtonHandler()
{
	this->stackedLayout->setCurrentWidget(this->userWidget);
}

void MenuSelectGUI::backButtonHandler()
{
	this->stackedLayout->setCurrentWidget(this->menuOptionWidget);
}
