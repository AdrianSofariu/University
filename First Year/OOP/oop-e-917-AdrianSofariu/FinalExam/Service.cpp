#include "Service.h"
#include <vector>
#include <algorithm>

using namespace std;

std::vector<Department> Service::getDepartments()
{
    return repo.getDepartments();
}

std::vector<Volunteer> Service::getVolunteers()
{
    return repo.getVolunteers();
}

std::vector<Volunteer> Service::getByDepartment(std::string dept)
{
    vector<Volunteer> all = repo.getVolunteers();
    vector<Volunteer> filtered;
    for (Volunteer v : all)
        if (v.getDep() == dept)
            filtered.push_back(v);
    sort(filtered.begin(), filtered.end(), [](Volunteer& v1, Volunteer& v2) {return v1.getName() < v2.getName(); });
    return filtered;
}

std::vector<Volunteer> Service::getUnassigned()
{
    vector<Volunteer> all = repo.getVolunteers();
    vector<Volunteer> filtered;
    for (Volunteer v : all)
        if (v.getDep() == "")
            filtered.push_back(v);
    return filtered;
}

void Service::add(std::string name, std::string email, std::vector<std::string> interests)
{
    Volunteer v(name, email, interests, "");
    this->repo.add(v);
}

std::vector<Volunteer> Service::mostSuited(Department dept)
{
    vector<Volunteer> ms;
    vector<Volunteer> all = this->getUnassigned();
    sort(all.begin(), all.end(), [&](Volunteer& v1, Volunteer& v2) { return v1.getMatching(dept) > v2.getMatching(dept); });
    if (all.size() < 3)
        return all;
    for (int i = 0; i < 3; i++)
    {
        ms.push_back(all[i]);
    }
    return ms;
}

void Service::assign(std::string name, std::string dep)
{
    this->repo.assign(name, dep);
}
