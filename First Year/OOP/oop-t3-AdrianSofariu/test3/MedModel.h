#pragma once
#include <qabstractlistmodel>
#include "Medication.h"

class MedModel : public QAbstractListModel
{
private:
	std::vector<Medication> medications;

public:
	MedModel(std::vector<Medication> medications) : medications{ medications } {};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override;
	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
};

