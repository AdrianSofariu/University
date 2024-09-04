#include "Repository.h"
#include <stdexcept>
#include <algorithm>
#include <assert.h>

void Repository::addMovie(const Movie& movie)
{
	Movie* found = this->findMovie(movie);
	if (found != NULL)
		throw DuplicateMovieException();
	this->movies.push_back(movie);
}

void Repository::deleteMovie(const Movie& movie)
{
	std::vector<Movie>::iterator found = std::find(this->movies.begin(), this->movies.end(), movie);
	if (found == this->movies.end())
		throw InexistentMovieException();
	this->movies.erase(found);
}

void Repository::updateMovie(const Movie& movie, const Movie& new_movie)
{
	Movie* found = this->findMovie(movie);
	if (found == NULL)
		throw InexistentMovieException();
	found->setGenre(new_movie.getGenre());
	found->setTrailer(new_movie.getTrailer());
	found->setYear(new_movie.getYear());
	found->setLikes(new_movie.getLikes());

}

Movie* Repository::findMovie(const Movie& movie)
{
	std::vector<Movie>::iterator found = std::find(this->movies.begin(), this->movies.end(), movie);
	if (found != this->movies.end())
	{
		return &(*found);
	}
	return NULL;
}

Movie Repository::findMovieByTitle(const std::string& title)
{
	for (auto m : this->movies)
	{
		if (m.getTitle() == title)
			return m;
	}
	throw InexistentMovieException();
}

int Repository::getLength() const
{
	return this->movies.size();
}

Movie& Repository::operator[](int index)
{
	return this->movies[index];
}

void testRepository()
{
	// Test addMovie
	Movie movie1("Title1", "Genre1", 2021, 100, "Trailer1");
	Movie movie2("Title2", "Genre2", 2022, 200, "Trailer2");
	Repository repository;
	repository.addMovie(movie1);
	assert(repository.getLength() == 1);
	repository.addMovie(movie2);
	assert(repository.getLength() == 2);
	try
	{
		repository.addMovie(movie1);
	}
	catch (DuplicateMovieException& e)
	{
		assert(true);
	};

	// Test operator[]
	assert(repository[0].getTitle() == "Title1");

	// Test deleteMovie
	repository.deleteMovie(movie1);
	assert(repository.getLength() == 1);
	try
	{
		repository.deleteMovie(movie1);
	}
	catch (InexistentMovieException& e)
	{
		assert(true);
	};
	repository.deleteMovie(movie2);
	assert(repository.getLength() == 0);

	// Test updateMovie
	Movie movie3("Title3", "Genre3", 2023, 300, "Trailer3");
	repository.addMovie(movie3);
	assert(repository.getLength() == 1);
	Movie newMovie("Title3", "NewGenre", 2024, 400, "NewTrailer");
	repository.updateMovie(movie3, newMovie);
	assert(repository.findMovie(newMovie)->getTitle() == "Title3");
	assert(repository.findMovie(newMovie)->getGenre() == "NewGenre");
	assert(repository.findMovie(newMovie)->getYear() == 2024);
	assert(repository.findMovie(newMovie)->getLikes() == 400);
	assert(repository.findMovie(newMovie)->getTrailer() == "NewTrailer");
}

