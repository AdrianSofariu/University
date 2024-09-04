from colorama import Fore, Style

from src.domain.expense import Expense
from src.services.service import Service


class UI:

    def __init__(self, repo_type):
        self.__serv = Service(repo_type)

    def start(self):
        """
        Driver method for the UI
        :return:
        """
        UI.print_menu()
        while True:
            try:
                command = input(">>")
                UI.validate_command(command)
                self.execute_command(int(command))
            except ValueError as e:
                print(Fore.RED + str(e))
                print(Style.RESET_ALL)

    @staticmethod
    def print_menu():
        print("This app manages a list of expenses.\nThe following commands are available:")
        print("\t1. Add expense")
        print("\t2. Display expenses")
        print("\t3. Filter the list")
        print("\t4. Undo")
        print("\t0. Exit")
        print("Please input the number of your chosen command:")

    @staticmethod
    def validate_command(command: str):
        """
        Method to check if a command is valid (is numeric and 0<=command<=4).
        If invalid, raises ValueError
        :return:
        """
        if command.isdigit():
            if int(command) not in range(0, 5):
                raise ValueError("Unknown command")
        else:
            raise ValueError("Unknown command")

    def execute_command(self, command: int):
        """
        Call appropriate service functions to execute UI commands
        :param command: integer between 0 and 4
        :return:
        """
        if command == 0:
            exit()
        elif command == 1:
            self.add_expense()
        elif command == 2:
            self.display_records()
        elif command == 3:
            self.filter_above()
        elif command == 4:
            self.undo_operation()

    def add_expense(self):
        """
        Method to add a new expense that checks input
        :return:
        raises ValueError if input does not satisfy conditions for an expense-type record
        """
        day = input("Day of the expense: ")
        amount = input("Value of the expense: ")
        type = input("Type of the expense: ")

        # check if day input is ok
        if day.isnumeric():
            Expense.valid_day(int(day))
        else:
            raise ValueError("Day must be numeric")

        # check if amount input is ok
        Expense.valid_amount(int(amount))

        self.__serv.add_to_repository(int(day), int(amount), type)

    def display_records(self):
        """
        Method to display the currently memorised expenses
        :return:
        """
        expenses = self.__serv.get_expenses()
        print("------------------Expenses-----------------")
        for expense in expenses:
            print(str(expense))
        print("-------------------------------------------")

    def filter_above(self):
        """
        Method to filter the records so that it contains only records above a certain value
        :return:
        """
        value = int(input("Keep only records with value above: "))
        if Expense.valid_amount(value):
            self.__serv.filter_above_value(value)

    def undo_operation(self):
        """
        Call the undo operation from service
        :return:
        """
        self.__serv.repo_undo()
