#include "MovieValidator.h"
#include "Exceptions.h"

using namespace std;

void MovieValidator::validateMovie(const Movie movie)
{
	vector<string>errors;
	if (movie.getTitle().size() < 1)
		errors.push_back("The title cannot be empty\n");
	if (movie.getGenre().size() < 1)
		errors.push_back("The genre cannot be empty\n");
	if (movie.getYear() < 0)
		errors.push_back("Year must be a positive number\n");
	if (movie.getLikes() < 0)
		errors.push_back("Likes must be a positive number\n");

	// search for "www" or "http" at the beginning of the source string
	size_t posWww = movie.getTrailer().find("www");
	size_t posHttp = movie.getTrailer().find("http");
	if (posWww != 0 && posHttp != 0)
		errors.push_back("The source must start with one of the following strings: \"www\" or \"http\"");

	if (errors.size() > 0)
		throw MovieException(errors);
}
