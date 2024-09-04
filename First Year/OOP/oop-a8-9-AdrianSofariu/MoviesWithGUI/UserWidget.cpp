#include "UserWidget.h"
#include <qlayout.h>
#include <qlabel.h>
#include <qmessagebox.h>
#include "LikeMovieDialog.h"
#include "BrowseMoviesByGenreDialog.h"

UserWidget::UserWidget(Service& serv, UserService& userv) : serv{ serv }, userv{ userv }
{
	this->buildGUI();
	QObject::connect(this->removeButton, &QPushButton::clicked, this, &UserWidget::removeButtonHandler);
	QObject::connect(this->saveButton, &QPushButton::clicked, this, &UserWidget::saveButtonHandler);
	QObject::connect(this->seeMoviesofGenreButton, &QPushButton::clicked, this, &UserWidget::seeMoviesofGenreButtonHandler);
	QObject::connect(this->seeWatchlistButton, &QPushButton::clicked, this, &UserWidget::seeWatchlistButtonHandler);
	QObject::connect(this->openWatchlistButton, &QPushButton::clicked, this, &UserWidget::openWatchlistButtonHandler);
}

void UserWidget::buildGUI()
{
	//build the GUI
	QHBoxLayout* layout = new QHBoxLayout{ this };

	QGridLayout* grid = new QGridLayout;

	QLabel* titleLabel = new QLabel{ "Title" };
	this->titleEdit = new QLineEdit;

	QLabel* genreLabel = new QLabel{ "Genre" };
	this->genreEdit = new QLineEdit;

	QLabel* fileLabel = new QLabel{ "File" };
	this->fileEdit = new QLineEdit;

	grid->addWidget(titleLabel, 0, 0);
	grid->addWidget(this->titleEdit, 0, 1);
	grid->addWidget(genreLabel, 1, 0);
	grid->addWidget(this->genreEdit, 1, 1);
	grid->addWidget(fileLabel, 2, 0);
	grid->addWidget(this->fileEdit, 2, 1);

	//build the buttons
	QVBoxLayout* buttonsLayout = new QVBoxLayout;
	this->seeMoviesofGenreButton = new QPushButton{ "See Movies of genre" };
	this->removeButton = new QPushButton{ "Remove from watchlist" };
	this->saveButton = new QPushButton{ "Save watchlist" };
	this->backToMenuButton = new QPushButton{ "Back to menu" };
	this->seeWatchlistButton = new QPushButton{ "See watchlist" };
	this->openWatchlistButton = new QPushButton{ "Open watchlist" };

	this->seeMoviesofGenreButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->removeButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->seeWatchlistButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->saveButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->backToMenuButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->openWatchlistButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);


	buttonsLayout->addWidget(this->seeMoviesofGenreButton);
	buttonsLayout->addWidget(this->removeButton);
	buttonsLayout->addWidget(this->saveButton);
	buttonsLayout->addWidget(this->seeWatchlistButton);
	buttonsLayout->addWidget(this->openWatchlistButton);
	buttonsLayout->addWidget(this->backToMenuButton);

	//add the layouts to the main layout
	layout->addLayout(grid);
	layout->addLayout(buttonsLayout);

	this->setLayout(layout);
	this->setMinimumSize(800, 600);
}

void UserWidget::removeButtonHandler()
{
	QString title = this->titleEdit->text();
	try
	{
		this->userv.removeFromWatchlist(title.toStdString());
		this->titleEdit->clear();

		//if removal was succesful, open a like movie dialog
		LikeMovieDialog* dialog = new LikeMovieDialog{this, title.toStdString(), &this->userv};
		dialog->exec();
	}
	catch (InexistentMovieException& e)
	{
		this->titleEdit->clear();
		QMessageBox::critical(this, "Error", e.what());
	}
}

void UserWidget::saveButtonHandler()
{
	QString filename = this->fileEdit->text();
	if (filename.isEmpty())
	{
		QMessageBox::critical(this, "Error", "Please provide a filename.");
		return;
	}

	try {
		this->userv.saveWatchlist(filename.toStdString());
		if (this->userv.getWatchlist().size() == 0)
		{
			QMessageBox::critical(this, "Error", "The watchlist cannot be displayed.");
			return;
		}
		QMessageBox::information(this, "Success", "Watchlist saved successfully.");
	}
	catch (FileException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
}

void UserWidget::seeMoviesofGenreButtonHandler()
{
	QString genre = this->genreEdit->text();
	try {
		BrowseMoviesByGenreDialog* dialog = new BrowseMoviesByGenreDialog{ this, &this->userv, genre.toStdString() };
		dialog->exec();
		genreEdit->clear();
	}
	catch (InexistentMovieException& e)
	{
		genreEdit->clear();
		QMessageBox::critical(this, "Error", "No movies of the given genre!");
	}
}

void UserWidget::seeWatchlistButtonHandler()
{
	
	try {
		this->watchlistTable = new QTableView;
		std::vector<Movie> aux = this->userv.getWatchlistMovies();
		this->watchlistModel = new WatchlistModel{ this, aux };
		this->watchlistTable->setModel(this->watchlistModel);
		this->watchlistTable->resizeColumnsToContents();
		this->watchlistTable->resizeRowsToContents();
		this->watchlistTable->resize(800, 600);
		this->watchlistTable->show();
	}
	catch (EmptyWatchlistException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}	
}

void UserWidget::openWatchlistButtonHandler()
{
	try {
		this->userv.openWatchlist();
	}
	catch (EmptyWatchlistException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
	catch (FileException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
}


