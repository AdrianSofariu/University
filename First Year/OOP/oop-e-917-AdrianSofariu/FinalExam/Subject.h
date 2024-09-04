#pragma once
#include "Observer.h"
#include <vector>

class Subject
{
private:
	std::vector<Observer*> obs;

public:
	void addObserver(Observer* o);
	void removeObserver(Observer* o);
	void notify();

};

