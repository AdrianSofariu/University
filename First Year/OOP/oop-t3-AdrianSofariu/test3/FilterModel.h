#pragma once
#include <qsortfilterproxymodel.h>
#include <string>
#include <qstring.h>

class FilterModel : public QSortFilterProxyModel
{
private:
	QString filter = "";

public:
	FilterModel(QObject* parent = NULL) : QSortFilterProxyModel(parent) {};

	bool filterAcceptsRow(int sourceRow, const QModelIndex& sourceParent) const override;
	void setFilter(const QString& f);
};

