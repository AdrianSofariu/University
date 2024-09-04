#include "test3.h"
#include <QtWidgets/QApplication>
#include "Repository.h"
#include "Service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
	Repository repo{"data.txt"};
	Service serv{ repo };
    test3 w{ serv };
    w.show();
    return a.exec();
}
