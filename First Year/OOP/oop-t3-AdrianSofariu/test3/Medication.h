#pragma once
#include <string>
#include <vector>
#include <iostream>

class Medication
{
private:
	std::string name;
	std::vector<std::string> side_effects;
	std::string category;

public:
	Medication() {};
	Medication(std::string name, std::string category, std::vector<std::string> side_effects);

	std::string get_name() const;
	std::string get_category() const;
	std::vector<std::string> get_side_effects() const;

	friend std::istream& operator>>(std::istream& is, Medication& m);

};

