from src.domain.expense import Expense


class Service:

    def __init__(self, repo_type):
        self.__repo = repo_type
        self.__repo.generate_random()

    def add_to_repository(self, day: int, amount: int, type: str):
        """
        Method to create and add a new expense to the repository
        :param day: integer between 1 and 30
        :param amount: positive integer
        :param type: string description
        :return:
        """
        expense = Expense(day, amount, type)
        self.__repo.add_entry(expense)

    def get_expenses(self):
        return self.__repo.get_records()

    def filter_above_value(self, value):
        """
        Remove all records with amount <= value
        :param value:
        :return:
        """
        self.__repo.filter(value)

    def repo_undo(self):
        """
        Call the undo operation from the repository
        :return:
        """
        self.__repo.undo()
