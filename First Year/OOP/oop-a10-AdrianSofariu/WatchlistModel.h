#pragma once
#include <QAbstractTableModel>
#include "Movie.h"
#include <qvector.h>

class WatchlistModel : public QAbstractTableModel
{
	Q_OBJECT
public:
	explicit WatchlistModel(QObject* parent = 0, const std::vector<Movie>& wlist = std::vector<Movie>());

	int rowCount(const QModelIndex& parent = QModelIndex()) const override;
	int columnCount(const QModelIndex& parent = QModelIndex()) const override;
	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
	QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;

private:
	QVector<Movie> watchlist;
};

