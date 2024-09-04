#pragma once
#include <cassert>

template<typename TElem>

class DynamicArray
{
private:
	TElem* elems;
	int size;
	int capacity;

public:

	//constructor
	DynamicArray(int capacity = 10);

	//copy constructor
	DynamicArray(const DynamicArray& v);
	
	//destructor
	~DynamicArray();

	//assignment operator
	DynamicArray operator=(const DynamicArray& v);

	//adds an element to the dynamic array
	void add(const TElem& e);

	//removes an element from the dynamic array
	void remove(const TElem& e);

	//returns the size of the dynamic array
	int getSize() const;

	/*
	Overloading the subscript operator
	Input: pos - a valid position within the array.
	Output: a reference to the element o position pos.
	*/
	TElem& operator[](int pos);

private:
	//resizes the array, multiplying its capacity by a given factor (real number)
	void resize(int factor = 2);
};


//implementation
template<typename TElem>
inline DynamicArray<TElem>::DynamicArray(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elems = new TElem[capacity];
}

template<typename TElem>
inline DynamicArray<TElem>::DynamicArray(const DynamicArray& v)
{
	this->size = v.size;
	this->capacity = v.capacity;
	this->elems = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];
}

template<typename TElem>
inline DynamicArray<TElem>::~DynamicArray()
{
	delete[] this->elems;
}

template<typename TElem>
inline DynamicArray<TElem> DynamicArray<TElem>::operator=(const DynamicArray<TElem>& v)
{
	if(this == &v)
		return *this;
	this->size = v.size;
	this->capacity = v.capacity;
	delete[] this->elems;
	this->elems = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elems[i] = v.elems[i];
	return *this;
}

template<typename TElem>
inline void DynamicArray<TElem>::add(const TElem& e)
{
	if (this->size == this->capacity)
		this->resize();
	this->elems[this->size] = e;
	this->size++;
}

template<typename TElem>
inline void DynamicArray<TElem>::remove(const TElem& e)
{
	int i = 0;
	while (i < this->size && this->elems[i] != e)
		i++;
	if (i < this->size)
	{
		this->elems[i] = this->elems[this->size - 1];
		this->size--;
	}
}

template<typename TElem>
inline int DynamicArray<TElem>::getSize() const
{
	return this->size;
}

template<typename TElem>
inline TElem& DynamicArray<TElem>::operator[](int pos)
{
	return this->elems[pos];
}

template<typename TElem>
inline void DynamicArray<TElem>::resize(int factor)
{
	this->capacity *= factor;
	TElem* els = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++)
		els[i] = this->elems[i];
	delete[] this->elems;
	this->elems = els;
}
