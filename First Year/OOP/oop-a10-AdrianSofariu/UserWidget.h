#pragma once
#pragma once
#include <QWidget>
#include <QPushButton>
#include "Service.h"
#include "UserService.h"
#include <qlistwidget.h>
#include <qlineedit.h>
#include <qtableview.h>
#include "WatchlistModel.h"
#include <qboxlayout.h>

class UserWidget : public QWidget
{
	Service& serv;
	UserService& userv;

	QTableView* watchlistTable;
	WatchlistModel* watchlistModel;

	QLineEdit* titleEdit;
	QLineEdit* genreEdit;
	QLineEdit* fileEdit;

	QPushButton* openWatchlistButton;
	QPushButton* seeMoviesofGenreButton;
	QPushButton* removeButton;
	QPushButton* saveButton;
	QPushButton* backToMenuButton;
	QPushButton* seeWatchlistButton;


public:
	UserWidget(Service& serv, UserService& userv);
	QPushButton* getBackButton() const { return this->backToMenuButton; }

private:
	void buildGUI();
	void removeButtonHandler();
	void saveButtonHandler();
	void seeMoviesofGenreButtonHandler();
	void seeWatchlistButtonHandler();
	void openWatchlistButtonHandler();
};

