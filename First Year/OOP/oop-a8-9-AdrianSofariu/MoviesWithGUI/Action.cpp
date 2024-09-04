#include "Action.h"

void AddAction::executeUndo()
{
	this->repo.deleteMovie(this->movie);
}

void AddAction::executeRedo()
{
	this->repo.addMovie(this->movie);
}

void DeleteAction::executeUndo()
{
	this->repo.addMovie(this->movie);
}

void DeleteAction::executeRedo()
{
	this->repo.deleteMovie(this->movie);
}

void UpdateAction::executeUndo()
{
	this->repo.updateMovie(this->new_movie, this->old_movie);
}

void UpdateAction::executeRedo()
{
	this->repo.updateMovie(this->old_movie, this->new_movie);
}
