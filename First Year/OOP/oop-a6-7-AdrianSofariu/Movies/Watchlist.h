#pragma once
#include "Movie.h"
#include <vector>

class Watchlist
{
protected:
	std::vector<Movie> movies;

public:
	Watchlist() {};
	virtual ~Watchlist() {};

	// Adds a movie to the watchlist.
	// Input: movie - Movie.
	// Output: the movie is added to the watchlist.
	// Throws: exception if the movie is already in the watchlist.
	virtual void addMovie(const Movie& movie);

	// Deletes a movie from the watchlist.
	// Input: movie - Movie.
	// Output: the movie is deleted from the watchlist.
	// Throws: exception if the movie is not in the watchlist.
	virtual void deleteMovie(const Movie& movie);

	// Updates a movie from the watchlist.
	// Input: movie - Movie, new_movie - Movie.
	// Output: the movie is updated in the watchlist.
	// Throws: exception if the movie is not in the watchlist.
	virtual void updateMovie(const Movie& movie, const Movie& new_movie);

	// Finds a movie in the watchlist.
	// Input: movie - Movie.
	// Output: the movie or null if it is not in the watchlist.
	Movie* findMovie(const Movie& movie);

	// Gets the length of the repo
	int getLength() const;

	// Overload [] operator
	Movie& operator[](int index);

	// get all elements from the watchlist
	std::vector<Movie> getRepo() const { return movies; };

};

