#include "DynamicArray.h"
#include <stdlib.h>
#include <assert.h>

DynamicArray* createDynamicArray(int capacity, DestroyFunction destroyFct)
{
	DynamicArray* da = malloc(sizeof(DynamicArray));
	// make sure that the space was allocated
	if (da == NULL)
		return NULL;

	da->capacity = capacity;
	da->length = 0;
	da->destroyFct = destroyFct;

	// allocate space for the elements
	da->elems = malloc(capacity * sizeof(TElement));

	// make sure space for the elements was allocated
	if (da->elems == NULL)
		return NULL;

	return da;
}

void destroy(DynamicArray* arr)
{
	if (arr == NULL)
		return;


	// free the space allocated for the products
	for (int i = 0; i < arr->length; i++)
		arr->destroyFct(&arr->elems[i]);
	free(arr->elems);
	arr->elems = NULL;
	// free the space allocated for the dynamic array
	free(arr);
}

// Resizes the array, allocating more space.
void resize(DynamicArray* arr)
{
	if (arr == NULL)
		return;

	arr->capacity *= 2;
	TElement* aux = realloc(arr->elems, arr->capacity * sizeof(TElement));
	if (aux == NULL)
		return;
	arr->elems = aux;
}

// Resizes the array, allocating less space.
void shrink(DynamicArray* arr)
{
	if (arr == NULL)
		return;

	arr->capacity /= 2;
	TElement* aux = realloc(arr->elems, arr->capacity * sizeof(TElement));
	if (aux == NULL)
		return;
	arr->elems = aux;
}

void add(DynamicArray* arr, TElement t)
{
	if (arr == NULL)
		return;
	if (arr->elems == NULL)
		return;

	// resize the array, if necessary
	if (arr->length == arr->capacity)
		resize(arr);
	arr->elems[arr->length] = t;
	arr->length++;
}

void deleteP(DynamicArray* arr, TElement t)
{
	if (arr == NULL)
		return;
	if (arr->elems == NULL)
		return;

	int i = 0;
	while (i < arr->length && equals(arr->elems[i], t) == 1)
		i++;
	// if product was not found, return
	if (i == arr->length)
		return;

	//firstly deallocate its space
	arr->destroyFct(&arr->elems[i]);

	// delete the product from position i by shifting
	for (int j = i; j < arr->length - 1; j++)
		arr->elems[j] = arr->elems[j + 1];
	arr->length--;

	//resize if the length is less than a quarter of the capacity
	if (arr->length > 0 && arr->length <= arr->capacity / 4)
	{
		shrink(arr);
	}
}

void update(DynamicArray* arr, TElement oldT, TElement newT)
{
	if (arr == NULL)
		return;
	
	int pos = find(arr, oldT);
	TElement* old = findElement(arr, oldT);
	if (find != -1)
	{
		if (old->name != oldT.name)
			arr->destroyFct(old);
		arr->destroyFct(&oldT);
		arr->elems[pos] = newT;
	}
}

int find(DynamicArray* arr, TElement t)
{
	if (arr == NULL)
		return -1;
	if (arr->elems == NULL)
		return -1;

	// search for the product in the array and return position if found
	for (int i = 0; i < arr->length; i++)
		if (equals(arr->elems[i], t) == 0)
			return i;

	// if the product was not found, return -1
	return -1;
}

TElement* findElement(DynamicArray* arr, TElement t)
{

	if (arr == NULL)
		return -1;
	if (arr->elems == NULL)
		return -1;

	// search for the product in the array and return pointer if found
	for (int i = 0; i < arr->length; i++)
		if (equals(arr->elems[i], t) == 0)
			return &arr->elems[i];

	// if the product was not found, return null
	return NULL;

}

TElement* get(DynamicArray* arr, int pos)
{
	TElement* ele = &arr->elems[pos];
	return ele;
}

int getLength(DynamicArray* arr)
{
	if (arr == NULL)
		return 0;
	return arr->length;
}

int getCapacity(DynamicArray* arr)
{
	if (arr == NULL)
		return 0;
	return arr->capacity;
}

DAIterator createDAIterator(DynamicArray* arr)
{
	DAIterator it;
	it.products = arr->elems;
	it.current = 0;
	it.length = arr->length;
	return it;
}

DynamicArray* copyDynamicArray(DynamicArray* arr)
{
	DynamicArray* da = createDynamicArray(arr->capacity, arr->destroyFct);
	for (int i = 0; i < arr->length; i++)
	{
		TElement new_e = copyProduct(arr->elems[i]);
		add(da, new_e);
	}
	return da;
}


void testsDynamicArray()
{
	DynamicArray* da = createDynamicArray(2, destroyProduct);
	if (da == NULL)
		assert(0);

	assert(getCapacity(da) == 2);
	assert(getLength(da) == 0);

	Product p1 = createProduct("Milk", "dairy", 10, createDate(10, 10, 2020));
	add(da, p1);
	assert(getLength(da) == 1);

	Product p2 = createProduct("Bread", "bakery", 20, createDate(10, 10, 2020));
	add(da, p2);
	assert(getLength(da) == 2);

	// capacity must double
	Product p3 = createProduct("Butter", "dairy", 5, createDate(10,10,2020));
	add(da, p3);
	assert(getLength(da) == 3);
	assert(getCapacity(da) == 4);

	//search for a product
	assert(find(da, p1) == 0);
	assert(find(da, p2) == 1);
	assert(find(da, p3) == 2);
	Product p5 = createProduct("Juice", "fruit", 10, createDate(10,10,2020));
	assert(find(da, p5) == -1);
	destroyProduct(&p5);

	//test the other find method
	assert(equals(*findElement(da, p1), p1) == 0);

	//test iterator
	DAIterator it = createDAIterator(da);
	assert(validIterator(&it) == 0);
	assert(equals(getCurrent(&it), p1) == 0);
	next(&it);
	next(&it);
	next(&it);
	assert(validIterator(&it) == -1);

	//test copying the da
	DynamicArray* da2 = copyDynamicArray(da);
	assert(getLength(da2) == 3);
	destroy(da2);

	//capacity must halve
	deleteP(da, p3);
	deleteP(da, p2);
	assert(getLength(da) == 1);
	assert(getCapacity(da) == 2);

	Product p4 = createProduct("Butter", "dairy", 20, createDate(10,10,2020));
	update(da, p1, p4);
	assert(da->elems[0].quantity == 20);

	destroy(da);
}
