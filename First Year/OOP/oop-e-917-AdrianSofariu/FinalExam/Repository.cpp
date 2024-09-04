#include "Repository.h"
#include <fstream>

using namespace std;

void Repository::add(Volunteer v)
{
	if (find(this->volunteers.begin(), this->volunteers.end(), v) != volunteers.end())
		throw exception("Invalid volunteer!");
	this->volunteers.push_back(v);
	this->notify();
}

void Repository::assign(std::string name, std::string dep)
{
	for (Volunteer& v : this->volunteers)
		if (name == v.getName())
			v.setDep(dep);
	this->notify();
}

void Repository::readFromFile()
{
	ifstream f{ this->dfile };
	ifstream g{ this->vfile };

	if (!f.is_open())
		throw exception("Cannot read departments!\n");

	if (!g.is_open())
		throw exception("Cannot read volunteers!\n");

	Department d;
	while (f >> d)
	{
		this->departments.push_back(d);
	}

	Volunteer v;
	while (g >> v)
	{
		this->volunteers.push_back(v);
	}

	f.close();
	g.close();
}

void Repository::writeToFile()
{
	ofstream f{ this->vfile};

	for (Volunteer v : this->volunteers)
		f << v;

	f.close();
}
