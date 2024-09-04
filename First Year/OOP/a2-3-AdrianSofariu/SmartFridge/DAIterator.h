#pragma once
#include "Product.h"

typedef struct {
	Product* products;
	int current;
	int length;
}DAIterator;


Product getCurrent(DAIterator* it);
void next(DAIterator* it);
void reset(DAIterator* it);
int validIterator(DAIterator* it);
