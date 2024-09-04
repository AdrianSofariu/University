#include "Subject.h"

void Subject::addObserver(Observer* o)
{
	this->obs.push_back(o);
}

void Subject::removeObserver(Observer* o)
{
	auto it = std::find(obs.begin(), obs.end(), o);
	obs.erase(it);
}

void Subject::notify()
{
	for (Observer* observer : obs)
		observer->update();
}
