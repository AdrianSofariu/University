#pragma once
#include "Repository.h"
#include <assert.h>

class Service
{
private:
	Repository repo;

public:

	Service() {};
	Service(Repository repo);

	/// <summary>
	/// Creates a new protein and adds it to the repository by calling the add function from repo
	/// </summary>
	/// <param name="organism">string representing the organism parameter</param>
	/// <param name="name">string representing the name parameter</param>
	/// <param name="sequence">string representing the sequence parameter</param>
	/// If there already is a protein with the same name and organism in the repo, the add function will throw an exception
	/// that is not caught by this function
	void addRecord(std::string organism, std::string name, std::string sequence);

	std::vector<Protein> getProteins();
	void initRepo();

	/// <summary>
	/// Returns a list of proteins with a given name sorted by organism
	/// </summary>
	/// <param name="given_name">std::string representing the name</param>
	/// <returns>std::vector<Protein> containing the Proteins matching</returns>
	std::vector<Protein> getProteinsByName(std::string given_name);

	static void testGetByString();
};

