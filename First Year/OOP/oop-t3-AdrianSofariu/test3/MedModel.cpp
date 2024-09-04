#include "MedModel.h"

int MedModel::rowCount(const QModelIndex& parent) const
{
    return this->medications.size();
}

QVariant MedModel::data(const QModelIndex& index, int role) const
{
    int row = index.row();
    if (role == Qt::DisplayRole)
    {
        return QString::fromStdString(this->medications[row].get_category() + "  " + this->medications[row].get_name());
    }

    return QVariant();
}
