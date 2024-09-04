#pragma once
#include "Repository.h"

class Service
{
private:
	Repository& repo;

public:
	Service(Repository& r) : repo{ r } {};
	std::vector<Department> getDepartments();
	std::vector<Volunteer> getVolunteers();
	std::vector<Volunteer> getByDepartment(std::string dept);
	std::vector<Volunteer> getUnassigned();
	void add(std::string name, std::string email, std::vector<std::string> interests);
	std::vector<Volunteer> mostSuited(Department dept);
	void assign(std::string name, std::string dep);
};

