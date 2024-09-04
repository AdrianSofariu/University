#include "VolunteerWindow.h"
#include <QtWidgets/QApplication>
#include "Repository.h"
#include "Service.h"
#include "Overview.h"

int main(int argc, char *argv[])
{
    Repository repo{ "vols.txt", "deps.txt" };
    Service serv{ repo };

    QApplication a(argc, argv);

    std::vector<VolunteerWindow*> windows;

    for (Department d : repo.getDepartments())
    {
        VolunteerWindow* w = new VolunteerWindow{ d, serv };
        windows.push_back(w);
        repo.addObserver(w);
        w->show();
    }

    Overview* ow = new Overview{ serv };
    repo.addObserver(ow);
    ow->show();

    return a.exec();
}
