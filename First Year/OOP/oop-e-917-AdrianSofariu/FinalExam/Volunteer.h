#pragma once
#include <string>
#include <vector>
#include <iostream>
#include "Department.h"

class Volunteer
{
private:
	std::string name, email;
	std::vector<std::string> interests;
	std::string dept;

public:
	Volunteer() {};
	Volunteer(std::string n, std::string e, std::vector<std::string> i, std::string d) : name{ n }, email{ e }, interests{ i }, dept{ d } {};
	std::string getDep() { return this->dept; };
	std::string getName() { return this->name; };
	std::string getEmail() { return this->email; };
	double getMatching(Department d);
	void setDep(std::string dep) { this->dept = dep; };

	bool operator==(const Volunteer& other);

	friend std::istream& operator>>(std::istream& is, Volunteer& vol);
	friend std::ostream& operator<<(std::ostream& os, Volunteer vol);
};

