#include "CSVWatchlist.h"
#include <fstream>
#include <Windows.h>

void CSVWatchlist::writeToFile()
{
	std::ofstream f{ this->filename };

	if (!f.is_open())
		throw FileException("The file could not be opened!");

	for (auto m : this->movies)
		f << m.getTitle() << "," << m.getGenre() << "," << m.getYear() << "," << m.getLikes() << "," << m.getTrailer() << "\n";

	f.close();
}

void CSVWatchlist::displayWatchlist() const
{
	if (this->filename == "")
		throw FileException("The file is not set!");
	std::string aux = "\"" + this->filename + "\""; // if the path contains spaces, we must put it inside quotations
	ShellExecuteA(NULL, NULL, "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel", aux.c_str(), NULL, SW_SHOWMAXIMIZED);
}

