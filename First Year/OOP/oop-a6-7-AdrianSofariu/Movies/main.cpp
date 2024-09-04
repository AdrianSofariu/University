#include "Movie.h"
#include "Repository.h"
#include "TextFileRepository.h"
#include "Service.h"
#include "UserService.h"
#include "UserInterface.h"
#include <iostream>
#include "Exceptions.h"

int main()
{
	//tests
	{
		/*testMovie();
		testRepository();
		testService();
		testUserService();*/
	}

	//run
	{
		try {
			TextFileRepository repo{ "Movies.txt" };

			//user must decide between csv or html
			std::string choice;
			std::cout << "Choose between CSV and HTML playlist: ";
			std::cin >> choice;
			while (choice != "CSV" && choice != "HTML")
			{
				std::cout << "Invalid choice. Choose between CSV and HTML playlist: ";
				std::cin >> choice;
				
			}
			if (choice == "CSV")
			{
				std::cin.clear();
				std::cin.ignore(256, '\n');
				CSVWatchlist watchlist;
				Service service{ repo };
				UserService uservice{ repo, watchlist };
				UserInterface ui{ service, uservice };
				ui.run();
			}	
			else
			{
				std::cin.clear();
				std::cin.ignore(256, '\n');
				HTMLWatchlist watchlist;
				Service service{ repo };
				UserService uservice{ repo, watchlist };
				UserInterface ui{ service, uservice };
				ui.run();
			}
		}
		catch (FileException& e)
		{
			std::cout << e.what();
		}
		
	}

	_CrtDumpMemoryLeaks();
	return 0;
}