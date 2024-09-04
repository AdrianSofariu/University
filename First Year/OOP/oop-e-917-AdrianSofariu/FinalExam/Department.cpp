#include "Department.h"
#include <vector>
#include "Utils.h"

using namespace std;

std::istream& operator>>(std::istream& is, Department& dept)
{
    string line;
    getline(is, line);

    vector<string> tokens = tokenize(line, ',');

    if (tokens.size() != 2)
        return is;

    dept.name = tokens[0];
    dept.desc = tokens[1];
    return is;
}

std::ostream& operator<<(std::ostream& os, Department dept)
{
    os << dept.name << "," << dept.desc << "\n";
    return os;
}
