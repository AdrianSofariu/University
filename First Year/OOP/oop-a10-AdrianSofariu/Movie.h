#pragma once
#include <string>

class Movie
{
private:
	std::string title;
	std::string genre;
	int year;
	int likes;
	std::string trailer;

public:

	// Constructors
	Movie(std::string title = "", std::string genre = "", int year = 0, int likes = 0, std::string trailer = "");

	// Copy constructor
	Movie(const Movie& m);

	// Destructor
	~Movie() {};

	// Getters
	std::string getTitle() const { return this->title; }
	std::string getGenre() const { return this->genre; }
	int getYear() const { return this->year; }
	int getLikes() const { return this->likes; }
	std::string getTrailer() const { return this->trailer; }

	// Setters
	void setTitle(std::string title);
	void setGenre(std::string genre);
	void setYear(int year);
	void setLikes(int likes);
	void setTrailer(std::string trailer);

	//To string
	std::string toString();

	// Overloading the equality operator
	bool operator==(const Movie& m);
	bool operator!=(const Movie& m);

	friend std::istream& operator>>(std::istream& is, Movie& m);
	friend std::ostream& operator<<(std::ostream& os, const Movie& m);

};

//testing
void testMovie();

