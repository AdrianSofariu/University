#include "DAIterator.h"

//DAIterator createDAIterator(Product* product_list, int length)
//{
//	DAIterator it;
//	it.products = product_list;
//	it.current = 0;
//	it.length = length;
//	return it;
//}

int validIterator(DAIterator* it)
{
	if (it->current < it->length)
		return 0;
	return -1;
}

void next(DAIterator* it)
{
	if (validIterator(it) == 0)
	{
		it->current++;
	}
}

void reset(DAIterator* it)
{
	it->current = 0;
}

Product getCurrent(DAIterator* it)
{
	if (validIterator(it) == 0)
	{
		return it->products[it->current];
	}
}


