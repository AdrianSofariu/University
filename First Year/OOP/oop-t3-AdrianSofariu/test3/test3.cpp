#include "test3.h"
#include <QMessageBox>

test3::test3(Service& service, QWidget *parent)
	: QMainWindow(parent), serv{ service }
{
    ui.setupUi(this);
	this->populate_list();
	QObject::connect(this->ui.searchBar, &QLineEdit::textChanged, this, &test3::search);
	QObject::connect(this->ui.seButton, &QPushButton::clicked, this, &test3::see_side_effects);
}

test3::~test3()
{}

void test3::populate_list()
{
	std::vector<Medication> meds = this->serv.get_medications();
	std::sort(meds.begin(), meds.end(), [](const Medication& m1, const Medication& m2) { return m1.get_category() < m2.get_category(); });
	this->model = new MedModel{ meds };
	this->filter_model = new FilterModel{};
	this->filter_model->setSourceModel(this->model);
	this->ui.medList->setModel(this->filter_model);
}

void test3::search()
{
	QString text = this->ui.searchBar->text();
	this->filter_model->setFilter(text);
}

void test3::see_side_effects()
{
	try{
		this->ui.seList->clear();
		std::string name = this->ui.medEdit->text().toStdString();
		std::vector<std::string> side_effects = this->serv.get_side_effects(name);
		for (std::string se : side_effects)
			this->ui.seList->addItem(QString::fromStdString(se));
	}
	catch (std::exception& e)
	{
		QMessageBox::critical(this, "Error", e.what());
	}
}
