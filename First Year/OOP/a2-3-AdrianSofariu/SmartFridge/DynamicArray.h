#pragma once
#include "Product.h"
#include "DAIterator.h"

typedef Product TElement;

typedef void (*DestroyFunction)(TElement*);

typedef struct
{
	TElement* elems;
	int length;			// actual length of the array
	int capacity;
	DestroyFunction destroyFct;
} DynamicArray;

/// <summary>
/// Creates a dynamic array of generic elements, with a given capacity.
/// </summary>
/// <param name="capacity">Integer, maximum capacity for the dynamic array.</param>
/// <param name="destroyFct">DestroyFunction, a pointer to a function that deallocates memory used by the TElement
/// <returns>A pointer the the created dynamic array.</returns>
DynamicArray* createDynamicArray(int capacity, DestroyFunction destroyFct);

/// <summary>
/// Destroys the dynamic array.
/// </summary>
/// <param name="arr">The dynamic array to be destoyed.</param>
void destroy(DynamicArray* arr);

/// <summary>
/// Adds a generic element to the dynamic array.
/// </summary>
/// <param name="arr">The dynamic array.</param>
/// <param name="p">The product to be added.</param>
void add(DynamicArray* arr, TElement t);

/// <summary>
/// Removes a given element.
/// </summary>
/// <param name="arr">The dynamic array.</param>
/// <param name="pos">The element to be removed</param>
void deleteP(DynamicArray* arr, TElement t);

/// <summary>
/// Updates the element oldT with newT
/// </summary>
/// <param name="arr">The dynamic array.</param>
/// <param name="oldT">A pointer to the element to update</param>
/// <param name="newT">A pointer to the new element</param>
void update(DynamicArray* arr, TElement oldT, TElement newT);

/// <summary>
/// Searches for a given element and returns its position
/// </summary>
/// <param name="arr">The dynamic array</param>
/// <param name="t">The element to search</param>
/// <returns>int position of the element or -1 if not found</returns>
int find(DynamicArray* arr, TElement t);

/// <summary> 
/// Searches for a given element and returns a pointer to it
/// </summary>
/// <param name="arr">The dynamic array</param>
/// <param name="t">The element to search</param>
/// <returns>A pointer to the element or null if not found</returns>
TElement* findElement(DynamicArray* arr, TElement t);

/// <summary>
/// Get element from a given position if it is valid
/// </summary>
/// <param name="arr">The dynamic array</param>
/// <param name="pos">position</param>
/// <returns>A pointer to the element from position pos or null if position is invalid</returns>
TElement* get(DynamicArray* arr, int pos);

int getLength(DynamicArray* arr);
int getCapacity(DynamicArray* arr);

DAIterator createDAIterator(DynamicArray* arr);

DynamicArray* copyDynamicArray(DynamicArray* arr);

// Tests
void testsDynamicArray();

