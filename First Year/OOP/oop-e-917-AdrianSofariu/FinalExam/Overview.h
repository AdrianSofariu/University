#pragma once

#include <QWidget>
#include "ui_Overview.h"
#include "Service.h"

class Overview : public QWidget, public Observer
{
	Q_OBJECT

public:
	Overview(Service& s, QWidget *parent = nullptr);
	~Overview();

private:
	Ui::OverviewClass ui;
	Service& serv;

	void populateOverview();
	void update() override;
};
