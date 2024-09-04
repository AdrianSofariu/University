#pragma once
#include "DynamicArray.h"
#include "Movie.h"

class Repository
{
private:
	DynamicArray<Movie> movies;

public:
	Repository(DynamicArray<Movie>& movies) : movies{ movies } {};
	~Repository() {};

	// Adds a movie to the repository.
	// Input: movie - Movie.
	// Output: the movie is added to the repository.
	// Throws: exception if the movie is already in the repository.
	void addMovie(const Movie& movie);

	// Deletes a movie from the repository.
	// Input: movie - Movie.
	// Output: the movie is deleted from the repository.
	// Throws: exception if the movie is not in the repository.
	void deleteMovie(const Movie& movie);

	// Updates a movie from the repository.
	// Input: movie - Movie, new_movie - Movie.
	// Output: the movie is updated in the repository.
	// Throws: exception if the movie is not in the repository.
	void updateMovie(const Movie& movie, const Movie& new_movie);

	// Finds a movie in the repository.
	// Input: movie - Movie.
	// Output: the movie or null if it is not in the repository.
	Movie* findMovie(const Movie& movie);

	// Gets the length of the repo
	int getLength() const;

	// Overload [] operator
	Movie& operator[](int index);
};

// Tests the Repository class.
void testRepository();
void testDynamicArray();

