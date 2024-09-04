#pragma once

#include <QDialog>
#include "ui_BrowseMoviesByGenreDialog.h"
#include "UserService.h"


class BrowseMoviesByGenreDialog : public QDialog
{
	Q_OBJECT

public:
	BrowseMoviesByGenreDialog(QWidget *parent = nullptr, UserService* us = nullptr, const std::string& genre = "");
	~BrowseMoviesByGenreDialog();

private:
	Ui::BrowseMoviesByGenreDialogClass ui;
	UserService* userv;
	std::vector<Movie> movies;
	std::vector<Movie>::iterator it;
	const std::string& genre;

	void nextButtonHandler();
	void addButtonHandler();
};
