#include "Map.h"
#include "MapIterator.h"

Map::Map() {
	this->m = 16;
	this->nrElem = 0;
	this->table = new Node*[this->m];
	for (int i = 0; i < this->m; i++)
		this->table[i] = NULL;
}
//BC=WC=TC=Theta(m)

Map::~Map() {
	for (int i = 0; i < this->m; i++) {
		Node* current = this->table[i];
		while (current != NULL) {
			this->table[i] = this->table[i]->next;
			delete current;
			current = this->table[i];
		}
	}
	delete[] this->table;
}
//BC=Theta(m), if we have an empty map or only one element per SLL
//WC=Theta(nrElems), because we have to delete all the nodes in the SLLs
//TC=O(nrElems)

TValue Map::add(TKey c, TValue v){
	int position = this->hash(c, this->m);
	Node* current = this->table[position];

	//check if the key already exists in the map
	while (current != NULL and current->elem.first != c)
		current = current->next;
	//replace the value associated with the key
	if (current != NULL) {
		TValue oldValue = current->elem.second;
		current->elem.second = v;
		return oldValue;
	}
	//add a new pair else
	else {
		Node* newNode = new Node;
		newNode->elem.first = c;
		newNode->elem.second = v;

		//add the new node at the beginning of the SLL
		newNode->next = this->table[position];
		this->table[position] = newNode;

		//increase the number of elements in the map
		this->nrElem++;

		//check if the load factor is exceeded and resize the table
		if ((this->nrElem * 1.0) / (this->m * 1.0) >= 0.7)
			this->resize();

		return NULL_TVALUE;
	}
}
//BC=Theta(1), if the key exists and is on the first position in the table and SLL
//WC=Theta(nrElems+m), if we have to rehash all the elements or all elements have the same hash value and the searched one is the last
//TC=O(nrElems+m)
//AC=Theta(1) amortized

TValue Map::search(TKey c) const{
	int position = this->hash(c, this->m);
	Node* current = this->table[position];

	//search for the key
	while (current != NULL and current->elem.first != c)
		current = current->next;

	//if the key is not found
	if (current == NULL)
		return NULL_TVALUE;

	//if the key is found
	return current->elem.second;
}
//BC=Theta(1), if the key is on the first position in the table and SLL
//WC=Theta(nrElems), if all the elements are in the same SLL
//TC=O(nrElems)
//AC=Theta(nrElems/m + 1)

TValue Map::remove(TKey c){

	int position = this->hash(c, this->m);

	//keep the current and the previous node
	Node* current = this->table[position];
	Node* previous = NULL;

	//search for the key
	while (current != NULL and current->elem.first != c)
	{
		previous = current;
		current = current->next;
	}

	//if the key is not found
	if (current == NULL)
		return NULL_TVALUE;
	//if the key is found
	else
	{
		//save the value associated with the key
		TValue value = current->elem.second;

		//remove the node from the SLL and delete it

		//check if the node is the first in the SLL
		if (previous == NULL)
			this->table[position] = current->next;
		else
		{
			previous->next = current->next;
		}
		delete current;

		//decrease the number of elements in the map
		this->nrElem--;

		return value;
	}
}
//BC=Theta(1), if the key is on the first position in the table and SLL
//WC=Theta(nrElems), if all the elements are in the same SLL
//TC=O(nrElems)

int Map::size() const {
	return this->nrElem;
}
//BC=WC=TC=Theta(1)

bool Map::isEmpty() const{
	if (this->nrElem == 0)
		return true;
	return false;
}
//BC=WC=TC=Theta(1)

MapIterator Map::iterator() const {
	return MapIterator(*this);
}

void Map::resize()
{
	Node** newTable = new Node*[this->m * 2];
	for (int i = 0; i < this->m * 2; i++)
		newTable[i] = NULL;
	//rehash all the elements
	for (int i = 0; i < this->m; i++) {
		Node* current = this->table[i];
		while (current != NULL) {
			int newPosition = this->hash(current->elem.first, this->m * 2);
			
			//save the next node
			Node* next = current->next;

			//add the rehashed node at the beginning of the SLL
			current->next = newTable[newPosition];
			newTable[newPosition] = current;

			//move to the next node
			current = next;
		}
	}

	//delete the old table
	delete[] this->table;

	//update the table and the size
	this->table = newTable;
	this->m *= 2;
}
//BC=WC=TC=Theta(nrElems+m) because we have to rehash all the elements

int Map::hash(TKey key, int f) const
{
	if (key < 0)
		return (-1 * key) % f;
	return key % f;
}
//BC=WC=TC=Theta(1)

void Map::replace(TKey k, TValue oldValue, TValue newValue)
{
	int position = this->hash(k, this->m);
	Node* current = this->table[position];

	//search for the key
	while (current != NULL and current->elem.first != k)
		current = current->next;

	//if the key is not found
	if (current == NULL)
		return;

	//if the key is found
	if (current->elem.second == oldValue)
		current->elem.second = newValue;
}
//BC=Theta(1), if the key is on the first position in the table and SLL
//WC=Theta(nrElems), if all the elements are in the same SLL
//TC=O(nrElems)