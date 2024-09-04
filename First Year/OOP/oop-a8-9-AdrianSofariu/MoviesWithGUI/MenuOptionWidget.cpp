#include "MenuOptionWidget.h"
#include <QVBoxLayout>


MenuOptionWidget::MenuOptionWidget()
{
	buildGUI();
}

void MenuOptionWidget::buildGUI()
{
	QVBoxLayout* mainLayout = new QVBoxLayout;

	this->adminButton = new QPushButton{ "Admin" };
	this->userButton = new QPushButton{ "User" };

	//make the buttons expand horizontally & vertically
	this->adminButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
	this->userButton->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);

	//add the buttons to the layout
	mainLayout->addWidget(this->adminButton);
	mainLayout->addWidget(this->userButton);

	
	this->setLayout(mainLayout);
	this->resize(800, 600);
}

