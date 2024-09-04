#include "Controller.h"
#include "Date.h"
#include "ProductValidator.h"
#include <stdlib.h>
#include "Repository.h"
#include <string.h>
#include "Operations.h"
#include <crtdbg.h>
#include <assert.h>

Controller* createController(Repository* repo)
{
	Controller* ctrl = (Controller*)malloc(sizeof(Controller));

	//make sure that the space was allocated
	if (ctrl == NULL)
		return NULL;
	//make sure repo exists
	if (repo == NULL)
		return NULL;

	ctrl->repository = repo;
	ctrl->index = -1;
	ctrl->history = createOperationsArray(10, destroyProduct);

	return ctrl;
}

void destroyController(Controller* ctrl)
{
	if (ctrl == NULL)
		return;

	destroyRepository(ctrl->repository);
	destroyOA(ctrl->history);
	ctrl->repository = NULL;
	free(ctrl);
}

int addProduct(Controller* ctrl, char* name, char* category, int quantity, int day, int month, int year)
{
	Date expirationDate = createDate(day, month, year);
	int valid = validCategory(category);

	// check if category is valid
	if (valid == -1)
		return -1;

	Product p = createProduct(name, category, quantity, expirationDate);

	// check if product already exists
	Product* old_prod = findInRepo(ctrl->repository, p);

	// if the product does not exist, add it
	if (old_prod == NULL)
	{
		addToRepo(ctrl->repository, p);
		Operation op = addOperation(ctrl->repository, p, addToRepo, deleteFromRepo);
		addOA(ctrl->history, op);
		ctrl->index = getLength(ctrl->history) - 1;
	}
	else {
		// if the product exists, update the quantity
		p.quantity += getQuantity(old_prod);
		Operation op = updateOperation(ctrl->repository, *old_prod, p, updateInRepo, updateInRepo);
		addOA(ctrl->history, op);
		ctrl->index = getLength(ctrl->history) - 1;
		setQuantity(old_prod, getQuantity(old_prod) + quantity);
		destroyProduct(&p);
	}
	return 0;
}

int removeProduct(Controller* ctrl, char* name, char* category)
{
	Date expirationDate = createDate(0, 0, 0);
	int valid = validCategory(category);

	// check if category is valid
	if (valid == -1)
		return -1;

	Product p = createProduct(name, category, 0, expirationDate);

	// check if product already exists
	Product* old_prod = findInRepo(ctrl->repository, p);

	if (old_prod == NULL)
	{
		destroyProduct(&p);
		return -1;
	}
	else 
	{
		Operation op = deleteOperation(ctrl->repository, *old_prod, addToRepo, deleteFromRepo);
		addOA(ctrl->history, op);
		ctrl->index = getLength(ctrl->history) - 1;
		deleteFromRepo(ctrl->repository, p);
	}
	destroyProduct(&p);
	return 0;
}

int updateProduct(Controller* ctrl, char* name, char* category, int quantity, int day, int month, int year)
{
	Date expirationDate = createDate(day, month, year);
	int valid = validCategory(category);

	// check if category is valid
	if (valid == -1)
		return -1;

	Product p = createProduct(name, category, quantity, expirationDate);

	// check if product already exists
	Product* old_prod = findInRepo(ctrl->repository, p);

	// if the product does not exist, return error code -1
	if (old_prod == NULL)
	{
		destroyProduct(&p);
		return -1;
	}
	else {
		// if the product exists, update it
		Operation op = updateOperation(ctrl->repository, *old_prod, p, updateInRepo);
		addOA(ctrl->history, op);
		ctrl->index = getLength(ctrl->history) - 1;
		updateInRepo(ctrl->repository, *old_prod, p);
	}
	return 0;
}

/// <summary>
/// Sort a list of products using a comparator function
/// </summary>
/// <param name="list">A list of products</param>
/// <param name="length">The lenght of the list</param>
/// <param name="compare">A function that compares two products, which returns 1 if p1 > p2</param>
void sortProducts(Product* list, int length, ComparatorFunction greater)
{
	int i, j;
	Product aux;
	for (i = 0; i < length - 1; i++)
		for (j = i + 1; j < length; j++)
			if (greater(list[i], list[j]) == 1)
			{
				aux = list[i];
				list[i] = list[j];
				list[j] = aux;
			}
}

Product* filterProductsByName(Controller* ctrl, char* name, int* length)
{
	*length = 0;

	RepoIterator it = createRepoIterator(ctrl->repository);
	Product* filtered_list = NULL;
	
	// check if we need to filter or not
	*length = getRepoLength(ctrl->repository);
	if (*length != 0)
	{
		if (strcmp(name, "") == 0)
		{
			// if we received an empty string, return all products
			filtered_list = malloc(sizeof(Product) * (*length));
			int i = 0;
			if (filtered_list == NULL)
				return NULL;
			else {
				while (validIterator(&it) == 0)
				{
					Product p = getCurrent(&it);
					filtered_list[i] = p;
					i++;
					next(&it);
				}
			}
		}
		else
		{
			*length = 0;
			// count how many products contain the given name
			while (validIterator(&it) == 0)
			{
				Product p = getCurrent(&it);
				if (strstr(getName(&p), name) != NULL)
				{
					(*length)++;
				}
				next(&it);
			}

			filtered_list = malloc(sizeof(Product) * (*length));
			if (filtered_list == NULL)
				return NULL;
			else
			{
				reset(&it);

				//store them in a new array
				int i = 0;
				while (validIterator(&it) == 0)
				{
					Product p = getCurrent(&it);
					if (strstr(getName(&p), name) != NULL)
					{
						filtered_list[i] = p;
						i++;
					}
					next(&it);
				}
			}
		}

		//sort the list
		sortProducts(filtered_list, *length, greaterQuantity);
	}
	return filtered_list;
}


