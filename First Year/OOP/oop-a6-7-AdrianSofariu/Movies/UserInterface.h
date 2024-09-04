#pragma once
#include "Service.h"
#include "UserService.h"
#include "Exceptions.h"

class UserInterface
{
private:
	Service& serv;
	UserService& userserv;

public:

	//constructor
	UserInterface(Service& service, UserService& userv) :serv{ service }, userserv{userv} {};

	//destructor
	~UserInterface() {}

	//runs the application
	void run();

	//print the user menu
	void printUserMenu();

	//print the admin menu
	void printAdminMenu();

	//Admin CLI
	void adminMode();

	//User CLI
	void userMode();

	//add a movie
	void addMovie();

	//delete a movie
	void deleteMovie();

	//update a movie
	void updateMovie();

	//list all movies
	void listMovies();

	//see watchlist
	void seeWatchlist();

	//save watchlist to file
	void saveWatchlistToFile();

	//delete a movie from watchlist
	//if removal was successful, ask if the user wants to like the movie
	void deleteFromWatchlist();

	//see movies of given genre
	void seeByGenre();
};

