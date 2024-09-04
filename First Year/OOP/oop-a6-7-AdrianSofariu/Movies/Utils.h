#pragma once
#include <vector>
#include <string>
#include <sstream>

/*
	Tokenizes a string.
	Input:	str - the string to be tokenized.
	delimiter - char - the delimiter used for tokenization
	Output: a vector of strings, containing the tokens
*/
std::vector<std::string> tokenize(const std::string& str, char delimiter);
