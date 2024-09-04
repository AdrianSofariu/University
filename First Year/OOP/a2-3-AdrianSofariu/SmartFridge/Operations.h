#pragma once
#include "Product.h"
#include "Repository.h"

typedef void (*simpleFunction)(Repository*, TElement);
typedef void (*updateFunction)(Repository*, TElement, TElement);

typedef struct
{
	void (*addFunction)(Repository* repo, TElement p);
	void (*deleteFunction)(Repository* repo, TElement p);
	void (*updateFunction)(Repository* repo, TElement oldP, TElement newP);
	TElement oldP;
	TElement newP;
	int type;
} Operation;


Operation addOperation(Repository* repo, TElement p, simpleFunction addFct, simpleFunction deleteFct);

Operation deleteOperation(Repository* repo, TElement p, simpleFunction addFct, simpleFunction deleteFct);

Operation updateOperation(Repository* repo, TElement oldP, TElement newP, updateFunction updateFct);

void undoOperation(Operation* op, Repository* repo);

void redoOperation(Operation* op, Repository* repo);
