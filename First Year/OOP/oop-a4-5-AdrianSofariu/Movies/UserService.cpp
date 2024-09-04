#include "UserService.h"
#include <stdexcept>
#include <windows.h>
#include <tchar.h>

DynamicArray<std::string> UserService::getWatchlist()
{
	DynamicArray<std::string> v;
	for (int i = 0; i < this->getWatchlistLength(); i++)
	{
		v.add(this->watchlist[i].toString());
	}
	return v;
}

int UserService::getWatchlistLength()
{
	return this->watchlist.getSize();
}

DynamicArray<Movie> UserService::browseByGenre(const std::string& genre)
{
	DynamicArray<Movie> matching_genre;
	if(genre == "")
	{
		for (int i = 0; i < this->repo.getLength(); i++)
		{
			matching_genre.add(this->repo[i]);
		}
	}
	else
	{
		for (int i = 0; i < this->repo.getLength(); i++)
		{
			if (this->repo[i].getGenre() == genre)
			{
				matching_genre.add(this->repo[i]);
			}
		}
	}
	return matching_genre;
}

void UserService::addToWatchlist(const Movie& movie)
{
	//search the movie
	for (int i = 0; i < this->watchlist.getSize(); i++)
	{
		if (this->watchlist[i] == movie)
			throw std::invalid_argument("Movie already in watchlist!");
	}
	//add if not already in watchlist
	this->watchlist.add(movie);
}

void UserService::removeFromWatchlist(const Movie& movie)
{
	//search the movie
	Movie* found = NULL;
	for (int i = 0; i < this->watchlist.getSize(); i++)
	{
		if (this->watchlist[i] == movie)
			found = &this->watchlist[i];
	}
	//remove if found
	if (found != NULL)
		this->watchlist.remove(*found);
	else
		throw std::invalid_argument("Movie not in watchlist!");
}

void UserService::likeMovie(const Movie& movie)
{
	//search the movie in the repo
	for (int i = 0; i < this->repo.getLength(); i++)
	{
		if (this->repo[i] == movie)
		{
			this->repo[i].setLikes(this->repo[i].getLikes() + 1);
			return;
		}
	}
}

void UserService::openLink(const Movie& movie)
{
	//open the link of a movie in browser
	std::string trailer = movie.getTrailer();
	std::string command = "start " + trailer;
	std::system(command.c_str());
}

void testUserService()
{

	Movie movie1("Title1", "Genre1", 2021, 100, "Trailer1");
	Movie movie2("Title2", "Genre2", 2022, 200, "Trailer2");
	DynamicArray<Movie> movies;
	Repository repository(movies);
	UserService userserv(repository);

	//Test addToWatchlist
	userserv.addToWatchlist(movie1);
	userserv.addToWatchlist(movie2);
	try {
		userserv.addToWatchlist(movie1);
	}
	catch (std::invalid_argument&)
	{
		assert(true);
	}

	// Test getWatchlistLength
	assert(userserv.getWatchlistLength() == 2);


	// Test getWatchlist
	DynamicArray<std::string> watchlist = userserv.getWatchlist();

	assert(watchlist[0] == movie1.toString());
	assert(watchlist[1] == movie2.toString());
	assert(watchlist.getSize() == 2);

	// Test browseByGenre
	Movie m1("Titanic", "Drama", 1997, 100, "https://www.imdb.com/title/tt0120338/");
	Movie m2("Inception", "Action", 2010, 150, "https://www.imdb.com/title/tt1375666/");
	Movie m3("The Shawshank Redemption", "Drama", 1994, 142, "https://www.imdb.com/title/tt0111161/");
	repository.addMovie(m1);
	repository.addMovie(m2);
	repository.addMovie(m3);

	DynamicArray<Movie> matching_genre = userserv.browseByGenre("Drama");
	assert(matching_genre.getSize() == 2);

	DynamicArray<Movie> matching_genre2 = userserv.browseByGenre("");
	assert(matching_genre2.getSize() == 3);


	// Test removeFromWatchlist
	userserv.removeFromWatchlist(movie1);
	assert(userserv.getWatchlistLength() == 1);
	try {
		userserv.removeFromWatchlist(movie1);
	}
	catch (std::invalid_argument&)
	{
		assert(true);
	}

	// Test likeMovie
	userserv.likeMovie(m1);
	assert(repository.findMovie(m1)->getLikes() == 101);

	// Test openLink
	userserv.openLink(m1);
}
