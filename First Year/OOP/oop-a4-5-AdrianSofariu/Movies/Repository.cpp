#include "Repository.h"
#include <stdexcept>

void Repository::addMovie(const Movie& movie)
{
	Movie* found = this->findMovie(movie);
	if (found != NULL)
		throw std::invalid_argument("Movie already exists!");
	this->movies.add(movie);
}

void Repository::deleteMovie(const Movie& movie)
{
	Movie* found = this->findMovie(movie);
	if (found == NULL)
		throw std::invalid_argument("Movie does not exist!");
	this->movies.remove(movie);
}

void Repository::updateMovie(const Movie& movie, const Movie& new_movie)
{
	Movie* found = this->findMovie(movie);
	if (found == NULL)
		throw std::invalid_argument("Movie does not exist!");
	found->setGenre(new_movie.getGenre());
	found->setTrailer(new_movie.getTrailer());
	found->setYear(new_movie.getYear());
	found->setLikes(new_movie.getLikes());

}

Movie* Repository::findMovie(const Movie& movie)
{
	Movie* found = NULL;
	for(int i = 0; i < this->getLength(); i++)
	{
		if (this->movies[i] == movie)
			return &this->movies[i];
	}
	return found;
}

int Repository::getLength() const
{
	return this->movies.getSize();
}

Movie& Repository::operator[](int index)
{
	return this->movies[index];
}

void testRepository()
{
	// Test addMovie
	Movie movie1("Title1", "Genre1", 2021, 100, "Trailer1");
	Movie movie2("Title2", "Genre2", 2022, 200, "Trailer2");
	DynamicArray<Movie> movies;
	Repository repository(movies);
	repository.addMovie(movie1);
	assert(repository.getLength() == 1);
	repository.addMovie(movie2);
	assert(repository.getLength() == 2);
	try
	{
		repository.addMovie(movie1);
	}
	catch (std::invalid_argument& e)
	{
		assert(std::string(e.what()) == "Movie already exists!");
	};

	// Test operator[]
	assert(repository[0].getTitle() == "Title1");

	// Test deleteMovie
	repository.deleteMovie(movie1);
	assert(repository.getLength() == 1);
	try
	{
		repository.deleteMovie(movie1);
	}
	catch (std::invalid_argument& e)
	{
		assert(std::string(e.what()) == "Movie does not exist!");
	};
	repository.deleteMovie(movie2);
	assert(repository.getLength() == 0);

	// Test updateMovie
	Movie movie3("Title3", "Genre3", 2023, 300, "Trailer3");
	repository.addMovie(movie3);
	assert(repository.getLength() == 1);
	Movie newMovie("Title3", "NewGenre", 2024, 400, "NewTrailer");
	repository.updateMovie(movie3, newMovie);
	assert(repository.findMovie(newMovie)->getTitle() == "Title3");
	assert(repository.findMovie(newMovie)->getGenre() == "NewGenre");
	assert(repository.findMovie(newMovie)->getYear() == 2024);
	assert(repository.findMovie(newMovie)->getLikes() == 400);
	assert(repository.findMovie(newMovie)->getTrailer() == "NewTrailer");
}


void testDynamicArray()
{
	// Test constructor
	DynamicArray<int> arr(5);
	assert(arr.getSize() == 0);

	// Test add function & resize
	arr.add(10);
	arr.add(20);
	arr.add(30);
	assert(arr.getSize() == 3);
	assert(arr[0] == 10);
	assert(arr[1] == 20);
	assert(arr[2] == 30);

	// Test remove function
	arr.remove(20);
	assert(arr.getSize() == 2);
	assert(arr[0] == 10);
	assert(arr[1] == 30);

	// Test copy constructor
	DynamicArray<int> arr2(arr);
	assert(arr2.getSize() == 2);
	assert(arr2[0] == 10);
	assert(arr2[1] == 30);

	// Test assignment operator
	DynamicArray<int> arr3 = arr;
	assert(arr3.getSize() == 2);
	assert(arr3[0] == 10);
	assert(arr3[1] == 30);
	arr[0] = 0;
	assert(arr3[0] != arr[0]);

	// Test resize function
	arr3.add(40);
	arr3.add(50);
	arr3.add(60);
	arr3.add(70);
	assert(arr3.getSize() == 6);
	assert(arr3[0] == 10);
	assert(arr3[1] == 30);
	assert(arr3[2] == 40);
	assert(arr3[3] == 50);
	assert(arr3[4] == 60);
}
