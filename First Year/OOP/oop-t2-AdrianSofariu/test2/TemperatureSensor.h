#pragma once
#include "Sensor.h"

class TemperatureSensor: public Sensor
{
private:
	double diameter;
public:
	TemperatureSensor(double _diameter, std::string& _producer, std::vector<double> _recordings):Sensor{_producer, _recordings}, diameter{_diameter}{}
	~TemperatureSensor() override {};
	bool sendAlert() override;
	double getPrice() override;
	std::string toString() override;
};

