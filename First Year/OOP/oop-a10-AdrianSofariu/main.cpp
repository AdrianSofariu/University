#include "MoviesWithGUI.h"
#include <QtWidgets/QApplication>


int main(int argc, char* argv[])
{
    QSizePolicy::Policy::Expanding;
    QApplication a(argc, argv);
    MoviesWithGUI w;
    w.resize(800, 600);
    w.show();
    return a.exec();
}