Product* filterProductsByCategory(Controller* ctrl, char* category, int* length, int daysUntilExpired)
{

	RepoIterator it = createRepoIterator(ctrl->repository);
	Product* filtered_list = NULL;

	//get current date
	Date today = getCurrentDate();

	*length = getRepoLength(ctrl->repository);
	if(*length == 0)
		return NULL;

	// check if we need to filter or not
	if (strcmp(category, "") == 0)
	{
		// count how many products expire in the following daysUntilExpired days
		*length = 0;
		while (validIterator(&it) == 0)
		{
			Product p = getCurrent(&it);
			int diff = (int)dayDifference(today, getDate(&p));
			if (diff <= daysUntilExpired && diff >= 0)
			{
				(*length)++;
			}
			next(&it);
		}

		reset(&it);
		//store them in a new array
		filtered_list = malloc(sizeof(Product) * (*length));
		int i = 0;
		if (filtered_list == NULL)
			return NULL;
		else {
			while (validIterator(&it) == 0)
			{
				Product p = getCurrent(&it);
				int diff = (int)dayDifference(today, getDate(&p));
				if (diff <= daysUntilExpired && diff >= 0)
				{
					filtered_list[i] = p;
					i++;
				}
				next(&it);
			}
		}
	}
	else
	{
		*length = 0;
		// count how many products contain the given name and expire in the following daysUntilExpired days
		while (validIterator(&it) == 0)
		{
			Product p = getCurrent(&it);
			int diff = (int)dayDifference(today, getDate(&p));
			if (strcmp(getType(&p), category) == 0 && diff <= daysUntilExpired && diff >= 0)
			{
				(*length)++;
			}
			next(&it);
		}

		filtered_list = malloc(sizeof(Product) * (*length));
		if (filtered_list == NULL)
			return NULL;
		else
		{
			reset(&it);

			//store them in a new array
			int i = 0;
			while (validIterator(&it) == 0)
			{
				Product p = getCurrent(&it);
				int diff = (int)dayDifference(today, getDate(&p));
				if (strcmp(getType(&p), category) == 0 && diff <= daysUntilExpired && diff >= 0)
				{
					filtered_list[i] = p;
					i++;
				}
				next(&it);
			}
		}
	}

	//return the list
	return filtered_list;
}

int undo(Controller* ctrl)
{
	if(ctrl->index == -1)
		return -1;
	undoOperation(&ctrl->history->elems[ctrl->index], ctrl->repository);
	ctrl->index--;
	return 0;
}

int redo(Controller* ctrl)
{
	if (ctrl->index == getLength(ctrl->history) - 1)
		return -1;
	redoOperation(&ctrl->history->elems[ctrl->index + 1], ctrl->repository);
	ctrl->index++;
	return 0;
}

void testController()
{
	DynamicArray* arr = createDynamicArray(10, destroyProduct);
	Repository* repo = createRepository(arr);
	Controller* ctrl = createController(repo);

	// test addProduct
	assert(addProduct(ctrl, "apple", "fruit", 10, 1, 1, 2021) == 0);
	assert(addProduct(ctrl, "banana", "fruit", 10, 1, 1, 2021) == 0);
	assert(addProduct(ctrl, "milk", "dairy", 10, 1, 1, 2021) == 0);


	// test removeProduct
	assert(removeProduct(ctrl, "apple", "fruit") == 0);
	assert(removeProduct(ctrl, "apple", "fruit") == -1);

	//test update
	assert(updateProduct(ctrl, "banana", "fruit", 20, 1, 1, 2021) == 0);

	//test filter by name
	int length = 0;
	char* name = "banana";
	Product* filtered_list = filterProductsByName(ctrl, name, &length);
	assert(length == 1);
	assert(strcmp(getName(&filtered_list[0]), "banana") == 0);
	free(filtered_list);

	//test filter by empty name
	filtered_list = filterProductsByName(ctrl, "", &length);
	assert(length == 2);
	free(filtered_list);

	//test filter by category
	addProduct(ctrl, "apple", "fruit", 10, 25, 4, 2024);
	filtered_list = filterProductsByCategory(ctrl, "fruit", &length, 30);
	assert(length == 1);
	free(filtered_list);

	//destroy controller
	destroyController(ctrl);
}

void testUndoRedo()
{
	DynamicArray* arr = createDynamicArray(10, destroyProduct);
	Repository* repo = createRepository(arr);
	Controller* ctrl = createController(repo);

	//test undo & redo
	addProduct(ctrl, "milk", "dairy", 10, 25, 3, 2024);
	assert(undo(ctrl) == 0);
	//check if the product was removed
	assert(getRepoLength(ctrl->repository) == 0);
	assert(redo(ctrl) == 0);
	//check if the product was added
	assert(getRepoLength(ctrl->repository) == 1);

	//more undo redo tests
	addProduct(ctrl, "butter", "dairy", 20, 25, 3, 2024);
	addProduct(ctrl, "kiwi", "fruit", 20, 25, 3, 2024);
	removeProduct(ctrl, "kiwi", "fruit");
	assert(undo(ctrl) == 0);
	assert(getRepoLength(ctrl->repository) == 3);
	assert(redo(ctrl) == 0);
	assert(getRepoLength(ctrl->repository) == 2);
	//out of redos
	assert(redo(ctrl) == -1);

	//we can undo 4 times
	assert(undo(ctrl) == 0);
	assert(undo(ctrl) == 0);
	assert(undo(ctrl) == 0);
	assert(undo(ctrl) == 0);
	//out of undos
	assert(undo(ctrl) == -1);

	//destroy controller
	destroyController(ctrl);
}