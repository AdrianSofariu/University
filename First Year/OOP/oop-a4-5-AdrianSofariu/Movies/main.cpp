#include "Movie.h"
#include "Repository.h"
#include "Service.h"
#include "UserService.h"
#include "UserInterface.h"

int main()
{
	//tests
	{
		testMovie();
		testDynamicArray();
		testRepository();
		testService();
		testUserService();
	}

	//run
	{
		DynamicArray<Movie> movies;
		Repository repo{ movies };
		Service service{ repo };
		UserService uservice{ repo };
		UserInterface ui{service, uservice};
		ui.run();
	}

	_CrtDumpMemoryLeaks();
	return 0;
}