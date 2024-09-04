#include "MoviesWithGUI.h"
#include <qlayout.h>
#include <qmessagebox.h>
#include "Exceptions.h"
#include "MenuSelectGUI.h"


MoviesWithGUI::MoviesWithGUI()
{
	this->buildGUI();
	QObject::connect(this->csvButton, &QPushButton::clicked, this, &MoviesWithGUI::csvButtonHandler);
	QObject::connect(this->htmlButton, &QPushButton::clicked, this, &MoviesWithGUI::htmlButtonHandler);
}

void MoviesWithGUI::buildGUI()
{
	QWidget* centralWidget = new QWidget;
	QVBoxLayout* mainLayout = new QVBoxLayout;

	this->csvButton = new QPushButton{"CSV Watchlist"};
	this->htmlButton = new QPushButton{ "HTML Watchlist" };
	
	//make the buttons expand horizontally & vertically
	this->csvButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->htmlButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);

	//add the buttons to the layout
	mainLayout->addWidget(this->csvButton);
	mainLayout->addWidget(this->htmlButton);

	centralWidget->setLayout(mainLayout);
	this->setCentralWidget(centralWidget);
}

void MoviesWithGUI::csvButtonHandler()
{
	//open the main menu window with a CSV watchlist
	try {
		this->repo = new TextFileRepository{ "Movies.txt" };
		this->watchlist = new CSVWatchlist;
		this->serv = new Service{ *repo };
		this->userv = new UserService{ *repo, *watchlist };


		this->centralWidget = new MenuSelectGUI{ *this->serv, *this->userv };
		this->setCentralWidget(this->centralWidget);
		
	}
	catch (FileException& e) {
		QMessageBox::critical(this, "Error", e.what());
	}
}

void MoviesWithGUI::htmlButtonHandler()
{
	//open the main menu window with an HTML watchlist
	try {

		this->repo = new TextFileRepository{ "Movies.txt" };
		this->watchlist = new HTMLWatchlist;
		this->serv = new Service{ *repo };
		this->userv = new UserService{ *repo, *watchlist };
		this->centralWidget = new MenuSelectGUI{ *this->serv, *this->userv };

		//show the main menu while replacing the current window
		//this->newWindow = new MenuSelectGUI{ service, uservice };
		//this->newWindow->show();
		this->centralWidget = new MenuSelectGUI{ *this->serv, *this->userv };
		this->setCentralWidget(this->centralWidget);
		
	}
	catch (FileException& e) {
		QMessageBox::critical(this, "Error", e.what());
	}
}
