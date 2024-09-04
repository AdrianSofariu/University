#include "Overview.h"
#include <vector>
#include "Aux.h"
#include <algorithm>

using namespace std;

Overview::Overview(Service& s, QWidget *parent) : QWidget(parent), serv{s}
{
	ui.setupUi(this);
	this->populateOverview();
}

Overview::~Overview()
{}

void Overview::populateOverview()
{
	vector<Department> dep = serv.getDepartments();
	vector<Volunteer> vol = serv.getVolunteers();
	vector<Aux> items;
	for (Department d : dep)
	{
		int count = 0;
		for (Volunteer v : vol)
			if (v.getDep() == d.getName())
				count++;
		Aux a{ d.getName(), count };
		items.push_back(a);
	}

	sort(items.begin(), items.end(), [](Aux& a1, Aux& a2) { return a1.getCount() < a2.getCount(); });

	for (Aux aux : items)
	{
		QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(aux.getDep() + " number of volunteers: " + to_string(aux.getCount())));
		this->ui.overviewList->addItem(item);
	}

}

void Overview::update()
{
	this->ui.overviewList->clear();
	this->populateOverview();
}
