#include "FilterModel.h"
#include <Medication.h>

bool FilterModel::filterAcceptsRow(int sourceRow, const QModelIndex& sourceParent) const
{
	if(this->filter == "")
		return true;

	QModelIndex index0 = sourceModel()->index(sourceRow, 0, sourceParent);
	QString displaystring = sourceModel()->data(index0, Qt::DisplayRole).toString();

	displaystring = displaystring.toLower();

	if (displaystring.contains(this->filter))
		return true;

	return false;
}

void FilterModel::setFilter(const QString& f)
{
	this->filter = f;
	this->filter.toLower();
	this->invalidateFilter();
}
