#pragma once
#include "Volunteer.h"
#include "Department.h"
#include "Subject.h"
#include <vector>

class Repository : public Subject
{
private:
	std::vector<Volunteer> volunteers;
	std::vector<Department> departments;
	std::string vfile, dfile;

public:

	Repository(std::string f, std::string d) : vfile{ f }, dfile{ d } { readFromFile(); };
	~Repository() { writeToFile(); };
	std::vector<Volunteer> getVolunteers() { return this->volunteers; };
	std::vector<Department> getDepartments() { return this->departments; };
	void add(Volunteer v);
	void assign(std::string name, std::string dep);

private:
	void readFromFile();
	void writeToFile();
};

