#include "WatchlistModel.h"
#include "Exceptions.h"


WatchlistModel::WatchlistModel(QObject* parent, const std::vector<Movie>& wlist) : QAbstractTableModel{ parent }
{
	this->watchlist = QVector<Movie>(wlist.begin(), wlist.end());
	if(this->watchlist.isEmpty())
		throw EmptyWatchlistException();
}

int WatchlistModel::rowCount(const QModelIndex& parent) const
{
	return this->watchlist.size();
}

int WatchlistModel::columnCount(const QModelIndex& parent) const
{
	return 5;
}

QVariant WatchlistModel::data(const QModelIndex& index, int role) const
{
	if (!index.isValid())
		return QVariant();

	if (role == Qt::DisplayRole)
	{
		if(index.column() == 0)
			return QString::fromStdString(watchlist[index.row()].getTitle());
		if (index.column() == 1)
			return QString::fromStdString(watchlist[index.row()].getGenre());
		if (index.column() == 2)
			return QString::number(watchlist[index.row()].getYear());
		if (index.column() == 3)
			return QString::number(watchlist[index.row()].getLikes());
		if (index.column() == 4)
			return QString::fromStdString(watchlist[index.row()].getTrailer());
	}
	return QVariant();
}

QVariant WatchlistModel::headerData(int section, Qt::Orientation orientation, int role) const
{
	if (role == Qt::DisplayRole && orientation == Qt::Horizontal)
	{
		switch (section) {
		case 0:
			return QString("Title");
		case 1:
			return QString("Genre");
		case 2:
			return QString("Year");
		case 3:
			return QString("Likes");
		case 4:
			return QString("Trailer");
		}
	}
	return QVariant();
}
