#pragma once
#include <QWidget>
#include <QPushButton>
#include "Service.h"
#include <qlistwidget.h>
#include <qlineedit.h>
#include <qshortcut.h>

class AdminWidget : public QWidget
{
private:
	Service& serv;

	QListWidget* movieList;
	QLineEdit* titleEdit;
	QLineEdit* genreEdit;
	QLineEdit* yearEdit;
	QLineEdit* likesEdit;
	QLineEdit* trailerEdit;

	QPushButton* addButton;
	QPushButton* deleteButton;
	QPushButton* updateButton;
	QPushButton* filterButton;
	QPushButton* backToMenuButton;
	QPushButton* undoButton;
	QPushButton* redoButton;

	QShortcut* undoShortcut;
	QShortcut* redoShortcut;

public:
	AdminWidget(Service& serv);
	QPushButton* getBackButton() const { return this->backToMenuButton; }

private:
	void buildGUI();
	void addButtonHandler();
	void deleteButtonHandler();
	void updateButtonHandler();
	void undoButtonHandler();
	void redoButtonHandler();

public:
	void populateList();
};

