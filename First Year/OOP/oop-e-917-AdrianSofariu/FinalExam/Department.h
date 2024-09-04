#pragma once
#include <string>
#include <iostream>

class Department
{
private:
	std::string name, desc;

public:
	Department() {};
	Department(std::string n, std::string d) : name{ n }, desc{ d } {};
	std::string getName() { return this->name; };
	std::string getDec() { return this->desc; };

	friend std::istream& operator>>(std::istream& is, Department& dept);
	friend std::ostream& operator<<(std::ostream& os, Department dept);

};

