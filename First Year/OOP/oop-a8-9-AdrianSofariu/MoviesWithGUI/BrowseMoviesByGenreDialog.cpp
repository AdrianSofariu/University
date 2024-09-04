#include "BrowseMoviesByGenreDialog.h"
#include <qmessagebox.h>

BrowseMoviesByGenreDialog::BrowseMoviesByGenreDialog(QWidget *parent, UserService* us, const std::string& g)
	: QDialog(parent), userv{ us }, genre{ g }
{
	ui.setupUi(this);

	QObject::connect(this->ui.nextButton, &QPushButton::clicked, this, &BrowseMoviesByGenreDialog::nextButtonHandler);
	QObject::connect(this->ui.addButton, &QPushButton::clicked, this, &BrowseMoviesByGenreDialog::addButtonHandler);

	//prepare the list of movies
	this->movies = this->userv->browseByGenre(this->genre);
	if (this->movies.size() == 0) {
		throw InexistentMovieException();
	}
	this->it = this->movies.begin();

	//display the genre & first movie
	if(this->genre == "")
		ui.genreLabel->setText("All movies");
	else
		ui.genreLabel->setText(QString::fromStdString(this->genre));
	ui.movieLabel->setText(QString::fromStdString(this->it->toString()));
	//open link
	this->userv->openLink(*this->it);

}

BrowseMoviesByGenreDialog::~BrowseMoviesByGenreDialog()
{}

void BrowseMoviesByGenreDialog::nextButtonHandler()
{
	it++;
	if (it == this->movies.end())
		it = this->movies.begin();

	//display the movie
	ui.movieLabel->setText(QString::fromStdString(this->it->toString()));
	this->userv->openLink(*this->it);
}

void BrowseMoviesByGenreDialog::addButtonHandler()
{
	try {
		this->userv->addToWatchlist(*this->it);
		QMessageBox::information(this, "Success", "Movie added to watchlist!");
	}
	catch (DuplicateMovieException& e) {
		QMessageBox::critical(this, "Error", e.what());
	}
}
