#pragma once
#include "Service.h"
#include <iostream>

using namespace std;

class UI
{
private:
	Service serv;

public:
	UI(Service serv);
	void print_menu();
	void run();

	/// <summary>
	/// Read input for a new protein obj and add it to the repo
	/// </summary>
	void addProtein();

	void displayAll();

	/// <summary>
	/// Read a name and display all proteins with the given name sorted by organsims and the number of organisms
	/// </summary>
	void showAllWithName();
};

