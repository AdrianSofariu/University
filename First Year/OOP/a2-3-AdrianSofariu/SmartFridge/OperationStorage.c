#include "OperationStorage.h"
#include "DynamicArray.h"
#include <stdlib.h>
#include <assert.h>

OperationsArray* createOperationsArray(int capacity, DestroyFunction destroyFct)
{
	OperationsArray* da = malloc(sizeof(OperationsArray));
	// make sure that the space was allocated
	if (da == NULL)
		return NULL;

	da->capacity = capacity;
	da->length = 0;
	da->destroyFct = destroyFct;

	// allocate space for the elements
	da->elems = malloc(capacity * sizeof(Operation));

	// make sure space for the elements was allocated
	if (da->elems == NULL)
		return NULL;

	return da;
}

void destroyOA(OperationsArray* arr)
{
	if (arr == NULL)
		return;


	// free the space allocated for the products
	for (int i = 0; i < arr->length; i++)
	{
		arr->destroyFct(&arr->elems[i].oldP);
		arr->destroyFct(&arr->elems[i].newP);
	}
	free(arr->elems);
	arr->elems = NULL;
	// free the space allocated for the dynamic array
	free(arr);
}

// Resizes the array, allocating more space.
void resizeOA(OperationsArray* arr)
{
	if (arr == NULL)
		return;

	arr->capacity *= 2;
	Operation* aux = realloc(arr->elems, arr->capacity * sizeof(Operation));
	if (aux == NULL)
		return;
	arr->elems = aux;
}


void addOA(OperationsArray* arr, Operation t)
{
	if (arr == NULL)
		return;
	if (arr->elems == NULL)
		return;

	// resize the array, if necessary
	if (arr->length == arr->capacity)
		resizeOA(arr);
	arr->elems[arr->length] = t;
	arr->length++;
}


Operation* getOp(OperationsArray* arr, int pos)
{
	Operation* ele = &arr->elems[pos];
	return ele;
}

int getLengthOA(OperationsArray* arr)
{
	if (arr == NULL)
		return 0;
	return arr->length;
}

int getCapacityOA(OperationsArray* arr)
{
	if (arr == NULL)
		return 0;
	return arr->capacity;
}



