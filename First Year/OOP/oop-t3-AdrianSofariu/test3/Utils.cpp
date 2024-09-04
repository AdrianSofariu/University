#include "Utils.h"

using namespace std;

std::vector<std::string> tokenize(const std::string str, char delimiter)
{
	stringstream ss(str);
	string token;
	vector<string> result;
	while (getline(ss, token, delimiter))
		result.push_back(token);
	return result;
}
