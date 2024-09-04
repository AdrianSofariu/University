#pragma once
#include <string>

class Protein
{
private:
	std::string organism;
	std::string name;
	std::string sequence;

public:
	Protein(std::string organism, std::string name, std::string sequence);
	std::string getOrganism();
	std::string getName();
	std::string getSequence();
	bool operator==(Protein b);
	std::string toString();

};

