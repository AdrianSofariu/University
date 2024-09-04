#pragma once
#include "Product.h"
#include "Operations.h"



typedef struct
{
	Operation* elems;
	int length;			// actual length of the array
	int capacity;
	DestroyFunction destroyFct;
} OperationsArray;

/// <summary>
/// Creates a dynamic array of generic elements, with a given capacity.
/// </summary>
/// <param name="capacity">Integer, maximum capacity for the dynamic array.</param>
/// <param name="destroyFct">DestroyFunction, a pointer to a function that deallocates memory used by the Operation
/// <returns>A pointer the the created dynamic array.</returns>
OperationsArray* createOperationsArray(int capacity, DestroyFunction destroyFct);

/// <summary>
/// Destroys the dynamic array.
/// </summary>
/// <param name="arr">The dynamic array to be destoyed.</param>
void destroyOA(OperationsArray* arr);

/// <summary>
/// Adds a generic element to the dynamic array.
/// </summary>
/// <param name="arr">The dynamic array.</param>
/// <param name="p">The operation to be added.</param>
void addOA(OperationsArray* arr, Operation t);


int getLengthOA(OperationsArray* arr);
int getCapacityOA(OperationsArray* arr);



