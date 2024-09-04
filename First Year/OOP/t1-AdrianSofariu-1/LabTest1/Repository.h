#pragma once
#include <vector>
#include "Protein.h"

class Repository
{
private:
	std::vector<Protein> proteins;

public:

	/// <summary>
	/// This function adds a protein to the repository
	/// </summary>
	/// <param name="p">Protein object</param>
	/// Throws exception if there already is a protein with the same name and organism in the repo
	void add(Protein p);


	std::vector<Protein> getAll();

	static void testAdd();
};

