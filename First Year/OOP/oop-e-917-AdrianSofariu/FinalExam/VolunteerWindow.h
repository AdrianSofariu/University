#pragma once

#include <QtWidgets/QWidget>
#include "ui_VolunteerWindow.h"
#include "Service.h"
#include "Department.h"

class VolunteerWindow : public QWidget, public Observer
{
    Q_OBJECT

public:
    VolunteerWindow(Department d, Service& s, QWidget* parent = nullptr);
    ~VolunteerWindow();
    void update() override;

private:
    Ui::VolunteerWindowClass ui;
    Service& serv;
    Department dept;
    
    void populateDepList();
    void populateUnassigned();
    void add();
    void mostSuited();
    void assign();
};
