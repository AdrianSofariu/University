#pragma once
#include "Repository.h"
#include "Exceptions.h"
#include "Watchlist.h"
#include "FileWatchlist.h"
#include "HTMLWatchlist.h"
#include "CSVWatchlist.h"

class UserService
{
private:
	Repository& repo;
	FileWatchlist& watchlist;

public:

	//constructor
	UserService(Repository& _repo, FileWatchlist& _watchlist) : repo{ _repo }, watchlist{ _watchlist } {};

	//desctructor
	~UserService() {};

	//see all the movies in the watchlist
	std::vector<std::string> getWatchlist();

	//length of the watchlist
	int getWatchlistLength();

	//browse movies by genre
	//input: genre - string
	//output: a list of movies with the given string as genre or all movies in repo if the string is empty
	std::vector<Movie> browseByGenre(const std::string& genre);

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

	//save the watchlist to a file
	//input: filename - string
	//throws: file exception if it cannot be opened
	void saveWatchlist(const std::string& filename);

	//open the watchlist
	//throws: empty watchlist exception if it cannot be opened
	void openWatchlist() const;

};

void testUserService();

