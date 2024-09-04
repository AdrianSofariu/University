from src.domain.errors import RepositoryError
from src.domain.id_object import IdObject


class RepositoryIterator:
    """
    this class is used to navigate the repository
    """
    def __init__(self, data: list):
        self._data = data
        self._pos = -1

    def __next__(self):
        # return the next item we iterate over
        self._pos += 1
        if self._pos == len(self._data):
            raise StopIteration()
        return self._data[self._pos]


class Repository:
    """
    this class manages the entities in our app by storing them in a memory dict
    """
    def __init__(self):
        self._data = {}

    def add_to_repo(self, obj: IdObject):
        """
        Add new object to the repository
        :param obj: IdObject to be added
        :return:
        raises RepositoryError if object with given id is already in the repo,
        in which case the object is not added
        """

        if not isinstance(obj, IdObject):
            raise TypeError("Can only add IdObject instances")

        if obj.id in self._data.keys():
            raise RepositoryError("Object already exists")

        self._data[obj.id] = obj

    def remove(self, _id: int) -> IdObject:
        """
        Remove IdObject with the given id
        :param _id:
        :return: the object that was removed
        raises RepositoryError if the object is not in the repository
        """
        if self.find(_id) is None:
            raise RepositoryError("Object doesn't exist.")
        return self._data.pop(_id)

    def update(self, _id: int, new_obj: IdObject):
        """
        Update IdObject with the given id
        :param _id:
        :param new_obj: updated version of the IdObject
        :return:
        raises RepositoryError if the object is not in the repository
        """
        if self.find(_id) is None:
            raise RepositoryError("Object doesn't exist.")
        else:
            self.remove(_id)
            self.add_to_repo(new_obj)

    def find(self, _id: int) -> IdObject | None:
        """
        Find the object with given id
        :param _id:
        :return: IdObject instance, or None if object with given id was not found
        """

        if _id in self._data.keys():
            return self._data[_id]
        else:
            return None

    def list_records(self) -> list:
        """
        List all records in the repository in string form
        :return:
        """
        records = []
        for record in self._data.values():
            records.append(str(record))
        if len(records) == 0:
            raise RepositoryError("No records found")
        else:
            return records

    def __iter__(self):
        """
        This is the Iterator design pattern
        """
        return RepositoryIterator(list(self._data.values()))

    def __getitem__(self, item):
        """
        Get item from the repository
        :param item:
        :return: IdObject if it exists in the repository, None else
        """
        if item not in self._data:
            return None
        return self._data[item]

    def __len__(self):
        """
        Return the number of objects in the repository
        :return:
        """
        return len(self._data)
