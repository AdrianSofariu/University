#include "HumiditySensor.h"
#include <sstream>

bool HumiditySensor::sendAlert()
{
	int ct = 0;
	for (double record : this->recordings)
	{
		if (record < 30)
			ct++;
		if (ct == 2)
			return true;
	}
	return false;
}

double HumiditySensor::getPrice()
{
	return 4;
}

std::string HumiditySensor::toString()
{
	std::string baseStr = Sensor::toString();
	std::stringstream output;

	output << "Humidity sensor -- " << baseStr;
	for (double record : this->recordings)
	{
		output << record << "% ";
	}
	output << " price=" << this->getPrice() << "\n";
	return output.str();
}
