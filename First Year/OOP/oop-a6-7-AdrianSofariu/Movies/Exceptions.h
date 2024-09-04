#pragma once

#include <exception>
#include <string>
#include <vector>

//file exception
class FileException : public std::exception
{
protected:
	std::string message;
public:
	FileException(const std::string& msg) : message{ msg } {};
	virtual const char* what();
};

//repository exception
class RepositoryException : public std::exception
{
protected:
	std::string message;
public:
	RepositoryException(const std::string& msg) : message{ msg } {};
	RepositoryException() {};
	~RepositoryException() {};
	virtual const char* what();
};


//duplicate movie exception
class DuplicateMovieException : public RepositoryException
{
public:
	const char* what();
};

//inexistent movie exception
class InexistentMovieException : public RepositoryException
{
public:
	const char* what();
};

//movie validator exception
class MovieException
{
private:
	std::vector<std::string> errors;

public:
	MovieException(std::vector<std::string> _errors) : errors{ _errors } {};
	std::vector<std::string> getErrors() const;
};

//empty watchlist exception
class EmptyWatchlistException : public std::exception
{
public:
	const char* what();
};