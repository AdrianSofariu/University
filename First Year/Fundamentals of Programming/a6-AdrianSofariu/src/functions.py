#
# The program's functions are implemented here. There is no user interaction in this file,
# therefore no input/print statements. Functions here communicate via function parameters,
# the return statement and raising of exceptions.
#
import copy
import datetime
import operator
import random

from transaction import *


def add_transaction(value: int, transaction_type: str, description: str, account: list):
    """
    Add a transaction with the current day to our account
    :param value: amount of money integer
    :param transaction_type: type of transaction ("in"/"out")
    :param description: string description of the transaction
    :param account: list that represents the account
    :return:
    """
    transaction = create_transaction(datetime.datetime.now().day, value, transaction_type, description)
    account.append(transaction)


def insert_transaction(day: int, value: int, transaction_type: str, description: str, account: list):
    """
    Insert a transaction with a given day to our account
    :param day: integer day between 1 and 30
    :param value: amount of money integer
    :param transaction_type: type of transaction ("in"/"out")
    :param description: string description of the transaction
    :param account: list that represents the account
    :return:
    """
    transaction = create_transaction(day, value, transaction_type, description)
    account.append(transaction)


def remove_day(day: int, account:  list):
    """
    Remove all transactions from a valid day
    :param day: day to remove transactions from
    :param account: list of transactions
    :return:
    """
    if validate_day(day):
        i = 0
        while i < len(account):
            if get_day(account[i]) == day:
                account.pop(i)
            else:
                i += 1


def remove_day_interval(start_day: int, end_day: int, account: list):
    """
    Remove all transaction in the given interval of days
    :param start_day: start day of the interval
    :param end_day: end day of the interval
    :param account: list of transactions
    :return:
    Raise ValueError if end day is smaller than start day
    """
    if validate_day(start_day) and validate_day(end_day):
        if start_day > end_day:
            raise ValueError("Start day must be smaller than end day")
        else:
            for day in range(start_day, end_day + 1):
                remove_day(day, account)


def remove_type(transaction_type: str, account: list):
    """
    Remove all in/out transactions
    :param transaction_type: type of transaction = in/out
    :param account: list of transactions
    :return:
    """
    if validate_transaction_type(transaction_type):
        i = 0
        while i < len(account):
            if get_type(account[i]) == transaction_type:
                account.pop(i)
            else:
                i += 1


def replace_transaction(day: int, transaction_type: str, description: str, amount: int, account: list):
    """
    Replace the value of a transaction defined by day, type and description with given amount
    :param account: list of transactions
    :param day: day of the transaction we are replacing
    :param transaction_type: type of the transaction we are replacing = in/out
    :param description: description of the transaction we are replacing
    :param amount: new amount
    :return:
    raises ValueError if transaction is not found
    """
    found = False
    if validate_data(day, transaction_type, amount):
        for i in range(len(account)):
            if get_day(account[i]) == day and get_type(account[i]) == transaction_type and get_description(account[i]) == description:
                set_amount(amount, account[i])
                found = True
    if not found:
        raise ValueError("Transaction not found!")


def display_type(account: list, transaction_type: str) -> list:
    """
    Display all transactions of a certain type
    :param account: list of transactions
    :param transaction_type: type = in/out
    :return: list with transactions containing all transactions of a certain type
    """
    to_display = []
    if validate_transaction_type(transaction_type):
        for transaction in account:
            if get_type(transaction) == transaction_type:
                to_display.append(transaction)
    return to_display


def display_comparison(account: list, amount: int, comparator: str) -> list:
    """
    Display all transactions where the value comparator(<, =, >) to a given amount
    :param account: list of transactions
    :param amount: value to compare to
    :param comparator: < , = , >
    :return: list with transactions satisfying the comparison condition
    """
    ops = {
        '<': operator.lt,
        '=': operator.eq,
        '>': operator.gt,
    }

    to_display = []
    if validate_amount(amount):
        for transaction in account:
            if ops[comparator](get_amount(transaction), amount):
                to_display.append(transaction)
    return to_display


