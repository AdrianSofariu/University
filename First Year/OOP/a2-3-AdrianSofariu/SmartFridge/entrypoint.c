#include <stdio.h>
#include <string.h>
#include <crtdbg.h>

#include "DynamicArray.h"
#include "Controller.h"
#include "UserInterface.h"
#include "Repository.h"

int main()
{
	testsDynamicArray();
	testProduct();
	testDate();
	testRepository();
	testController();
	testUndoRedo();

	DynamicArray* arr = createDynamicArray(20, destroyProduct);
	Repository* repo = createRepository(arr);
	initRepo(repo);
	Controller* ctrl = createController(repo);
	UI* ui = createUI(ctrl);
	startUI(ui);
	destroyUI(ui);

	_CrtDumpMemoryLeaks();
	return 0;
}