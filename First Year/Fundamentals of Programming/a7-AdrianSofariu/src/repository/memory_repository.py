import copy
import random

from src.domain.expense import Expense


class MemoryRepository:

    def __init__(self):
        self._records = []
        self._history = []
        # self.generate_random()

    def get_records(self):
        return self._records

    def get_history(self):
        return self._history

    def generate_random(self):
        """
        Method to generate 10 random records
        :return:
        """
        types = ["salary", "pocket money", "groceries", "restaurant", "entertainment", "bills"]
        for i in range(10):
            t = Expense(random.randint(1, 30), random.randint(1, 1000), random.choice(types))
            self._records.append(t)

    def add_entry(self, obj):
        """
        Overwrite add method of Repository class
        :param obj: expense record to be added
        :return:
        """
        self.update_history()
        self._records.append(obj)

    def remove_entry(self, obj):
        """
        Overwrite remove method of Repository class
        :param obj: expense record to be removed
        :return:
        """
        self.update_history()
        i = 0
        while i < len(self._records):
            if self._records[i] == obj:
                self._records.pop(i)
            else:
                i += 1

    def remove_by_index(self, index):
        """
        Remove a record by index
        :param index:
        :return:
        """
        self._records.pop(index)

    def update_history(self):
        """
        Procedure that updates the history by adding a deepcopy of the current record
        :return:
        """
        self._history.append(copy.deepcopy(self._records))

    def undo(self):
        """
        Overwrite undo method of Repository class
        :return:
        raises ValueError if there is no operation to undo
        """
        if len(self._history) > 0:
            self._records = self._history.pop()
        else:
            raise ValueError("Undo unavailable")

    def filter(self, value):
        """
        Remove all entries with amount <= value
        :param value:
        :return:
        """
        self.update_history()
        i = 0
        while i < len(self._records):
            if self._records[i].get_amount() <= value:
                self._records.pop(i)
            else:
                i += 1
