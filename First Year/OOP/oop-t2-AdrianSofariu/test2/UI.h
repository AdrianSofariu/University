#pragma once
#include "Device.h"

class UI
{
private:
	Device& device;
public:
	UI(Device& dev) :device{ dev } {};
	void run();
	void addSensorToDevice();
	void printSensors();
	void printAlertingSensors();
	void saveSensors();
private:
	void printMenu();
};

