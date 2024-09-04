#pragma once
#include "Repository.h"
#include "Exceptions.h"

class TextFileRepository : public Repository
{
private:
	std::string filename;

public:
	TextFileRepository(std::string filename);
	~TextFileRepository() {};

	void addMovie(const Movie& movie) override;
	void deleteMovie(const Movie& movie) override;
	void updateMovie(const Movie& movie, const Movie& new_movie) override;

private:
	void readFromFile();
	void writeToFile();

};

