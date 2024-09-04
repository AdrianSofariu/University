from src.domain.id_object import IdObject
from src.repository.repository import Repository


class TextFileRepository(Repository):

    def __init__(self, filename: str):
        super().__init__()
        self.__file = filename

    @property
    def filename(self):
        return self.__file

    def add_to_repo(self, obj: IdObject):
        """
        Add new object to the repository by calling super().add_to_repo() and then update binary file
        :param obj: IdObject to be added
        :return:
        raises RepositoryError if object with given id is already in the repo,
        in which case the object is not added
        """
        super().add_to_repo(obj)
        self.update_file()

    def add_no_update(self, obj: IdObject):
        """
        Add new object to the repository by calling super() without updating the file
        :param obj: IdObject to be added
        :return:
        """
        super().add_to_repo(obj)

    def remove(self, _id: int) -> IdObject:
        """
        Remove IdObject with the given id by call to super and then update file
        :param _id:
        :return: the object that was removed
        raises RepositoryError if the object is not in the repository
        """
        obj = super().remove(_id)
        self.update_file()
        return obj

    def update(self, _id: int, new_obj: IdObject):
        """
        Update IdObject with the given id by call to super and then update file
        :param _id:
        :param new_obj: updated version of the IdObject
        :return:
        raises RepositoryError if the object is not in the repository
        """
        super().update(_id, new_obj)
        self.update_file()

    def update_file(self):
        """
        Method to update the content of our file repository
        :return:
        """
        with open(self.__file, 'w') as file:
            for entry in self:
                file.write(str(entry) + "\n")
