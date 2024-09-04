#include "Device.h"
#include <fstream>
#include <algorithm>
#include "TemperatureSensor.h"
#include "HumiditySensor.h"
#include "SmokeSensor.h"

void Device::addSensor(Sensor* sensor)
{
	this->sensors.push_back(sensor);
}

std::vector<Sensor*> Device::getAllSensors()
{
	return this->sensors;
}

std::vector<Sensor*> Device::getAlertingSensors()
{
	std::vector<Sensor*> alertingSensors;
	for (auto sensor : this->sensors)
	{
		if (sensor->sendAlert())
			alertingSensors.push_back(sensor);
	}
	return alertingSensors;
}

void Device::writeToFile(std::string filename, double price)
{
	std::ofstream f(filename);
	std::vector<Sensor*> filtered;
	for (auto sensor : this->sensors)
	{
		if (sensor->getPrice() < price)
			filtered.push_back(sensor);
	}
	std::sort(filtered.begin(), filtered.end(), [](Sensor* a, Sensor* b)->bool { return a->getProducer() < b->getProducer();  });
	for (auto sensor : filtered)
		f << sensor->toString();
}

void Device::initDevice()
{
	std::vector<double> records;
	records.push_back(1);
	records.push_back(2);

}

void Device::deleteSensors()
{
	for (auto sensor : this->sensors)
		delete sensor;
}


