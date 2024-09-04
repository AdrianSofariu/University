#include "SmokeSensor.h"
#include <sstream>


bool SmokeSensor::sendAlert()
{
	int ct = 0;
	for (double record : this->recordings)
	{
		if (record > 1600)
			return true;
	}
	return false;
}

double SmokeSensor::getPrice()
{
    return 25;
}

std::string SmokeSensor::toString()
{
	std::string baseStr = Sensor::toString();
	std::stringstream output;

	output << "Smoke sensor -- " << baseStr;
	for (double record : this->recordings)
	{
		output << record << "p ";
	}
	output << " price=" << this->getPrice() << "\n";
	return output.str();
}


