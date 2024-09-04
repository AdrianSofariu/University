#pragma once
#include "Sensor.h"

class SmokeSensor: public Sensor
{
public:
	SmokeSensor(std::string& _producer, std::vector<double> _recordings) :Sensor{ _producer, _recordings } {}
	~SmokeSensor() override {};
	bool sendAlert() override;
	double getPrice() override;
	std::string toString() override;
};

