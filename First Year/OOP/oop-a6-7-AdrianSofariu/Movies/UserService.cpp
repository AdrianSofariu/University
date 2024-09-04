#include "UserService.h"
#include <stdexcept>
#include <windows.h>
#include <tchar.h>
#include <assert.h>
#include <algorithm>
#include <iterator>

std::vector<std::string> UserService::getWatchlist()
{
	std::vector<std::string> v;
	for (Movie m : this->watchlist.getRepo())
	{
		v.push_back(m.toString());
	}
	return v;
}

int UserService::getWatchlistLength()
{
	return this->watchlist.getLength();
}

std::vector<Movie> UserService::browseByGenre(const std::string& genre)
{
	std::vector<Movie> matching_genre;
	std::vector<Movie> all_movies = this->repo.getRepo();
	if(genre == "")
	{
		std::copy(all_movies.begin(), all_movies.end(), std::back_inserter(matching_genre));
	}
	else
	{
		std::copy_if(all_movies.begin(), all_movies.end(), std::back_inserter(matching_genre), [genre](Movie m) {return m.getGenre() == genre; });
	}
	return matching_genre;
}

void UserService::addToWatchlist(const Movie& movie)
{
	this->watchlist.addMovie(movie);
}

void UserService::removeFromWatchlist(const Movie& movie)
{
	this->watchlist.deleteMovie(movie);
}

void UserService::likeMovie(const Movie& movie)
{
	Movie* found = this->repo.findMovie(movie);
	if (found == NULL)
		throw InexistentMovieException();
	found->setLikes(found->getLikes() + 1);
}

void UserService::openLink(const Movie& movie)
{
	//open the link of a movie in browser
	std::string trailer = movie.getTrailer();
	std::string command = "start " + trailer;
	std::system(command.c_str());
}

void UserService::saveWatchlist(const std::string& filename)
{
	this->watchlist.setFilename(filename);
	this->watchlist.writeToFile();
}

void UserService::openWatchlist() const
{
	if (this->watchlist.getLength() != 0)
		this->watchlist.displayWatchlist();
	else
		throw EmptyWatchlistException();
}

void testUserService()
{

	Movie movie1("Title1", "Genre1", 2021, 100, "Trailer1");
	Movie movie2("Title2", "Genre2", 2022, 200, "Trailer2");
	Repository repository;
	CSVWatchlist watchlist;
	UserService userserv{repository, watchlist};

	//Test addToWatchlist
	userserv.addToWatchlist(movie1);
	userserv.addToWatchlist(movie2);
	try {
		userserv.addToWatchlist(movie1);
	}
	catch (DuplicateMovieException& d)
	{
		assert(true);
	}

	// Test getWatchlistLength
	assert(userserv.getWatchlistLength() == 2);


	// Test getWatchlist
	std::vector<std::string> wl = userserv.getWatchlist();

	assert(wl[0] == movie1.toString());
	assert(wl[1] == movie2.toString());
	assert(wl.size() == 2);

	// Test browseByGenre
	Movie m1("Titanic", "Drama", 1997, 100, "https://www.imdb.com/title/tt0120338/");
	Movie m2("Inception", "Action", 2010, 150, "https://www.imdb.com/title/tt1375666/");
	Movie m3("The Shawshank Redemption", "Drama", 1994, 142, "https://www.imdb.com/title/tt0111161/");
	repository.addMovie(m1);
	repository.addMovie(m2);
	repository.addMovie(m3);

	std::vector<Movie> matching_genre = userserv.browseByGenre("Drama");
	assert(matching_genre.size() == 2);

	std::vector<Movie> matching_genre2 = userserv.browseByGenre("");
	assert(matching_genre2.size() == 3);


	// Test removeFromWatchlist
	userserv.removeFromWatchlist(movie1);
	assert(userserv.getWatchlistLength() == 1);
	try {
		userserv.removeFromWatchlist(movie1);
	}
	catch (InexistentMovieException& e)
	{
		assert(true);
	}

	// Test likeMovie
	userserv.likeMovie(m1);
	assert(repository.findMovie(m1)->getLikes() == 101);

	// Test openLink
	userserv.openLink(m1);
}
