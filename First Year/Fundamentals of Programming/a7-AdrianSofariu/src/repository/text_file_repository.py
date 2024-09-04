from src.domain.expense import Expense
from src.repository.memory_repository import MemoryRepository


class TextFileRepository(MemoryRepository):

    def __init__(self):
        super().__init__()

    def generate_random(self, filename="repository/repo.txt"):
        """
        Method to generate 10 random records in a file
        :return:
        """
        with open(filename, 'r') as file:
            content = file.read()
            if len(content) == 0:
                super().generate_random()
                self.update_file()
            else:
                self.update_record(content.strip("\n"))

    def update_record(self, content: str):
        """
        Method to create expense-objects from file content
        :param content:
        :return:
        """
        expenses = content.split("\n")
        for expense in expenses:
            params = expense.split(" ")
            obj = Expense(int(params[1]), int(params[3]), params[5])
            self._records.append(obj)

    def add_entry(self, obj, filename="repository/repo.txt"):
        """
        Overwrite add method of Repository class
        :param filename: optional parameter to use a different file
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

    def update_file(self, filename="repository/repo.txt"):
        """
        Method to update the content of our file repository
        :return:
        """
        with open(filename, 'w') as file:
            for entry in self._records:
                file.write(str(entry) + "\n")
