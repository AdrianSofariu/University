#include "UI.h"
#include <string>


UI::UI(Service serv)
{
	this->serv = serv;
}

void UI::print_menu()
{
	cout << "1. Add a protein" << endl;
	cout << "2. Show all proteins" << endl;
	cout << "3. Show proteins with given name" << endl;
	cout << "0. Exit" << endl;
}

void UI::run()
{
	int option;
	while (1)
	{
		this->print_menu();
		cout << "Choose a command: ";
		try
		{
			cin >> option;
			switch (option)
			{
			case 1:
				addProtein();
				break;
			case 2:
				displayAll();
				break;
			case 3:
				showAllWithName();
				break;
			case 0:
				return;
			default:
				cout << "Invalid command";
				break;
			}
		}
		catch (exception& e)
		{
			cout << e.what() << endl;
		}
	}
}

void UI::addProtein()
{
	std::string organism, name, sequence;
	cout << "Input the organism: ";
	cin >> organism;
	cout << "Input the name: ";
	cin >> name;
	cout << "Input the sequence: ";
	cin >> sequence;

	this->serv.addRecord(organism, name, sequence);
}

void UI::displayAll()
{
	vector<string> display_records;
	vector<Protein> records = this->serv.getProteins();

	vector<Protein>::iterator it;
	vector<string>::iterator it2;

	for (it = records.begin(); it != records.end(); it++)
		display_records.push_back((*it).toString());
	
	for (it2 = display_records.begin(); it2 != display_records.end(); it2++)
		cout << *it2;
}

void UI::showAllWithName()
{
	std::string name;
	cout << "Give a name: ";
	cin >> name;
	cout << endl;

	vector<Protein> records = this->serv.getProteinsByName(name);
	vector<Protein>::iterator it;


	for (it = records.begin(); it != records.end(); it++)
		cout<< (*it).toString();

	cout << "There are " << records.size() << " organisms" <<endl<<endl;
}

