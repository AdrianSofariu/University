#include "Operations.h"

Operation addOperation(Repository* repo, TElement p, simpleFunction addFct, simpleFunction deleteFct)
{
	Operation op;
	op.addFunction = addFct;
	op.deleteFunction = deleteFct;
	op.oldP = copyProduct(p);
	op.newP = copyProduct(p);
	op.type = 1;
	return op;
}

Operation deleteOperation(Repository* repo, TElement p, simpleFunction addFct, simpleFunction deleteFct)
{
	Operation op;
	op.addFunction = addFct;
	op.deleteFunction = deleteFct;
	op.oldP = copyProduct(p);
	op.newP = copyProduct(p);
	op.type = 2;
	return op;
}

Operation updateOperation(Repository* repo, TElement oldP, TElement newP, updateFunction updateFct)
{
	Operation op;
	op.updateFunction = updateFct;
	op.oldP = copyProduct(oldP);
	op.newP = copyProduct(newP);
	op.type = 3;
	return op;
}

void undoOperation(Operation* op, Repository* repo)
{
	if (op->type == 1)
	{
		op->deleteFunction(repo, op->oldP);
	}
	else if (op->type == 2)
	{
		op->addFunction(repo, copyProduct(op->oldP));
	}
	else if (op->type == 3)
	{
		op->updateFunction(repo, copyProduct(op->newP), copyProduct(op->oldP));
	}
}

void redoOperation(Operation* op, Repository* repo)
{
	if (op->type == 1)
	{
		op->addFunction(repo, copyProduct(op->oldP));
	}
	else if (op->type == 2)
	{
		op->deleteFunction(repo, op->oldP);
	}
	else if (op->type == 3)
	{
		op->updateFunction(repo, copyProduct(op->oldP), copyProduct(op->newP));
	}
}