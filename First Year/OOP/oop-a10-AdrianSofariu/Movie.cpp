#include "Movie.h"
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <cassert>
#include <vector>
#include "Utils.h"


Movie::Movie(std::string title, std::string genre, int year, int likes, std::string trailer) : title{ title }, genre{ genre }, year{ year }, likes{ likes }, trailer{ trailer } {}

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
    this->year = year;
}

void Movie::setLikes(int likes)
{
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

std::istream& operator>>(std::istream& is, Movie& m)
{
    std::string line;
    std::getline(is, line);

    std::vector<std::string> tokens = tokenize(line, ',');

    if (tokens.size() != 5)
        return is;

    m.title = tokens[0];
    m.genre = tokens[1];
    m.year = std::stoi(tokens[2]);
    m.likes = std::stoi(tokens[3]);
    m.trailer = tokens[4];

    return is;
}

std::ostream& operator<<(std::ostream& os, const Movie& m)
{
    os << m.title << "," << m.genre << "," << m.year << "," << m.likes << "," << m.trailer << std::endl;
    return os;
}

void testMovie()
{
    //Test constructor and copy constructor
    {
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
}




