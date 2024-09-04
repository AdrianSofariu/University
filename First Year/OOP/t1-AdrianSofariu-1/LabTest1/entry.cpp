#include "UI.h"

int main()
{
	Repository::testAdd();
	Service::testGetByString();

	Repository repo;
	Service serv = Service(repo);
	serv.initRepo();
	UI user_interface = UI(serv);


	user_interface.run();
	return 0;
}