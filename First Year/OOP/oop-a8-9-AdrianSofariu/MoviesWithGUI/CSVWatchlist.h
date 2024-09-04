#pragma once
#include "FileWatchlist.h"
#include "Exceptions.h"

class CSVWatchlist : public FileWatchlist
{
public:

	//write the watchlist to csv file
	//throws: FileException - if it cannot write
	void writeToFile() override;

	//display the watchlist in Excel
	void displayWatchlist() const override;
};


