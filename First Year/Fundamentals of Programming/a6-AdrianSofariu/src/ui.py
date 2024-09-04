#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements)
# are found here
#
from functions import *
import copy


def print_menu():
    """
    Procedure to display the menu options
    :return:
    """
    print("This is a monthly bank account app. The following commands are available:")
    print("\tadd <value> <type> <description>")
    print("\tinsert <day> <value> <type> <description>")
    print("\tremove <day>")
    print("\tremove <start day> to <end day>")
    print("\tremove <type>")
    print("\treplace <day> <type> <description> with <value>")
    print("\tlist")
    print("\tlist <type>")
    print("\tlist [ < | = | > ] <value>")
    print("\tlist balance <day>")
    print("\tfilter <type>")
    print("\tfilter <type> <value>")
    print("\tundo")
    print("\texit")


def entrypoint():
    """
    Driver procedure of the UI
    :return:
    """
    print_menu()

    # initialize account
    account = []
    history = []
    to_display = []

    populate_account(account)
    history.append(copy.deepcopy(account))

    while True:
        command = input(">>").strip()
        if " " in command:
            type_of_command, str_params = command.split(" ", maxsplit=1)
            params = str_params.split()
        else:
            type_of_command = command
            params = []
        try:
            # handle the add command here
            if type_of_command == "add":
                add_command(params, account)
                history.append(copy.deepcopy(account))
            # handle the insert command here
            elif type_of_command == "insert":
                insert_command(params, account)
                history.append(copy.deepcopy(account))
            # handle the remove command here
            elif type_of_command == "remove":
                remove_command(params, account)
                history.append(copy.deepcopy(account))
            # handle the replace command here
            elif type_of_command == "replace":
                replace_command(params, account)
                history.append(copy.deepcopy(account))
            # handle the list command here
            elif type_of_command == "list":
                if len(params) == 2:
                    # handle special case when no list needs to be listed
                    if params[0] == 'balance':
                        list_command(params, account)
                    else:
                        to_display = list_command(params, account)
                        display(to_display)
                else:
                    to_display = list_command(params, account)
                    display(to_display)
            # handle the filter command here
            elif type_of_command == "filter":
                filter_command(params, account)
                history.append(copy.deepcopy(account))
            # handle the undo command here
            elif type_of_command == "undo":
                account = undo(history, account)
            # handle the exit command here
            elif type_of_command == "exit":
                break
            else:
                print("Invalid command")
        except ValueError as e:
            print(e)


def add_command(params: list, account: list):
    """
    Procedure to handle the add command
    :param params: parameters of the function add
    :param account: list of transactions
    :return:
    """
    if len(params) == 3:
        add_transaction(int(params[0]), params[1], params[2], account)
    else:
        raise ValueError("Incorrect command")


def insert_command(params: list, account: list):
    """
    Procedure to handle the insert command
    :param params: parameters of the function insert
    :param account: list of transactions
    :return:
    """
    if len(params) == 4:
        insert_transaction(int(params[0]), int(params[1]), params[2], params[3], account)
    else:
        raise ValueError("Incorrect command")


def remove_command(params: list, account: list):
    """
    Procedure to handle the remove command
    :param params: parameters of the function remove
    :param account: list of transactions
    :return:
    """
    if len(params) == 1:
        if params[0].isnumeric():
            remove_day(int(params[0]), account)
        else:
            remove_type(params[0], account)
    elif len(params) == 3 and params[1] == "to":
        remove_day_interval(int(params[0]), int(params[2]), account)
    else:
        raise ValueError("Incorrect command")


def replace_command(params: list, account: list):
    """
    Procedure to handle the replace command
    :param params: parameters of the function replace
    :param account: list of transactions
    :return:
    """
    if params[-2] == "with" and len(params) >= 5:
        desc = ''
        i = 2
        for i in range(2, len(params)-2):
            if i != len(params) - 3:
                desc += params[i] + ' '
            else:
                desc += params[i]
        desc.strip()
        replace_transaction(int(params[0]), params[1], desc, int(params[-1]), account)
    else:
        raise ValueError("Incorrect command")


def list_command(params: list, account: list):
    """
    Procedure to handle the list command
    :param params: parameters of list functions
    :param account: list of transactions
    :return: a list of transactions to display
    """
    if len(params) == 0:
        return account
    elif len(params) == 1:
        return display_type(account, params[0])
    elif len(params) == 2:
        if params[0] == "balance":
            print("Balance of day " + params[1] + " is " + str(compute_balance_day(account, int(params[1]))))
            return []
        elif params[0] in "<=>":
            return display_comparison(account, int(params[1]), params[0])
        else:
            raise ValueError("Incorrect command")
    else:
        raise ValueError("Incorrect command")


def display(to_display: list):
    """
    Procedure to display a list of transactions
    :param to_display: list of transactions
    :return:
    raise ValueError if the list is empty
    """
    if len(to_display) == 0:
        raise ValueError("Nothing to display!")
    else:
        for t in to_display:
            print(display_transaction(t))


def filter_command(params: list, account: list):
    """
    Procedure to handle the filter command
    :param params: parameters of filter functions
    :param account: list of transactions
    :return: a filtered list
    """
    if len(params) == 1:
        filter_type(account, params[0])
    elif len(params) == 2:
        filter_type_value(account, params[0], int(params[1]))
    else:
        raise ValueError("Incorrect command")
