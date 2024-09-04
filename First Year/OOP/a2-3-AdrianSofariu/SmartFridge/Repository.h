#pragma once
#include "DynamicArray.h"
#include "DAIterator.h"

typedef struct {
	DynamicArray* storage;
}Repository;

typedef DAIterator RepoIterator;

/// <summary>
/// Create a new repository object
/// </summary>
/// <param name="arr">Dynamic Array used as storage</param>
/// <returns>A pointer to the created repository</returns>
Repository* createRepository(DynamicArray* arr);

/// <summary>
/// Destroy a repository object
/// </summary>
/// <param name="ctrl">Pointer to the repository object</param>
void destroyRepository(Repository* repo);

/// <summary>
/// Adds a generic element to the repo.
/// </summary>
/// <param name="repo">A pointer to the repository.</param>
/// <param name="p">The product to be added.</param>
void addToRepo(Repository* repo, TElement t);

/// <summary>
/// Removes a given element.
/// </summary>
/// <param name="repo">A pointer to the repository.</param>
/// <param name="pos">The element to be removed</param>
void deleteFromRepo(Repository* repo, TElement t);

/// <summary>
/// Updates the element oldT with newT
/// </summary>
/// <param name="repo">A pointer to the repository.</param>
/// <param name="oldT">A pointer to the element to update</param>
/// <param name="newT">A pointer to the new element</param>
void updateInRepo(Repository* repo, TElement oldT, TElement newT);

/// <summary>
/// Search for an element in the repo
/// </summary>
/// <param name="repo">A pointer to the repository</param>
/// <param name="t">TElement to search for</param>
/// <returns>A pointer to the element or null if it is not in the repo</returns>
TElement* findInRepo(Repository* repo, TElement t);

int getRepoLength(Repository* repo);

RepoIterator createRepoIterator(Repository* repo);

/// <summary>
/// Copy a repository
/// </summary>
/// <param name="repo">Repositroy to be copied</param>
/// <returns>A repository object</returns>
Repository* copy(Repository* repo);

/// <summary>
///Initialize repo with 10 records
///</summary>
/// <param name="repo">A pointer to a repository</param>
void initRepo(Repository* repo);

//tests
void testRepository();