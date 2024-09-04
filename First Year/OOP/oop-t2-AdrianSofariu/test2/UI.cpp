#include "UI.h"
#include <string>
#include <vector>
#include <exception>
#include <iostream>
#include "SmokeSensor.h"
#include "HumiditySensor.h"
#include "TemperatureSensor.h"

using namespace std;

void UI::run()
{
	try {

		int command;
		while (true)
		{
			this->printMenu();
			cin >> command;
			if (command == 1)
				this->addSensorToDevice();
			if (command == 2)
				this->printSensors();
			if (command == 3)
				this->printAlertingSensors();
			if (command == 4)
				this->saveSensors();
			if (command == 0)
				break;
		}
	}
	catch (exception& ex)
	{
		cout << ex.what() << "\n";
	}
	
}

void UI::addSensorToDevice()
{
	string type;
	cout << "Please specify the type of sensor(t/h/s):\n";
	cin >> type;
	if (type == "t")
	{
		double diameter;
		cout << "Diameter: ";
		cin >> diameter;

		string producer;
		cout << "Producer: ";
		cin >> producer;

		double record = 10;
		vector<double> recordings;
		cout << "Read recordings until 0:\n";
		while (record != 0)
		{
			cin >> record;
			if (record != 0)
				recordings.push_back(record);
		}

		TemperatureSensor* ts = new TemperatureSensor{ diameter, producer, recordings };
		this->device.addSensor(ts);
	}
	else if (type == "h")
	{
		string producer;
		cout << "Producer: ";
		cin >> producer;

		double record = 10;
		vector<double> recordings;
		cout << "Read recordings until 0:\n";
		while (record != 0)
		{
			cin >> record;
			if (record != 0)
				recordings.push_back(record);
		}

		HumiditySensor* hs = new HumiditySensor{ producer, recordings };
		this->device.addSensor(hs);
		
	}
	else if (type == "s")
	{
		string producer;
		cout << "Producer: ";
		cin >> producer;

		double record = 10;
		vector<double> recordings;
		cout << "Read recordings until 0:\n";
		while (record != 0)
		{
			cin >> record;
			if (record != 0)
				recordings.push_back(record);
		}

		SmokeSensor* ss = new SmokeSensor{ producer, recordings };
		this->device.addSensor(ss);
	}
	else
		throw exception("Invalid type");
}

void UI::printSensors()
{
	vector<Sensor*> sensors = this->device.getAllSensors();
	for (auto sensor : sensors)
	{
		cout << sensor->toString();
	}
}

void UI::printAlertingSensors()
{
	vector<Sensor*> sensors = this->device.getAlertingSensors();
	for (auto sensor : sensors)
	{
		cout << sensor->toString();
	}
}

void UI::saveSensors()
{
	double price;
	string filename;
	cout << "Give a price: ";
	cin >> price;
	cout << "Give filename: ";
	cin >> filename;
	this->device.writeToFile(filename, price);
}

void UI::printMenu()
{
	cout << "1. Add new sensor\n";
	cout << "2. Show all sensors\n";
	cout << "3. Show alerting sensors\n";
	cout << "4. Save to file sensors with price under value\n";
	cout << "0. Exit\n";
}
