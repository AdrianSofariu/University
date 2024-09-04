#pragma once
#include "Repository.h"

class UserService
{
private:
	Repository& repo;
	DynamicArray<Movie> watchlist;

public:

	//constructor
	UserService(Repository& repo) : repo{ repo } {};

	//desctructor
	~UserService() {};

	//see all the movies in the watchlist
	DynamicArray<std::string> getWatchlist();

	//length of the watchlist
	int getWatchlistLength();

	//browse movies by genre
	//input: genre - string
	//output: a list of movies with the given string as genre or all movies in repo if the string is empty
	DynamicArray<Movie> browseByGenre(const std::string& genre);

	//add a movie to the watchlist
	//input: movie - Movie
	//output: the movie is added to the watchlist
	//throws: exception if the movie is already in the watchlist
	void addToWatchlist(const Movie& movie);

	//remove a movie from the watchlist
	//input: movie - Movie
	//output: the movie is removed from the watchlist
	//throws: exception if the movie is not in the watchlist
	void removeFromWatchlist(const Movie& movie);

	//like a movie
	//input: movie - Movie
	//output: the number of likes of the movie is incremented
	void likeMovie(const Movie& movie);

	//open the link of a movie
	//input: movie - Movie
	//output: the link is opened in browser
	void openLink(const Movie& movie);

};

void testUserService();

