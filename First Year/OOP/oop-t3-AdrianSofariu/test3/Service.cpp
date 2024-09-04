#include "Service.h"

std::vector<Medication> Service::get_medications() const
{
    return this->repo.get_medications();
}

std::vector<std::string> Service::get_side_effects(std::string name) const
{
    return this->repo.get_side_effects(name);
}
