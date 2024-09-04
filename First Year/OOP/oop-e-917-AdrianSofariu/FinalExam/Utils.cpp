#include "Utils.h"

using namespace std;

std::vector<std::string> tokenize(std::string line, char delim)
{
	stringstream ss{ line };
	string token;
	vector<string> tokens;

	while (getline(ss, token, delim))
	{
		tokens.push_back(token);
	}

	return tokens;
}
