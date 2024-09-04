from src.repository.memory_repository import MemoryRepository

import pickle


class BinaryFileRepository(MemoryRepository):

    def __init__(self):
        super().__init__()

    def generate_random(self, filename="repository/repo.pkl"):
        """
        Method to generate 10 random records
        :param filename: optional parameter to change used file
        :return:
        """
        with open(filename, 'rb') as file:
            length = 0
            try:
                while True:
                    loaded_data = pickle.load(file)
                    self._records.append(loaded_data)
                    length += 1
            except EOFError:
                if length == 0:
                    super().generate_random()
                    self.update_file()

    def add_entry(self, obj, filename="repository/repo.pkl"):
        """
        Overwrite add method of Repository class
        :param filename: optional parameter to change used file
        :param obj: expense record to be added
        :return:
        """
        super().add_entry(obj)
        self.update_file(filename)

    def remove_entry(self, obj):
        """
        Overwrite remove method of Repository class
        :param obj: expense record to be removed
        :return:
        """
        super().remove_entry(obj)
        self.update_file()

    def remove_by_index(self, index):
        """
        Remove a record by index
        :param index:
        :return:
        """
        super().remove_by_index(index)
        self.update_file()

    def undo(self):
        """
        Overwrite undo method of Repository class
        :return:
        raises ValueError if there is no operation to undo
        """
        super().undo()
        self.update_file()

    def filter(self, value):
        """
        Remove all entries with amount <= value
        :param value:
        :return:
        """
        super().filter(value)
        self.update_file()

    def update_file(self, filename="repository/repo.pkl"):
        """
        Method to update the content of our file repository
        :return:
        """
        with open(filename, 'wb') as file:
            for entry in self._records:
                pickle.dump(entry, file)
