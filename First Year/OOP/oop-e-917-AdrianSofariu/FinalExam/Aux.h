#pragma once
#include <string>

class Aux
{
private:
	std::string dep;
	int count;

public:
	Aux(std::string d, int c) : dep{ d }, count{ c } {};
	int getCount() { return this->count; };
	std::string getDep() { return this->dep; };
};

