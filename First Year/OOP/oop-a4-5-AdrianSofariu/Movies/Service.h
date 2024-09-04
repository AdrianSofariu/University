#pragma once
#include "Repository.h"
#include "Movie.h"

class Service
{
private:
	Repository& repo;

public:

	//constructor
	Service(Repository& repo) : repo{ repo } {};

	//desctructor
	~Service() {};

	//adds a new element to the repository
	//input: movie - Movie
	//output: the element is added to the repository
	//throws: exception if the element already exists
	void addToRepo(const Movie& movie);

	//removes an element from the repository
	//input: title - string
	//output: the element is removed from the repository
	//throws: exception if the element does not exist
	void removeFromRepo(const std::string& title);

	//updates an element from the repository
	//input: newMovie - Movie, title - string
	//output: the element is updated in the repository
	//throws: exception if the element does not exist
	void updateInRepo(const Movie& newMovie, const std::string& title);

	//searches for an element in the repository
	//input: title - string
	//output: the element is returned, or NULL if it does not exist
	Movie* findInRepo(const std::string& title);

	//check repo length
	//output: the length of the repository
	int getRepoLength() const;

	//get all elements from the repository as strings
	//output: a vector of strings
	DynamicArray<std::string> getRepo();

	//init repo with some data
	void initRepo();
};

void testService();

