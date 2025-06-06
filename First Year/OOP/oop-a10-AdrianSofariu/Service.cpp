#include "Service.h"
#include <assert.h>

void Service::addToRepo(const Movie& movie)
{
	MovieValidator::validateMovie(movie);
	this->repo.addMovie(movie);
	std::unique_ptr<Action> action = std::make_unique<AddAction>(this->repo, movie);
	this->undoStack.push(std::move(action));
	while (!this->redoStack.empty())
		this->redoStack.pop();
}

void Service::removeFromRepo(const std::string& title)
{
	Movie aux = this->repo.findMovieByTitle(title);
	this->repo.deleteMovie(aux);
	std::unique_ptr<Action> action = std::make_unique<DeleteAction>(this->repo, aux);
	this->undoStack.push(std::move(action));
	while (!this->redoStack.empty())
		this->redoStack.pop();
}

void Service::updateInRepo(const Movie& newMovie, const std::string& title)
{
	MovieValidator::validateMovie(newMovie);
	Movie aux = this->repo.findMovieByTitle(title);
	this->repo.updateMovie(aux, newMovie);
	std::unique_ptr<Action> action = std::make_unique<UpdateAction>(this->repo, aux, newMovie);
	this->undoStack.push(std::move(action));
	while (!this->redoStack.empty())
		this->redoStack.pop();
}

Movie* Service::findInRepo(const std::string& title)
{
	Movie aux(title);
	return this->repo.findMovie(aux);
}

void Service::initRepo()
{
	//initializing the repository with 10 movies
	Movie m1("Titanic", "Drama", 1997, 100, "https://www.imdb.com/title/tt0120338/");
	Movie m2("Inception", "Action", 2010, 150, "https://www.imdb.com/title/tt1375666/");
	Movie m3("The Shawshank Redemption", "Drama", 1994, 142, "https://www.imdb.com/title/tt0111161/");
	Movie m4("The Godfather", "Crime", 1972, 175, "https://www.imdb.com/title/tt0068646/");
	Movie m5("The Dark Knight", "Action", 2008, 152, "https://www.imdb.com/title/tt0468569/");
	Movie m6("The Lord of the Rings: The Return of the King", "Adventure", 2003, 201, "https://www.imdb.com/title/tt0167260/");
	Movie m7("The Matrix", "Action", 1999, 136, "https://www.imdb.com/title/tt0133093/");
	Movie m8("The Lion King", "Animation", 1994, 88, "https://www.imdb.com/title/tt0110357/");
	Movie m9("Avatar: The Last Airbender", "Animation", 2005, 23, "https://www.imdb.com/title/tt0417299/");
	Movie m10("Rogue One: A Star Wars Story", "Action", 2016, 133, "https://www.imdb.com/title/tt3748528/");

	this->repo.addMovie(m1);
	this->repo.addMovie(m2);
	this->repo.addMovie(m3);
	this->repo.addMovie(m4);
	this->repo.addMovie(m5);
	this->repo.addMovie(m6);
	this->repo.addMovie(m7);
	this->repo.addMovie(m8);
	this->repo.addMovie(m9);
	this->repo.addMovie(m10);
}



int Service::getRepoLength() const
{
	return this->repo.getLength();
}

std::vector<std::string> Service::getRepo()
{
	std::vector<std::string> v;
	for (Movie m : this->repo.getRepo())
	{
		v.push_back(m.toString());
	}
	return v;
}

void Service::undo()
{
	if (this->undoStack.empty())
		throw UndoException();
	this->undoStack.top().get()->executeUndo();
	this->redoStack.push(std::move(this->undoStack.top()));
	this->undoStack.pop();
}

void Service::redo()
{
	if (this->redoStack.empty())
		throw RedoException();
	this->redoStack.top().get()->executeRedo();
	this->undoStack.push(std::move(this->redoStack.top()));
	this->redoStack.pop();
}

void testService()
{
	Repository r;
	Service serv{ r };
	Movie m1("Titanic", "Drama", 1997, 100, "https://www.imdb.com/title/tt0120338/");
	Movie m2("Inception", "Action", 2010, 150, "https://www.imdb.com/title/tt1375666/");
	Movie m3("The Shawshank Redemption", "Drama", 1994, 142, "https://www.imdb.com/title/tt0111161/");

	//test add
	serv.addToRepo(m1);
	serv.addToRepo(m2);
	serv.addToRepo(m3);
	assert(serv.getRepoLength() == 3);

	//test get repo
	std::vector<std::string> v = serv.getRepo();
	assert(v[0] == "Title: Titanic -- Genre: Drama -- Year: 1997 -- Likes: 100 -- Trailer: https://www.imdb.com/title/tt0120338/\n");

	//test remove
	serv.removeFromRepo("Titanic");
	assert(serv.getRepoLength() == 2);

	//test update
	Movie m4("Inception", "Drama", 2012, 30, "https://www.imdb.com/title/tt0111161/");
	serv.updateInRepo(m4, "Inception");
	assert(serv.getRepoLength() == 2);
	Movie* m = serv.findInRepo("Inception");
	assert(m->getYear() == 2012);
	assert(m->getLikes() == 30);
	assert(m->getTrailer() == "https://www.imdb.com/title/tt0111161/");
	assert(m->getGenre() == "Drama");

	//test init repo
	Repository reposit;
	Repository watchls;
	Service service{ reposit };
	service.initRepo();
	assert(service.getRepoLength() == 10);
}

