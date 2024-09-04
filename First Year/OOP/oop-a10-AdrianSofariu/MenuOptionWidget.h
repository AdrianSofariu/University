#pragma once
#include <QWidget>
#include <QPushButton>

class MenuOptionWidget : public QWidget
{
private:
	QPushButton* adminButton;
	QPushButton* userButton;

public:
	MenuOptionWidget();
	QPushButton* getAdminButton() const { return this->adminButton; }
	QPushButton* getUserButton() const { return this->userButton; }

private:
	void buildGUI();
};

