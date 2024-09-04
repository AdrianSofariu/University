#pragma once
#include "Repository.h"

class Service
{
private:
	Repository& repo;

public:
	Service(Repository& repo) : repo{ repo } {};
	std::vector<Medication> get_medications() const;
	std::vector<std::string> get_side_effects(std::string name) const;
};

