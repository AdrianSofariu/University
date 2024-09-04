#include "Repository.h"
#include <stdlib.h>
#include <assert.h>

Repository* createRepository(DynamicArray* arr)
{
	Repository* repository = (Repository*)malloc(sizeof(Repository));

	//make sure that the space was allocated
	if (repository == NULL)
		return NULL;
	//make sure repo exists
	if (arr == NULL)
		return NULL;

	repository->storage = arr;
	return repository;
}

void destroyRepository(Repository* repo)
{
	if (repo == NULL)
		return;

	destroy(repo->storage);
	repo->storage = NULL;

	//free the space allocated for the repository
	free(repo);
}

void addToRepo(Repository* repo, TElement t)
{
	if (repo == NULL)
		return;
	if (repo->storage == NULL)
		return;
	add(repo->storage, t);
}

void updateInRepo(Repository* repo, TElement oldT, TElement newT)
{
	if (repo == NULL)
		return;
	if (repo->storage == NULL)
		return;
	update(repo->storage, oldT, newT);
}


void deleteFromRepo(Repository* repo, TElement t)
{
	if (repo == NULL)
		return;
	if (repo->storage == NULL)
		return;
	deleteP(repo->storage, t);
}

TElement* findInRepo(Repository* repo, TElement t)
{
	if(repo == NULL)
		return NULL;
	if (repo->storage == NULL)
		return NULL;
	return findElement(repo->storage, t);
}

int getRepoLength(Repository* repo)
{
	if (repo == NULL)
		return -1;
	if (repo->storage == NULL)
		return -1;
	return getLength(repo->storage);
}

//initialize the repository with some products
void initRepo(Repository* repo)
{
	if (repo == NULL)
		return;
	if (repo->storage == NULL)
		return;
	
	Product p1 = createProduct("Milk", "dairy", 10, createDate(1, 1, 2024));
	Product p2 = createProduct("Chocolate", "sweets", 20, createDate(1, 2, 2024));
	Product p3 = createProduct("Chicken", "meat", 5, createDate(20, 3, 2024));
	Product p4 = createProduct("Apple", "fruit", 15, createDate(25, 3, 2024));
	Product p5 = createProduct("Pear", "fruit", 10, createDate(1, 5, 2024));
	Product p6 = createProduct("Butter", "dairy", 5, createDate(1, 6, 2024));
	Product p7 = createProduct("Candy", "sweets", 20, createDate(1, 7, 2024));
	Product p8 = createProduct("Pork", "meat", 5, createDate(1, 8, 2024));
	Product p9 = createProduct("Banana", "fruit", 15, createDate(1, 9, 2024));
	Product p10 = createProduct("Cake", "bakery", 10, createDate(1, 10, 2024));

	addToRepo(repo, p1);
	addToRepo(repo, p2);
	addToRepo(repo, p3);
	addToRepo(repo, p4);
	addToRepo(repo, p5);
	addToRepo(repo, p6);
	addToRepo(repo, p7);
	addToRepo(repo, p8);
	addToRepo(repo, p9);
	addToRepo(repo, p10);
}


RepoIterator createRepoIterator(Repository* repo)
{
	return	createDAIterator(repo->storage);
}

Repository* copy(Repository* repo)
{
	DynamicArray* copied_array = copyDynamicArray(repo->storage);
	Repository* copied_repo = createRepository(copied_array);
	return copied_repo;
}

void testRepository()
{
	Repository* repo = createRepository(createDynamicArray(10, destroyProduct));
	if (repo == NULL)
		assert(0);

	assert(getRepoLength(repo) == 0);

	Product p1 = createProduct("Milk", "dairy", 10, createDate(10, 10, 2020));
	addToRepo(repo, p1);
	assert(getRepoLength(repo) == 1);

	Product p2 = createProduct("Bread", "bakery", 20, createDate(10, 10, 2020));
	addToRepo(repo, p2);
	assert(getRepoLength(repo) == 2);

	//search for a product
	assert(findInRepo(repo, p1) != NULL);
	assert(findInRepo(repo, p2) != NULL);
	Product p3 = createProduct("Butter", "dairy", 5, createDate(10, 10, 2020));
	assert(findInRepo(repo, p3) == NULL);
	destroyProduct(&p3);

	//update a product
	Product p4 = createProduct("Milk", "dairy", 20, createDate(10, 10, 2020));
	updateInRepo(repo, p1, p4);
	assert(findInRepo(repo, p1) == NULL);
	assert(findInRepo(repo, p4) != NULL);

	//copy the repository
	Repository* copied_repo = copy(repo);
	assert(getRepoLength(copied_repo) == 2);
	destroyRepository(copied_repo);

	//test the iterator
	RepoIterator it = createRepoIterator(repo);
	assert(validIterator(&it) == 0);
	assert(equals(getCurrent(&it), p4) == 0);
	next(&it);
	next(&it);
	assert(validIterator(&it) == -1);

	//delete a product
	deleteFromRepo(repo, p2);
	assert(findInRepo(repo, p2) == NULL);

	//destroy the repository
	destroyRepository(repo);
}


