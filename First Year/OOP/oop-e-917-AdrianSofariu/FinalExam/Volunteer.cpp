#include "Volunteer.h"
#include "Utils.h"
#include <string>
#include <vector>
#include <Department.h>

using namespace std;

std::istream& operator>>(std::istream& is, Volunteer& vol)
{
    string line;
    getline(is, line);

    vector<string> tokens = tokenize(line, ',');

    if (tokens.size() == 4)
    {
        vector<string> interests = tokenize(tokens[2], '|');
        vol.name = tokens[0];
        vol.email = tokens[1];
        vol.interests = interests;
        vol.dept = tokens[3];
    }
    else if (tokens.size() == 3)
    {
        vector<string> interests = tokenize(tokens[2], '|');
        vol.name = tokens[0];
        vol.email = tokens[1];
        vol.interests = interests;
        vol.dept = "";
    }
    else
        return is;

    return is;
}

std::ostream& operator<<(std::ostream& os, Volunteer vol)
{
    os << vol.name << ',' << vol.email << ",";
    for (int i = 0; i < vol.interests.size(); i++)
    {
        if (i != vol.interests.size() - 1)
            os << vol.interests[i] << "|";
        else
            os << vol.interests[i] << ",";
    }
    os << vol.dept << "\n";
    return os;
}

double Volunteer::getMatching(Department d)
{
    double score = 0.0;
    for (string word : this->interests)
        if (strstr(d.getDec().c_str(), word.c_str()) != nullptr)
            score++;
    vector<string> aux = tokenize(d.getDec(), ' ');
    score /= aux.size();
    return score;
}

bool Volunteer::operator==(const Volunteer& other)
{
    return this->name == other.name;
}
