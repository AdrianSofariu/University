#include "Repository.h"
#include <assert.h>

void Repository::add(Protein p)
{
	std::vector<Protein>::iterator it;
	for (it = this->proteins.begin(); it != this->proteins.end(); it++)
		if (*it == p)
			throw std::exception("Protein already exists");
	this->proteins.push_back(p);
}

std::vector<Protein> Repository::getAll()
{
	return this->proteins;
}

//test add
void Repository::testAdd()
{
	Repository repo;
	Protein a{ "Human", "Keratin", "awdaiwgdiyawgdoaw" };
	Protein b{ "Mouse", "Myosin-2", "dwadvoawgdiuawhduaiw" };
	Protein x{ "Human", "Keratin", "xxxxxxxxxxxxxxxx" };

	repo.add(a);
	assert(repo.proteins.size() == 1);

	repo.add(b);
	assert(repo.proteins.size() == 2);

	try
	{
		repo.add(x);
		assert(false);
	}
	catch (std::exception& e)
	{
		assert(std::string(e.what()) == "Protein already exists");
	}
}
