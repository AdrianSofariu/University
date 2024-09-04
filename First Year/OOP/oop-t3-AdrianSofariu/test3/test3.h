#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_test3.h"
#include "Service.h"
#include "MedModel.h"
#include "FilterModel.h"

class test3 : public QMainWindow
{
    Q_OBJECT

private:
    Service& serv;
    MedModel* model;
	FilterModel* filter_model;

public:
    test3(Service& service, QWidget *parent = nullptr);
    ~test3();

private:
    Ui::test3Class ui;

    void populate_list();
    void search();
    void see_side_effects();
};
