#pragma once
#include "FileWatchlist.h"

class HTMLWatchlist: public FileWatchlist
{
public:

	//write the watchlist to html file
	//throws: FileException - if it cannot write
	void writeToFile() override;

	//display the watchlist in Excel
	void displayWatchlist() const override;
};

