#pragma once
#include "Repository.h"
#include "OperationStorage.h"

typedef int (*ComparatorFunction)(Product, Product);

typedef struct {
	Repository* repository;
	OperationsArray* history;
	int index;
}Controller;

/// <summary>
/// Create a new controller object
/// </summary>
/// <param name="repo">A pointer to the repository</param>
/// <returns>A pointer to the created controller</returns>
Controller* createController(Repository* repo);

/// <summary>
/// Destroy a controller object
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
void destroyController(Controller* ctrl);

/// <summary>
/// Add a product to the repository
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
/// <param name="name">Name of the product</param>
/// <param name="category">Category of the product</param>
/// <param name="quantity">Quantity of the product</param>
/// <param name="day">Expiration day</param>
/// <param name="month">Expiration month</param>
/// <param name="year">Expiration year</param>
/// <returns>0 if the product was added successfully, -1 if the category is invalid</returns>
int addProduct(Controller* ctrl, char* name, char* category, int quantity, int day, int month, int year);

/// <summary>
/// Remove a product from the repository
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
/// <param name="name">Name of the product</param>
/// <param name="category">Category of the product</param>
/// <returns>0 if the removal was successfull, -1 otherwise</returns>
int removeProduct(Controller* ctrl, char* name, char* category);

/// <summary>
/// Update a product from the repository
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
/// <param name="name">Name of the product</param>
/// <param name="category">Category of the product</param>
/// <param name="quantity">Quantity of the product</param>
/// <param name="day">Expiration day</param>
/// <param name="month">Expiration month</param>
/// <param name="year">Expiration year</param>
/// <returns>0 if the product was updated successfully, -1 if the category is invalid or the product does not exist</returns>
int updateProduct(Controller* ctrl, char* name, char* category, int quantity, int day, int month, int year);

/// <summary>
/// Filter products by name
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
/// <param name="name">Filter</param>
/// <param name="length">will contain the lenght of the found list of products</param>
/// <returns>The list of products sorted ascending using a comparator function</returns>
Product* filterProductsByName(Controller* ctrl, char* name, int* length);

/// <summary>
/// Filter products by category and expiration date
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
/// <param name="category">Filter for category</param>
/// <param name="length">int pointer, will contain the length of the found list of products</param>
/// <param name="daysUntilExpired">(int)max days until expiration</param>
/// <returns>The list of products with a corresponding category that expire in the following x days</returns>
Product* filterProductsByCategory(Controller* ctrl, char* category, int* length, int daysUntilExpired);

/// <summary>
/// Undo the last operation that modified the repo
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
/// <returns>0 if operation was successful</returns>
int undo(Controller* ctrl);

/// <summary>
/// Redo the last operation that was undone
/// </summary>
/// <param name="ctrl">Pointer to the controller object</param>
/// <returns>0 if operation was successful</returns>
int redo(Controller* ctrl);

//tests
void testController();
void testUndoRedo();