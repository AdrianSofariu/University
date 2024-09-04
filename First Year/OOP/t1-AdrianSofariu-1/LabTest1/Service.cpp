#include "Service.h"
#include <algorithm>
#include <assert.h>

Service::Service(Repository repo)
{
	this->repo = repo;
}

void Service::addRecord(std::string organism, std::string name, std::string sequence)
{
	Protein p{ organism, name, sequence };
	this->repo.add(p);
}

std::vector<Protein> Service::getProteins()
{
	return this->repo.getAll();
}

void Service::initRepo()
{
	this->repo.add(Protein{ "Human", "Myosin-2", "MSSDSELAVFGEAA" });
	this->repo.add(Protein{ "Human", "Keratin", "TWDBAOWBDAIWVDIUPAWUIPDBA" });
	this->repo.add(Protein{ "Mouse", "Keratin", "MLWWWEEAWWJDBDAIWUDBAODJ" });
	this->repo.add(Protein{ "E_Coli", "tufA", "VTLHWABDIAWBDBANWDAIWN" });
	this->repo.add(Protein{ "E_Coli", "cspE", "MSKIKIGAWDBAIPBSDNPAUWBDAS " });
}

std::vector<Protein> Service::getProteinsByName(std::string given_name)
{
	std::vector<Protein> allProteins = this->getProteins();
	std::vector<Protein> matchingProteins;

	std::vector<Protein>::iterator it;
	for(it = allProteins.begin(); it != allProteins.end(); it++)
		if ((*it).getName() == given_name)
		{
			Protein p = *it;
			matchingProteins.push_back(p);
		}

	std::sort(matchingProteins.begin(), matchingProteins.end(), [](Protein a, Protein b) {return a.getOrganism() <= b.getOrganism(); });
	return matchingProteins;
}

void Service::testGetByString()
{
	Repository repo;
	Service serv{ repo };

	serv.initRepo();

	serv.addRecord("AAAAA", "Keratin", "DAWDAWDAW");
	
	std::vector<Protein> test = serv.getProteinsByName("Keratin");
	assert(test.size() == 3);
	assert(test[0].getOrganism() == "AAAAA");
	assert(test[1].getOrganism() == "Human");
	assert(test[2].getOrganism() == "Mouse");

	assert(test[0].getName() == "Keratin");
	assert(test[1].getName() == "Keratin");
	assert(test[2].getName() == "Keratin");
}

