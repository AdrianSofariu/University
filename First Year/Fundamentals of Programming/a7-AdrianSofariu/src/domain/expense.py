class Expense:

    def __init__(self, day: int, amount: int, type: str):
        self.__day = day
        self.__amount = amount
        self.__type = type

    def get_day(self) -> int:
        return self.__day

    def get_amount(self) -> int:
        return self.__amount

    def get_type(self) -> str:
        return self.__type

    def set_day(self, new_day: int):
        self.__day = new_day

    def set_amount(self, new_amount: int):
        self.__amount = new_amount

    def set_type(self, new_type: str):
        self.__type = new_type

    def __str__(self) -> str:
        """
        Overwritten str() procedure to display the expense object
        :return: string representing an expense object
        """
        return "Day: " + str(self.get_day()) + " Amount: " + str(self.get_amount()) + " Type: " + str(self.get_type())

    def __eq__(self, other):
        """
        Overwritten eq() procedure to check if two expense objects are identical
        :param other: expense to compare with
        :return:
        """
        if self.get_amount() == other.get_amount() and self.get_type() == other.get_type() and self.get_day() == other.get_day():
            return True
        return False

    @staticmethod
    def valid_day(day: int):
        """
        Procedure to check if a number can be a day field
        :param day: integer to be checked
        :return:
        raises ValueError if day < 1 or if day > 30
        """
        if day < 1 or day > 30:
            raise ValueError("Day must be an integer between 1 and 30")
        return True

    @staticmethod
    def valid_amount(amount: int):
        """
        Procedure to check if a number can be an amount field
        :param amount: integer to be checked
        :return:
        raises ValueError if number <= 0
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive integer")
        return True
