#include "UserInterface.h"
#include <iostream>
#include <sstream>
#include <conio.h>
using namespace std;

void UserInterface::run()
{
	while (true)
	{
		cout << endl<<"Welcome to the Local Movie Database!" << endl;
		cout << "1. Admin Mode" << endl;
		cout << "2. User Mode" << endl;
		cout << "3. Exit" << endl;
		cout << "Please choose the mode you would like to use: ";
		int option;
		string input;
		while (getline(cin, input))
		{
			stringstream sstream(input);
			if ((sstream >> option) && sstream.eof())
			{
				if (option == 1)
				{
					this->adminMode();
					break;
				}
				else if (option == 2)
				{
					this->userMode();
					break;
				}
				else if (option == 3)
				{
					cout << "Goodbye!" << endl;
					return;
				}
				else
				{
					cout << "Invalid input. Please enter a valid option." << endl;
				}
			}
			else
			{
				cout << "Invalid input. Please enter a valid option." << endl;
			}
		}
	}
}

void UserInterface::printUserMenu()
{
	cout << endl << "Welcome to the User Menu!" << endl;
	cout << "1. See watch list" << endl;
	cout << "2. Delete a movie from watch list" << endl;
	cout << "3. See movies of given genre" << endl;
	cout << "4. Exit" << endl;
	cout << "Please choose an option: ";
}

void UserInterface::printAdminMenu()
{
	cout<<endl<<"Welcome to the Admin Menu!"<<endl;
	cout<<"1. Add a movie"<<endl;
	cout<<"2. Delete a movie"<<endl;
	cout<<"3. Update a movie"<<endl;
	cout<<"4. List all movies"<<endl;
	cout<<"5. Exit"<<endl;
	cout << "Please choose an option: ";
}

void UserInterface::adminMode()
{
	while (true)
	{
		this->printAdminMenu();
		int option;
		string input;
		try {
			while (getline(cin, input))
			{
				stringstream sstream(input);
				if ((sstream >> option) && sstream.eof())
				{
					if (option == 1)
					{
						this->addMovie();
						break;
					}
					else if (option == 2)
					{
						this->deleteMovie();
						break;
					}
					else if (option == 3)
					{
						this->updateMovie();
						break;
					}
					else if (option == 4)
					{
						this->listMovies();
						break;
					}
					else if (option == 5)
					{
						cout << "Exiting Admin Mode..." << endl;
						return;
					}
					else
					{
						cout << "Invalid input. Please enter a valid option." << endl;
					}
				}
				else
				{
					cout << "Invalid input. Please enter a valid option." << endl;
				}
			}
		}
		catch (exception& e)
		{
			cout << e.what() << endl;
		}
	}
}

void UserInterface::userMode()
{
	while (true)
	{
		this->printUserMenu();
		int option;
		string input;
		try {
			while (getline(cin, input))
			{
				stringstream sstream(input);
				if ((sstream >> option) && sstream.eof())
				{
					if (option == 1)
					{
						this->seeWatchlist();
						break;
					}
					else if (option == 2)
					{
						this->deleteFromWatchlist();
						break;
					}
					else if (option == 3)
					{
						this->seeByGenre();
						break;
					}
					else if (option == 4)
					{
						cout << "Exiting User Mode..." << endl;
						return;
					}
					else
					{
						cout << "Invalid input. Please enter a valid option." << endl;
					}
				}
				else
				{
					cout << "Invalid input. Please enter a valid option." << endl;
				}
			}
		}
		catch (exception& e)
		{
			cout << e.what() << endl;
		}
	}
}

void UserInterface::addMovie()
{
	string input;

	//get title
	cout<<"Please enter the title of the movie: ";
	string title;
	while(getline(cin, title))
	{
		if(title.empty())
		{
			cout<<"Invalid input. Please enter a valid title."<<endl;
		}
		else
		{
			break;
		}
	}

	//get genre
	cout<<"Please enter the genre of the movie: ";
	string genre;
	while (getline(cin, genre))
	{
		if(genre.empty())
		{
			cout<<"Invalid input. Please enter a valid genre."<<endl;
		}
		else
		{
			break;
		}
	}

	//get year
	cout<<"Please enter the year the movie was released: ";
	int year = 0;
	while (getline(cin, input))
	{
		stringstream sstream(input);
		if((sstream >> year) && sstream.eof())
		{
			break;
		}
		else
		{
			cout<<"Invalid input. Please enter a valid year."<<endl;
		}
	}

	//get likes
	cout<<"Please enter the number of likes the movie has: ";
	int likes = 0;
	while (getline(cin, input))
	{
		stringstream sstream(input);
		if((sstream >> likes) && sstream.eof())
		{
			break;
		}
		else
		{
			cout<<"Invalid input. Please enter a valid number of likes."<<endl;
		}
	}

	//get trailer
	cout<<"Please enter the link to the trailer of the movie: ";
	string link;
	while (getline(cin, link))
	{
		if(link.empty())
		{
			cout<<"Invalid input. Please enter a valid link."<<endl;
		}
		else
		{
			break;
		}
	}

	//add movie
	Movie movie = Movie(title, genre, year, likes, link);
	this->serv.addToRepo(movie);
}

