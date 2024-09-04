#pragma once
#include "Sensor.h"
#include <vector>

class Device
{
private:
	std::vector<Sensor*>sensors;

public:
	Device() {};
	~Device() { this->deleteSensors(); };
	void addSensor(Sensor* sensor);
	std::vector<Sensor*> getAllSensors();
	std::vector<Sensor*> getAlertingSensors();
	void writeToFile(std::string filename, double price=25);

private:
	void initDevice();
	void deleteSensors();
};

