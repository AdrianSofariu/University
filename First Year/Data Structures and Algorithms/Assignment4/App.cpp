#include "ExtendedTest.h"
#include "ShortTest.h"
#include "assert.h"
#include "Map.h"


#include <iostream>
using namespace std;

void test_replace()
{
	cout << "Test replace\n";
	Map m = Map();

	m.add(1, 2);
	m.add(2, 3);

	m.replace(1, 2, 3);
	m.replace(2, 1, 1);
	m.replace(3, 1, 0);

	assert(m.search(1) == 3);
	assert(m.search(2) == 3);
	assert(m.search(3) == NULL_TVALUE);
}


int main() {
	testAll();
	testAllExtended();
	test_replace();
	cout << "That's all!" << endl;
	system("pause");
	_CrtDumpMemoryLeaks();
	return 0;
}