void UserInterface::deleteMovie()
{
	string input;
	cout<<"Please enter the title of the movie you would like to delete: ";
	string title;
	while(getline(cin, title))
	{
		if(title.empty())
		{
			cout<<"Invalid input. Please enter a valid title."<<endl;
		}
		else
		{
			break;
		}
	}

	this->serv.removeFromRepo(title);
}

void UserInterface::updateMovie()
{
	string input;

	//get title to identify movie
	cout<<"Please enter the title of the movie you would like to update: ";
	string title;
	while (getline(cin, title))
	{
		if(title.empty())
		{
			cout<<"Invalid input. Please enter a valid title."<<endl;
		}
		else
		{
			break;
		}
	}

	//get new genre
	cout<<"Please enter the new genre of the movie: ";
	string genre;
	while(getline(cin, genre))
	{
		if(genre.empty())
		{
			cout<<"Invalid input. Please enter a valid genre."<<endl;
		}
		else
		{
			break;
		}
	}

	//get new year
	cout<<"Please enter the new year the movie was released: ";
	int year = 0;
	while (getline(cin, input))
	{
		stringstream sstream(input);
		if((sstream >> year) && sstream.eof())
		{
			break;
		}
		else
		{
			cout<<"Invalid input. Please enter a valid year."<<endl;
		}
	}

	//get new likes
	cout<<"Please enter the new number of likes the movie has: ";
	int likes = 0;
	while (getline(cin, input))
	{
		stringstream sstream(input);
		if((sstream >> likes) && sstream.eof())
		{
			break;
		}
		else
		{
			cout<<"Invalid input. Please enter a valid number of likes."<<endl;
		}
	}

	//get new trailer
	cout<<"Please enter the new link to the trailer of the movie: ";
	string link;
	while (getline(cin, link))
	{
		if(link.empty())
		{
			cout<<"Invalid input. Please enter a valid link."<<endl;
		}
		else
		{
			break;
		}
	}

	//update movie
	Movie newMovie = Movie(title, genre, year, likes, link);
	this->serv.updateInRepo(newMovie, title);
}

void UserInterface::listMovies()
{
	DynamicArray<string> movies = this->serv.getRepo();
	for (int i =0; i < this->serv.getRepoLength(); i++)
	{
		cout<<movies[i];
	}
}

void UserInterface::seeWatchlist()
{
	DynamicArray<string> watchlist = this->userserv.getWatchlist();
	if (watchlist.getSize() == 0)
	{
		cout<<"The watchlist is empty."<<endl;
		return;
	}
	else
	{
		for (int i = 0; i < this->userserv.getWatchlistLength(); i++)
		{
			cout << watchlist[i];
		}
	}
}

void UserInterface::deleteFromWatchlist()
{
	string input;
	cout << "Please enter the title of the movie you would like to remove from the watchlist: ";
	string title;
	while (getline(cin, title))
	{
		if (title.empty())
		{
			cout << "Invalid input. Please enter a valid title." << endl;
		}
		else
		{
			break;
		}
	}

	this->userserv.removeFromWatchlist(title);

	//if removal was succesful ask for likes
	cout<<"Would you like to like the movie? (yes/no): ";
	string answer;
	while (getline(cin, answer))
	{
		if (answer == "yes")
		{
			this->userserv.likeMovie(title);
			break;
		}
		else if (answer == "no")
		{
			break;
		}
		else
		{
			cout<<"Invalid input. Please enter a valid answer."<<endl;
		}
	}
}

void UserInterface::seeByGenre()
{
	//read genre
	cout<<"Please enter the genre you would like to see: ";
	string genre;
	getline(cin, genre);

	//get movies
	DynamicArray<Movie> movies = this->userserv.browseByGenre(genre);
	if (movies.getSize() == 0)
	{
		cout<<"No movies of this genre."<<endl;
		return;
	}

	//show movies 1 by 1, while allowing the user to add them to the watchlist or go to the next movie
	//if the last movie is reached, the next is again the first
	int current = 0;
	while (true)
	{
		system("cls");
		cout<<movies[current].toString();
		this->userserv.openLink(movies[current]);
		cout<<"Would you like to add this movie to the watchlist? (yes/no): ";
		string answer;
		while (getline(cin, answer))
		{
			if (answer == "yes")
			{
				try{
					this->userserv.addToWatchlist(movies[current]);
					break;
				}
				catch(exception& e)
				{
					cout<<e.what()<<endl;
					break;
				}
			}
			else if (answer == "no") { break; }
			else
			{
				cout<<"Invalid input. Please enter a valid answer."<<endl;
			}
		}
		//now go to the next movie or break
		cout<<"Would you like to see the next movie? (yes/no): ";
		string answer2;
		while (getline(cin, answer2))
		{
			if (answer2 == "yes")
			{
				current++;
				if (current == movies.getSize())
					current = 0;
				break;
			}
			else if (answer2 == "no")
			{
				return;
			}
			else
			{
				cout<<"Invalid input. Please enter a valid answer."<<endl;
			}
		}
	}
}
