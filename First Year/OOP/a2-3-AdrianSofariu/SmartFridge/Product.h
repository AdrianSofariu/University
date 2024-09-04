#pragma once
#include "Date.h"


typedef struct {
	char* name;
	char* category;
	int quantity;
	Date expiration_date;
}Product;

Product createProduct(char* name, char* category, int quantity, Date time);
void destroyProduct(Product* product);

char* getName(Product* p);
char* getType(Product* p);
void setQuantity(Product* p, int quantity);
void setDate(Product* p, Date date);
Date getDate(Product* p);
int getQuantity(Product* p);
void toString(Product p, char str[]);

/// <summary>
/// Compares two products.
/// Two products are equal if their name and category are equal.
/// </summary>
/// <param name="p1">Product</param>
/// <param name="p2">Product</param>
/// <returns>Integer, 0 if they are equal, 1 otherwise</returns>
int equals(Product p1, Product p2);

/// <summary>
/// Compares two products using quantity field.
/// </summary>
/// <param name="p1">Product</param>
/// <param name="p2">Product</param>
/// <returns>Integer, 1 if p1.quantity > p2.quantity, 0 otherwise</returns>
int greaterQuantity(Product p1, Product p2);

/// <summary>
/// Copy a product
/// </summary>
/// <param name="p">Product</param>
/// <returns>A pointer to a new product, identical to p</returns>
Product copyProduct(Product p);

//tests
void testProduct();