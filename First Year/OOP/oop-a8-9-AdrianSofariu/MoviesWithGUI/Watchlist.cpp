#include "Watchlist.h"
#include "Exceptions.h"
#include <stdexcept>
#include <algorithm>
#include <assert.h>


void Watchlist::addMovie(const Movie& movie)
{
	Movie* found = this->findMovie(movie);
	if (found != NULL)
		throw DuplicateMovieException();
	this->movies.push_back(movie);
}

void Watchlist::deleteMovie(const Movie& movie)
{
	std::vector<Movie>::iterator found = std::find(this->movies.begin(), this->movies.end(), movie);
	if (found == this->movies.end())
		throw InexistentMovieException();
	this->movies.erase(found);
}

void Watchlist::updateMovie(const Movie& movie, const Movie& new_movie)
{
	Movie* found = this->findMovie(movie);
	if (found == NULL)
		throw InexistentMovieException();
	found->setGenre(new_movie.getGenre());
	found->setTrailer(new_movie.getTrailer());
	found->setYear(new_movie.getYear());
	found->setLikes(new_movie.getLikes());

}

Movie* Watchlist::findMovie(const Movie& movie)
{
	std::vector<Movie>::iterator found = std::find(this->movies.begin(), this->movies.end(), movie);
	if (found != this->movies.end())
	{
		return &(*found);
	}
	return NULL;
}

int Watchlist::getLength() const
{
	return this->movies.size();
}

Movie& Watchlist::operator[](int index)
{
	return this->movies[index];
}