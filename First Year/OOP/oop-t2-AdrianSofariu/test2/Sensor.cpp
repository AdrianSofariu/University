#include "Sensor.h"
#include <sstream>

std::string Sensor::toString()
{
	std::stringstream output;
	output << this->producer << " ";
	return output.str();
}
