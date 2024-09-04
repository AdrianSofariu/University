#pragma once
#include <string>
#include <vector>

class Sensor
{
protected:
	std::string producer;
	std::vector<double> recordings;
public:
	Sensor(std::string& _producer, std::vector<double> _recordings) : producer{_producer},  recordings{_recordings}{}
	virtual ~Sensor() {};
	virtual bool sendAlert() = 0;
	virtual double getPrice() = 0;
	virtual std::string toString();
	std::string getProducer() { return this->producer; };
};