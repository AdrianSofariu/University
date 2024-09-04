#pragma once
#include "Watchlist.h"

class FileWatchlist: public Watchlist
{
protected:
	std::string filename;

public:
	FileWatchlist() : Watchlist{}, filename{ "" } {};
	FileWatchlist(const std::string& filename) : Watchlist{}, filename { filename } {};
	virtual ~FileWatchlist() {};

	//change the file where the watchlist is stored
	virtual void setFilename(const std::string& filename);

	//write the watchlist to file
	virtual void writeToFile() = 0;

	//display the watchlist
	virtual void displayWatchlist() const = 0;
};

