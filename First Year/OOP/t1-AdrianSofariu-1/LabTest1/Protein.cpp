#include "Protein.h"
#include <sstream>

Protein::Protein(std::string organism, std::string name, std::string sequence)
{
	this->organism = organism;
	this->name = name;
	this->sequence = sequence;
}

std::string Protein::getOrganism()
{
	return this->organism;
}

std::string Protein::getName()
{
	return this->name;
}

std::string Protein::getSequence()
{
	return this->sequence;
}

bool Protein::operator==(Protein b)
{
	if (this->name == b.name && this->organism == b.organism)
		return true;
	return false;
}

std::string Protein::toString()
{
	std::stringstream s;
	s << this->organism << " | " << this->name << " | " << this->sequence << std::endl;
	return s.str();
}

