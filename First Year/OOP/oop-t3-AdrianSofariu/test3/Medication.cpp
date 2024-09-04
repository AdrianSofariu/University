#include "Medication.h"
#include "Utils.h"

using namespace std;

Medication::Medication(std::string name, std::string category, std::vector<std::string> side_effects) : name{ name }, category{ category }, side_effects{ side_effects }
{
}

std::string Medication::get_name() const
{
	return this->name;
}

std::string Medication::get_category() const
{
	return this->category;
}

std::vector<std::string> Medication::get_side_effects() const
{
	return this->side_effects;
}

std::istream& operator>>(std::istream& is, Medication& m)
{
	string line;
	getline(is, line);
	vector<string> tokens = tokenize(line, '|');
	if (tokens.size() != 3)
		return is;
	m.category = tokens[0];
	m.name = tokens[1];
	m.side_effects = tokenize(tokens[2], ',');
	return is;
}
