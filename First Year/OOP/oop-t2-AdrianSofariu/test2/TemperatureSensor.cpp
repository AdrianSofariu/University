#include "TemperatureSensor.h"
#include <sstream>

bool TemperatureSensor::sendAlert()
{
    int ct = 0;
    for (double record : this->recordings)
    {
        if (record > 35)
            ct++;
        if (ct == 2)
            return true;
    }
    return false;
}

double TemperatureSensor::getPrice()
{
    if (this->diameter < 3)
        return 17;
    else
        return 9;
}

std::string TemperatureSensor::toString()
{
    std::string baseStr = Sensor::toString();
    std::stringstream output;

    output << "Temperature sensor -- " << baseStr;
    for (double record : this->recordings)
    {
        output << record << "C ";
    }
    output<< " diameter=" << this->diameter << " price=" << this->getPrice()<<"\n";
    return output.str();
}
