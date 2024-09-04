#include "AdminWidget.h"
#include <qlayout.h>
#include <qlabel.h>
#include <qmessagebox.h>

AdminWidget::AdminWidget(Service& serv) : serv{serv}
{
	this->buildGUI();
	this->populateList();
	QObject::connect(this->addButton, &QPushButton::clicked, this, &AdminWidget::addButtonHandler);
	QObject::connect(this->deleteButton, &QPushButton::clicked, this, &AdminWidget::deleteButtonHandler);
	QObject::connect(this->updateButton, &QPushButton::clicked, this, &AdminWidget::updateButtonHandler);
	QObject::connect(this->undoButton, &QPushButton::clicked, this, &AdminWidget::undoButtonHandler);
	QObject::connect(this->redoButton, &QPushButton::clicked, this, &AdminWidget::redoButtonHandler);

	//connect the shortcuts
	QObject::connect(this->undoShortcut, &QShortcut::activated, this, &AdminWidget::undoButtonHandler);
	QObject::connect(this->redoShortcut, &QShortcut::activated, this, &AdminWidget::redoButtonHandler);
}

void AdminWidget::buildGUI()
{
	//build the GUI
	QHBoxLayout* layout = new QHBoxLayout{ this };

	//build the list with labels and input fields
	this->movieList = new QListWidget;
	layout->addWidget(this->movieList);

	QGridLayout* grid = new QGridLayout;

	QLabel* titleLabel = new QLabel{ "Title" };
	this->titleEdit = new QLineEdit;


	QLabel* genreLabel = new QLabel{ "Genre" };
	this->genreEdit = new QLineEdit;

	QLabel* yearLabel = new QLabel{ "Year" };
	this->yearEdit = new QLineEdit;

	QLabel* likesLabel = new QLabel{ "Likes" };
	this->likesEdit = new QLineEdit;

	QLabel* trailerLabel = new QLabel{ "Trailer" };
	this->trailerEdit = new QLineEdit;

	grid->addWidget(titleLabel, 0, 0);
	grid->addWidget(this->titleEdit, 0, 1);
	grid->addWidget(genreLabel, 1, 0);
	grid->addWidget(this->genreEdit, 1, 1);
	grid->addWidget(yearLabel, 2, 0);
	grid->addWidget(this->yearEdit, 2, 1);
	grid->addWidget(likesLabel, 3, 0);
	grid->addWidget(this->likesEdit, 3, 1);
	grid->addWidget(trailerLabel, 4, 0);
	grid->addWidget(this->trailerEdit, 4, 1);

	//build the buttons
	QVBoxLayout* buttonsLayout = new QVBoxLayout;
	this->addButton = new QPushButton{ "Add" };
	this->deleteButton = new QPushButton{ "Delete" };
	this->updateButton = new QPushButton{ "Update" };
	this->backToMenuButton = new QPushButton{ "Back to menu" };
	this->undoButton = new QPushButton{ "Undo" };
	this->redoButton = new QPushButton{ "Redo" };

	this->addButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->deleteButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->updateButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->backToMenuButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->undoButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->redoButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);


	buttonsLayout->addWidget(this->addButton);
	buttonsLayout->addWidget(this->deleteButton);
	buttonsLayout->addWidget(this->updateButton);
	buttonsLayout->addWidget(this->backToMenuButton);
	buttonsLayout->addWidget(this->undoButton);
	buttonsLayout->addWidget(this->redoButton);

	//add shortcuts
	this->undoShortcut = new QShortcut(QKeySequence(Qt::CTRL | Qt::Key_Z), this);
	this->redoShortcut = new QShortcut(QKeySequence(Qt::CTRL | Qt::Key_Y), this);

	//add the layouts to the main layout
	layout->addLayout(grid);
	layout->addLayout(buttonsLayout);

	this->setLayout(layout);
	this->setMinimumSize(800, 600);
}

void AdminWidget::populateList()
{
	//clear the list
	this->movieList->clear();

	//get the movies from the service
	for (auto& m : this->serv.getRepo())
	{
		this->movieList->addItem(QString::fromStdString(m));
	}
}

void AdminWidget::addButtonHandler()
{
	QString title = this->titleEdit->text();
	QString genre = this->genreEdit->text();
	QString year = this->yearEdit->text();
	QString likes = this->likesEdit->text();
	QString trailer = this->trailerEdit->text();

	try
	{
		Movie m{ title.toStdString(), genre.toStdString(), year.toInt(), likes.toInt(), trailer.toStdString() };
		this->serv.addToRepo(m);
		this->populateList();

		//clear the input fields
		this->titleEdit->clear();
		this->genreEdit->clear();
		this->yearEdit->clear();
		this->likesEdit->clear();
		this->trailerEdit->clear();
	}
	catch (MovieException& e)
	{
		QString message;
		for (auto& s : e.getErrors())
		{
			message.append(QString::fromStdString(s));
		}
		QMessageBox::critical(this, "Error", message);
	}
	catch (RepositoryException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
	catch (FileException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
}

void AdminWidget::deleteButtonHandler()
{
	QString title = this->titleEdit->text();

	try
	{
		this->serv.removeFromRepo(title.toStdString());
		this->populateList();
		this->titleEdit->clear();
	}
	catch (RepositoryException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
	catch (FileException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
}

void AdminWidget::updateButtonHandler()
{
	QString title = this->titleEdit->text();
	QString genre = this->genreEdit->text();
	QString year = this->yearEdit->text();
	QString likes = this->likesEdit->text();
	QString trailer = this->trailerEdit->text();

	try
	{
		Movie m{ title.toStdString(), genre.toStdString(), year.toInt(), likes.toInt(), trailer.toStdString() };
		this->serv.updateInRepo(m, title.toStdString());
		this->populateList();

		//clear the input fields
		this->titleEdit->clear();
		this->genreEdit->clear();
		this->yearEdit->clear();
		this->likesEdit->clear();
		this->trailerEdit->clear();
	}
	catch (MovieException& e)
	{
		QString message;
		for (auto& s : e.getErrors())
		{
			message.append(QString::fromStdString(s));
		}
		QMessageBox::critical(this, "Error", message);
	}
	catch (RepositoryException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
	catch (FileException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
}

void AdminWidget::undoButtonHandler()
{
	try {
		this->serv.undo();
		this->populateList();
	}
	catch (UndoException& e)
	{
		QMessageBox::critical(this, "Error", e.what());

	}
}

void AdminWidget::redoButtonHandler()
{
	try {
		this->serv.redo();
		this->populateList();
	}
	catch (RedoException& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
}


