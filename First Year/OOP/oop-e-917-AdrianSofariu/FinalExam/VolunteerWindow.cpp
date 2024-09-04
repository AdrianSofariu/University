#include "VolunteerWindow.h"
#include <qmessagebox.h>
#include <Utils.h>

using namespace std;

VolunteerWindow::VolunteerWindow(Department d, Service& s, QWidget* parent) : dept{ d }, serv { s }, QWidget(parent)
{
    ui.setupUi(this);
    this->setWindowTitle(QString::fromStdString(dept.getName()));
    this->ui.description->setText(QString::fromStdString(dept.getDec()));
    populateDepList();
    populateUnassigned();
    this->ui.unassignedList->setSelectionMode(QAbstractItemView::SingleSelection);

    QObject::connect(ui.addButton, &QPushButton::clicked, this, &VolunteerWindow::add);
    QObject::connect(ui.mostSuitedButton, &QPushButton::clicked, this, &VolunteerWindow::mostSuited);
    QObject::connect(ui.assignButton, &QPushButton::clicked, this, &VolunteerWindow::assign);
}

VolunteerWindow::~VolunteerWindow()
{}

void VolunteerWindow::update()
{
    this->ui.volunteerList->clear();
    this->ui.unassignedList->clear();
    populateDepList();
    populateUnassigned();
}

void VolunteerWindow::populateDepList()
{
    vector<Volunteer> v = this->serv.getByDepartment(dept.getName());
    for (Volunteer vol : v)
    {
        QListWidgetItem* item = new QListWidgetItem(QString::fromStdString("Name: " + vol.getName() + " Email: " + vol.getEmail()));
        this->ui.volunteerList->addItem(item);
    }
}

void VolunteerWindow::populateUnassigned()
{
    vector<Volunteer> v = this->serv.getUnassigned();
    for (Volunteer vol : v)
    {
        QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(vol.getName()));
        this->ui.unassignedList->addItem(item);
    }
}

void VolunteerWindow::add()
{
    try
    {
        string name = this->ui.lineEdit->text().toStdString();
        string email = this->ui.lineEdit_2->text().toStdString();
        string interests = this->ui.lineEdit_3->text().toStdString();

        if (name == "" || email == "")
            throw exception("Name or email is invalid!\n");

        vector<string> inters = tokenize(interests, ',');

        //add item
        this->serv.add(name, email, inters);

    }
    catch (exception& e)
    {
        QMessageBox* q = new QMessageBox(QMessageBox::Critical,"Error", e.what());
        q->show();
    }
}

void VolunteerWindow::mostSuited()
{
    vector<Volunteer> ms = this->serv.mostSuited(this->dept);
    this->ui.unassignedList->clear();
    for (Volunteer vol : ms)
    {
        QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(vol.getName()));
        this->ui.unassignedList->addItem(item);
    }
}

void VolunteerWindow::assign()
{
    QList<QListWidgetItem*> selected = this->ui.unassignedList->selectedItems();
    if(selected.size() == 0)
    {
        QMessageBox* q = new QMessageBox(QMessageBox::Critical, "Error", "No selection");
        q->show();
        return;
    }

    string name = selected[0]->text().toStdString();
    this->serv.assign(name, this->dept.getName());
}
