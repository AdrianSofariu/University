#pragma once
#include "Sensor.h"

class HumiditySensor: public Sensor
{

public:
	HumiditySensor(std::string& _producer, std::vector<double> _recordings) :Sensor{ _producer, _recordings }{}
	~HumiditySensor() override {};
	bool sendAlert() override;
	double getPrice() override;
	std::string toString() override;
};