def compute_balance_day(account: list, day: int) -> int:
    """
    Compute the balance of a day (sum of in transactions - sum of out transactions)
    :param account: list of transactions
    :param day: day to compute the balance
    :return: integer representing the balance
    """
    balance = 0
    if validate_day(day):
        for transaction in account:
            if get_day(transaction) <= day:
                if get_type(transaction) == 'in':
                    balance += get_amount(transaction)
                else:
                    balance -= get_amount(transaction)
    return balance


def filter_type(account: list, transaction_type: str):
    """
    Filter the transactions by type
    :param account: list of transactions
    :param transaction_type: type of transaction = in/out
    :return:
    """
    if validate_transaction_type(transaction_type):
        i = 0
        while i < len(account):
            if get_type(account[i]) != transaction_type:
                account.pop(i)
            else:
                i += 1


def filter_type_value(account: list, transaction_type: str, value: int):
    """
    Filter the transactions by type and with an amount < value
    :param account: list of transactions
    :param transaction_type: type of transaction = in/out
    :param value: value of transaction
    :return:
    """
    if validate_transaction_type(transaction_type) and validate_amount(value):
        i = 0
        while i < len(account):
            if get_type(account[i]) != transaction_type or get_amount(account[i]) > value:
                account.pop(i)
            else:
                i += 1


def undo(history: list, current: list):
    """
    Function to handle the undo action
    :param history: list with all previous iterations of the account list
    :param current: account list that is currently used
    :return: new value of the current account
    raises ValueError if we get to the original list
    """
    if len(history) > 1:
        history.pop()
        return copy.deepcopy(history[-1])
    else:
        raise ValueError("Undo unavailable")


def populate_account(account: list):
    types = ["in", "out"]
    descriptions = ["salary", "pocket money", "groceries", "restaurant", "entertainment", "dividends"]
    for i in range(10):
        t = create_transaction(random.randint(1, 30), random.randint(1, 1000),
                               random.choice(types), random.choice(descriptions))
        account.append(t)


def test_add():
    account = []
    add_transaction(1000, 'in', 'salary', account)
    add_transaction(2000, 'out', 'gift', account)
    transaction = create_transaction(datetime.datetime.now().day, 1000, 'in', 'salary')
    transaction2 = create_transaction(datetime.datetime.now().day, 2000, 'out', 'gift')
    assert transaction in account
    assert transaction2 in account


def test_insert():
    account = []
    insert_transaction(10, 1000, 'in', 'salary', account)
    insert_transaction(10, 2000, 'out', 'gift', account)
    transaction = create_transaction(10, 1000, 'in', 'salary')
    transaction2 = create_transaction(10, 2000, 'out', 'gift')
    assert transaction in account
    assert transaction2 in account


def test_remove_day():
    account = []
    transaction = create_transaction(10, 1000, 'in', 'salary')
    transaction2 = create_transaction(10, 2000, 'out', 'gift')
    account.append(transaction)
    account.append(transaction2)
    remove_day(10, account)
    assert transaction not in account
    assert transaction2 not in account


def test_remove_type():
    account = []
    transaction = create_transaction(10, 1000, 'in', 'salary')
    transaction2 = create_transaction(11, 2000, 'out', 'gift')
    transaction3 = create_transaction(13, 2000, 'in', 'dividend')
    account.append(transaction)
    account.append(transaction2)
    account.append(transaction3)
    remove_type('in', account)
    assert transaction not in account
    assert transaction2 in account
    assert transaction3 not in account


def test_remove_day_interval():
    account = []
    transaction = create_transaction(10, 1000, 'in', 'salary')
    transaction2 = create_transaction(11, 2000, 'out', 'gift')
    transaction3 = create_transaction(9, 2000, 'out', 'dividend')
    account.append(transaction)
    account.append(transaction2)
    account.append(transaction3)
    remove_day_interval(9, 10, account)
    assert transaction not in account
    assert transaction2 in account
    assert transaction3 not in account


def test_replace():
    account = []
    transaction = create_transaction(10, 1000, 'in', 'salary')
    new_transaction = create_transaction(10, 1000, 'in', 'salary')
    account.append(transaction)
    replace_transaction(10, 'in', 'salary', 2000, account)
    assert transaction in account
    assert new_transaction not in account
