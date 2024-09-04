#include "Product.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

Product createProduct(char* name, char* category, int quantity, Date time)
{
	Product prod;
	prod.name = malloc(sizeof(char) * (strlen(name) + 1));
	strcpy(prod.name, name);
	prod.category = malloc(sizeof(char) * (strlen(category) + 1));
	strcpy(prod.category, category);
	prod.quantity = quantity;
	prod.expiration_date = time;
	return prod;
}

void destroyProduct(Product* p)
{
	if (p == NULL)
		return;
	free(p->name);
	free(p->category);
}

char* getName(Product* p)
{
	return p->name;
}

char* getType(Product* p)
{
	return p->category;
}

void setQuantity(Product* p, int quantity)
{
	p->quantity = quantity;
}

int getQuantity(Product* p)
{
	return p->quantity;
}

void setDate(Product* p, Date date)
{
	p->expiration_date = date;
}

Date getDate(Product* p)
{
	return p->expiration_date;
}

void toString(Product p, char str[])
{
	sprintf(str, "Product name: %s, category: %s, quantity: %d, expiration date: %d-%d-%d", p.name, p.category, p.quantity, getDay(&p.expiration_date), getMonth(&p.expiration_date), getYear(&p.expiration_date));
}

int equals(Product a, Product b)
{
	if (strcmp(a.name, b.name) == 0 && strcmp(a.category, b.category) == 0)
		return 0;
	return 1;
}

int greaterQuantity(Product a, Product b)
{
	if (a.quantity > b.quantity)
		return 1;
	return 0;
}

Product copyProduct(Product p)
{
	Product new_p = createProduct(p.name, p.category, p.quantity, p.expiration_date);
	return new_p;
}

void testProduct()
{
	Product p = createProduct("Milk", "dairy", 10, createDate(10,10,2020));
	assert(strcmp(getName(&p), "Milk") == 0);
	assert(strcmp(getType(&p), "dairy") == 0);
	assert(getQuantity(&p) == 10);
	assert(getDay(&p.expiration_date) == 10);
	assert(getMonth(&p.expiration_date) == 10);
	assert(getYear(&p.expiration_date) == 2020);
	Date new_date = createDate(11,10,2020);
	setDate(&p, new_date);
	assert(getDay(&p.expiration_date) == 11);
	assert(getMonth(&p.expiration_date) == 10);
	assert(getYear(&p.expiration_date) == 2020);
	Product p2 = createProduct("Milk", "dairy", 10, createDate(10,10,2020));
	assert(equals(p, p2) == 0);
	assert(greaterQuantity(p, p2) == 0);
	destroyProduct(&p);
	destroyProduct(&p2);
}