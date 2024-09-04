#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


MapIterator::MapIterator(const Map& d) : map(d)
{
	this->currentPos = 0;
	while (this->currentPos < this->map.m && this->map.table[this->currentPos] == NULL)
		this->currentPos++;
	if (this->currentPos < this->map.m)
		this->currentNode = this->map.table[this->currentPos];
	else
		this->currentNode = NULL;
}
//BC=Theta(1), if we have an element on the first position in the table
//WC=Theta(m), if all the elements are on the last position in the table or it is empty
//TC=O(m)


void MapIterator::first() {
	this->currentPos = 0;
	while (this->currentPos < this->map.m && this->map.table[this->currentPos] == NULL)
		this->currentPos++;
	if (this->currentPos < this->map.m)
		this->currentNode = this->map.table[this->currentPos];
	else
		this->currentNode = NULL;
}
//BC=Theta(1), if we have an element on the first position in the table
//WC=Theta(m), if all the elements are on the last position in the table or it is empty
//TC=O(m)


void MapIterator::next() {
	if (this->currentNode == NULL && this->currentPos == this->map.m)
		throw exception();
	if (this->currentNode->next != NULL)
		this->currentNode = this->currentNode->next;
	else {
		this->currentPos++;
		while (this->currentPos < this->map.m && this->map.table[this->currentPos] == NULL)
			this->currentPos++;
		if (this->currentPos < this->map.m)
			this->currentNode = this->map.table[this->currentPos];
		else
			this->currentNode = NULL;
	}
}
//BC=Theta(1), if we have an element on the next position in the table
//WC=Theta(m), if we only have elements on the first & last positions in the table and we go from the first to the last position in the table
//			   or if we have all the elements on the first position in the table and we search the next position
//TC=O(m)


TElem MapIterator::getCurrent() {
	if (this->currentNode == NULL && this->currentPos == this->map.m)
		throw exception();
	return this->currentNode->elem;
}
//BC=WC=TC=Theta(1)

bool MapIterator::valid() const {
	if (this->currentNode == NULL && this->currentPos == this->map.m)
		return false;
	return true;
}
//BC=WC=TC=Theta(1)