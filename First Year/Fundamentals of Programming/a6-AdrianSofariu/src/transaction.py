#
# this file manages the transaction entity
#

def create_transaction(day: int, amount: int, transaction_type: str, description: str) -> dict:
    """
    Function that creates a new transaction represented as a dictionary
    :param day: day of the month between 1 and 30
    :param amount: amount of money, positive integer
    :param transaction_type: type of the transaction (string), can be 'in' or 'out'
    :param description: string that explains details of the transaction
    :return: a dictionary that contains all data from the transaction
    """
    if validate_data(day, transaction_type, amount):
        transaction = {"day": day, "amount of money": amount, "type": transaction_type, "description": description}
        return transaction


def validate_data(day: int, transaction_type: str, amount: int) -> bool:
    """
    Function to validate the data needed to create a new transaction by calling individual validating functions
    for its parameters
    :param day: integer representing the day of the month
    :param transaction_type: string representing the type of the transaction
    :param amount: integer representing the value of the transaction
    :return: true if data is valid
    raises ValueError through the called functions if some data is invalid
    """
    if validate_day(day) and validate_transaction_type(transaction_type) and validate_amount(amount):
        return True


def validate_day(day: int) -> bool:
    """
    Function to check if the day is between 1 and 30
    :param day: integer number
    :return: true if 0 < day < 31
    raises ValueError if the day < 1 or day >  30
    """
    if 0 < day < 31:
        return True
    raise ValueError("Day must be between 1 and 30")


def validate_amount(amount: int) -> bool:
    """
    Function to check if the amount is positive
    :param amount: integer number
    :return: true if the amount is positive
    raises ValueError if the amount is negative
    """
    if amount > 0:
        return True
    raise ValueError("Amount of money must be a positive integer")


def validate_transaction_type(transaction_type: str) -> bool:
    """
    Function to check if the transaction type string is 'in' or 'out'
    :param transaction_type: string representing the type of the transaction
    :return: true if the transaction type = 'in'/'out'
    raises ValueError if the transaction type is some other string
    """
    if transaction_type in ["in", "out"]:
        return True
    raise ValueError("Transaction type must be 'in' or 'out'")


def get_day(transaction: dict) -> int:
    """
    Getter for the day a transaction was made
    :param transaction: a dict representing the transaction
    :return: int, day of the transaction
    """
    return transaction["day"]


def get_amount(transaction: dict) -> int:
    """
    Getter for the amount of money in a transaction
    :param transaction: a dict representing the transaction
    :return: int, amount of money
    """
    return transaction["amount of money"]


def get_type(transaction: dict) -> str:
    """
    Getter for the type of transaction
    :param transaction: a dict representing the transaction
    :return: str, type of transaction, can be 'in' or 'out'
    """
    return transaction["type"]


def get_description(transaction: dict) -> str:
    """
    Getter for the description of a transaction
    :param transaction: a dict representing a transaction
    :return: str, description
    """
    return transaction["description"]


def set_day(day: int, transaction: dict):
    """
    Setter for the day of a transaction
    :param day: integer between 1 and 30
    :param transaction: a dict representing a transaction
    raises ValueError if the day is not valid
    """
    if validate_day(day):
        transaction["day"] = day


def set_amount(amount: int, transaction: dict):
    """
    Setter for the amount of money in a transaction
    :param amount: positive integer
    :param transaction: a dict representing a transaction
    raises ValueError if the amount is negative
    """
    if validate_amount(amount):
        transaction["amount of money"] = amount


def set_type(transaction_type: str, transaction: dict):
    """
    Setter for the type of transaction
    :param transaction_type: str, 'in'/'out'
    :param transaction: a dict representing a transaction
    raises ValueError if type is not 'in' or 'out'
    """
    if validate_transaction_type(transaction_type):
        transaction["type"] = transaction_type


def set_description(description: str, transaction: dict):
    """
    Setter for the description of a transaction
    :param description: a string detailing the transaction
    :param transaction: a dict representing a transaction
    """
    transaction["description"] = description


def display_transaction(transaction: dict) -> str:
    """
    Convert a transaction to a string to display it
    :param transaction:
    :return:
    """
    t_string = "Day: " + str(transaction["day"]) + " Amount: " + str(transaction["amount of money"]) + " "
    t_string += "Type: " + str(transaction["type"]) + " Description: " + str(transaction["description"])
    return t_string
