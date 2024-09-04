#include "HTMLWatchlist.h"
#include "Exceptions.h"
#include <Windows.h>
#include <fstream>
#include <sstream>

void HTMLWatchlist::writeToFile()
{
	std::ofstream f(this->filename);

	if (!f.is_open())
		throw FileException("The file could not be opened!");

	f << "<!DOCTYPE html>\n";
	f << "<html>\n";
	f << "<head>\n";
	f << "<title>Watchlist</title>\n";
	f << "</head>\n";
	f << "<body>\n";
	f << "<table border=\"1\">\n";
	f << "<tr>\n";
	f << "<td>Title</td>\n";
	f << "<td>Genre</td>\n";
	f << "<td>Year</td>\n";
	f << "<td>Likes</td>\n";
	f << "<td>Trailer</td>\n";
	f << "</tr>\n";

	for (auto m : this->movies)
	{
		f << "<tr>\n";
		f << "<td>" << m.getTitle() << "</td>\n";
		f << "<td>" << m.getGenre() << "</td>\n";
		f << "<td>" << m.getYear() << "</td>\n";
		f << "<td>" << m.getLikes() << "</td>\n";
		f << "<td><a href=\"" << m.getTrailer() << "\">Link</a></td>\n";
		f << "</tr>\n";
	}

	f << "</table>\n";
	f << "</body>\n";
	f << "</html>\n";

	f.close();
}

void HTMLWatchlist::displayWatchlist() const
{
	if (this->filename == "")
		throw FileException("The file could not be opened!");
	std::string aux = "C:\\Uni\\OOP\\assignments\\oop-a8-9-AdrianSofariu\\MoviesWithGUI\\" + this->filename;
	ShellExecuteA(NULL, NULL, "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome", aux.c_str(), NULL, SW_SHOWMAXIMIZED);
}

