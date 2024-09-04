#include "LikeMovieDialog.h"


LikeMovieDialog::LikeMovieDialog(QWidget* parent, std::string t, UserService* us) : QDialog(parent), title{t}, userv{us}
{
	ui.setupUi(this);

	QObject::connect(this->ui.closeButton, &QPushButton::clicked, this, &LikeMovieDialog::closeButtonHandler);
	QObject::connect(this->ui.likeButton, &QPushButton::clicked, this, &LikeMovieDialog::likeButtonHandler);
}

LikeMovieDialog::~LikeMovieDialog()
{}

void LikeMovieDialog::closeButtonHandler()
{
	this->close();
}

void LikeMovieDialog::likeButtonHandler()
{
	try {
		this->userv->likeMovie(this->title);
		this->close();
	}
	catch (InexistentMovieException& e) {
		this->close();
		throw e;
	}
}
