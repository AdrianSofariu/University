#include "Exceptions.h"

const char* RepositoryException::what()
{
	return this->message.c_str();
}

const char* FileException::what()
{
	return this->message.c_str();
}

const char* DuplicateMovieException::what()
{
	return "A movie with the same title already exists!";
}

const char* InexistentMovieException::what()
{
	return "A movie with the given title does not exist";
}

std::vector<std::string> MovieException::getErrors() const
{
	return this->errors;
}

const char* EmptyWatchlistException::what()
{
	return "The watchlist is empty!";
}

const char* UndoException::what()
{
	return "No more undos!";
}

const char* RedoException::what()
{
	return "No more redos!";
}
