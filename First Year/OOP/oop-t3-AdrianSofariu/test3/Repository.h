#pragma once
#include <vector>
#include "Medication.h"

class Repository
{
private:
	std::vector<Medication> medications;
	std::string file;

public:
	Repository(std::string file_name);
	std::vector<Medication> get_medications() const;
	std::vector<std::string> get_side_effects(std::string name) const;

private:
	void read_from_file();
};

