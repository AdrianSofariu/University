#include "Repository.h"
#include <fstream>
#include <exception>

using namespace std;


Repository::Repository(std::string file_name) : file{file_name}
{
	this->read_from_file();
}

std::vector<Medication> Repository::get_medications() const
{
	return this->medications;
}

std::vector<std::string> Repository::get_side_effects(std::string name) const
{
	for(auto m : this->medications)
		if (m.get_name() == name)
			return m.get_side_effects();
	throw exception("Medication not found");
}

void Repository::read_from_file()
{
	ifstream f{ this->file };
	if (!f.is_open())
		return;
	Medication m;
	while (f >> m)
		this->medications.push_back(m);
	f.close();
}
