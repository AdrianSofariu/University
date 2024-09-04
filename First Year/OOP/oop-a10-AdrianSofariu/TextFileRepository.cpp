#include "TextFileRepository.h"
#include <fstream>

TextFileRepository::TextFileRepository(std::string filename)
{
	this->filename = filename;
	this->readFromFile();
}

void TextFileRepository::addMovie(const Movie& movie)
{
	Repository::addMovie(movie);
	this->writeToFile();
}

void TextFileRepository::deleteMovie(const Movie& movie)
{
	Repository::deleteMovie(movie);
	this->writeToFile();
}

void TextFileRepository::updateMovie(const Movie& movie, const Movie& new_movie)
{
	Repository::updateMovie(movie, new_movie);
	this->writeToFile();
}

void TextFileRepository::readFromFile()
{
	std::ifstream file(this->filename);
	if (!file.is_open())
		throw FileException("File could not be opened!");

	Movie movie;
	while (file >> movie)
	{
		this->movies.push_back(movie);
	}
	file.close();
}

void TextFileRepository::writeToFile()
{
	std::ofstream file(this->filename);
	if (!file.is_open())
		throw FileException("File could not be opened!");

	for (auto m : this->movies)
	{
		file << m;
	}
	file.close();
}



