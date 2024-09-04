#pragma once
#include "Repository.h"
#include "Exceptions.h"
#include "Movie.h"

class Action
{
public:
	virtual void executeUndo() = 0;
	virtual void executeRedo() = 0;
	virtual ~Action() {};
};

class AddAction : public Action
{
private:
	Repository& repo;
	Movie movie;

public:
	AddAction(Repository& repo, const Movie& movie) : repo{ repo }, movie{ movie } {};
	~AddAction() {};
	void executeUndo() override;
	void executeRedo() override;
};

class DeleteAction : public Action
{
public:
	Repository& repo;
	Movie movie;

	DeleteAction(Repository& repo, const Movie& movie) : repo{ repo }, movie{ movie } {};
	~DeleteAction() {};
	void executeUndo() override;
	void executeRedo() override;
};

class UpdateAction : public Action
{
public:
	Repository& repo;
	Movie old_movie;
	Movie new_movie;

	UpdateAction(Repository& repo, const Movie& movie, const Movie& new_movie) : repo{ repo }, old_movie{ movie }, new_movie{ new_movie } {};
	~UpdateAction() {};
	void executeUndo() override;
	void executeRedo() override;
};