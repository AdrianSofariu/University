#include "Movie.h"
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <cassert>


Movie::Movie(std::string title, std::string genre, int year, int likes, std::string trailer): title{title}, genre{genre}, year{year}, likes{likes}, trailer{trailer}
{
	if(year < 0)
		throw std::invalid_argument("Year must be a positive number");
	if(likes < 0)
		throw std::invalid_argument("Likes must be a positive number");
}

Movie::Movie(const Movie& m)
{
    this->title = m.title;
	this->genre = m.genre;
	this->year = m.year;
	this->likes = m.likes;
	this->trailer = m.trailer;
}

void Movie::setTitle(std::string title)
{
	this->title = title;
}

void Movie::setGenre(std::string genre)
{
	this->genre = genre;
}

void Movie::setYear(int year)
{
	if(year < 0)
		throw std::invalid_argument("Year must be a positive number");
	this->year = year;

}

void Movie::setLikes(int likes)
{
	if(likes < 0)
		throw std::invalid_argument("Likes must be a positive number");
	this->likes = likes;
}

void Movie::setTrailer(std::string trailer)
{
	this->trailer = trailer;
}

std::string Movie::toString()
{
	std::stringstream ss;
	ss << "Title: " << this->title << " -- Genre: " << this->genre << " -- Year: " << this->year << " -- Likes: " << this->likes << " -- Trailer: " << this->trailer << std::endl;
	return ss.str();
}

bool Movie::operator==(const Movie& m)
{
	return this->title == m.title;
}

bool Movie::operator!=(const Movie& m)
{
    return !(this->title == m.title);
}

void testMovie()
{
    //Test constructor and copy constructor
    {
        try 
        {
            Movie movie("The Shawshank Redemption", "Drama", -1, 1000, "https://www.youtube.com/watch?v=6hB3S9bIaco");
        }
        catch(const std::invalid_argument& e)
		{
			assert(std::string(e.what()) == "Year must be a positive number");
		}
        try 
        {
			Movie movie("The Shawshank Redemption", "Drama", 1994, -1000, "https://www.youtube.com/watch?v=6hB3S9bIaco");
		}
        catch (const std::invalid_argument& e)
        {
            assert(std::string(e.what()) == "Likes must be a positive number");
        }
        Movie movie("The Shawshank Redemption", "Drama", 1994, 1000, "https://www.youtube.com/watch?v=6hB3S9bIaco");
        Movie movie2 = movie;
        assert(movie == movie2);
    }
    // Test Movie class setters and getters
    {
        Movie movie;
        movie.setTitle("The Shawshank Redemption");
        assert(movie.getTitle() == "The Shawshank Redemption");

        movie.setGenre("Drama");
        assert(movie.getGenre() == "Drama");

        movie.setYear(1994);
        assert(movie.getYear() == 1994);

        movie.setLikes(1000);
        assert(movie.getLikes() == 1000);

        movie.setTrailer("https://www.youtube.com/watch?v=6hB3S9bIaco");
        assert(movie.getTrailer() == "https://www.youtube.com/watch?v=6hB3S9bIaco");
    }

    // Test Movie class toString method
    {
        Movie movie;
        movie.setTitle("The Shawshank Redemption");
        movie.setGenre("Drama");
        movie.setYear(1994);
        movie.setLikes(1000);
        movie.setTrailer("https://www.youtube.com/watch?v=6hB3S9bIaco");

        std::string expectedOutput = "Title: The Shawshank Redemption -- Genre: Drama -- Year: 1994 -- Likes: 1000 -- Trailer: https://www.youtube.com/watch?v=6hB3S9bIaco\n";
        assert(movie.toString() == expectedOutput);
    }

    // Test Movie class equality operator
    {
        Movie movie1;
        movie1.setTitle("The Shawshank Redemption");

        Movie movie2;
        movie2.setTitle("The Shawshank Redemption");

        assert(movie1 == movie2);

        movie2.setTitle("The Godfather");
        assert(movie1 != movie2);
    }

    // Test invalid year and likes values
    {
        Movie movie;

        try
        {
            movie.setYear(-1994);
        }
        catch (const std::invalid_argument& e)
        {
            assert(std::string(e.what()) == "Year must be a positive number");
        }

        try
        {
            movie.setLikes(-1000);
        }
        catch (const std::invalid_argument& e)
        {
            assert(std::string(e.what()) == "Likes must be a positive number");
        }
    }
}



