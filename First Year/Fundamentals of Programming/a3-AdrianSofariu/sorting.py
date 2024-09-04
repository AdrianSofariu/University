import random
from texttable import Texttable
import timeit


def generate_random_list(mylist: list):
    """
    Generate a list with random integers
    :param mylist:
    :return:
    """
    try:
        list_length = int(input("How long should the list be?\n>>>"))
        mylist.clear()
        for i in range(0, list_length):
            mylist.append(random.randint(0, 100))
        print("The list is: ", mylist)
    except ValueError:
        print("Invalid number!")


def generate_random_list_no_input(mylist: list, length: int):
    mylist.clear()
    for i in range(length):
        mylist.append(random.randint(0, 100))


def get_step() -> int:
    """
    Request the step for printing the list while sorting
    :return: step
    """
    try:
        step = int(input("Please provide the step\n>>>"))
        if step < 0:
            print("Step must be >= 0")
            raise ValueError
        return step
    except ValueError:
        print("Invalid step!")


def merge_lists(l1: list, l2: list) -> list:
    """
    Merge two sorted lists
    :param l1:
    :param l2:
    :return: A sorted list built from l1 and l2
    """
    merged = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            merged.append(l1[0])
            l1.pop(0)
        else:
            merged.append(l2[0])
            l2.pop(0)
    merged += l1
    merged += l2
    return merged


def copy_list(original: list, copy: list):
    copy.clear()
    for element in original:
        copy.append(element)


def insertion_sort(mylist: list, step: int):
    """
    Sort the list using insertion sort
    :param mylist:
    :param step:
    :return:
    """

    # prepare counter and step number
    counter = step - 1
    stepcount = 1

    print("The initial list is: ", mylist)

    # sort the list
    for i in range(1, len(mylist)):
        key = mylist[i]
        j = i - 1
        while j >= 0 and key < mylist[j]:

            mylist[j + 1] = mylist[j]
            j -= 1
        mylist[j + 1] = key
        # manage printing by tracking swaps
        counter += 1
        if counter == step and step != 0:
            counter = 0
            print("Step", stepcount, ": ", mylist)
            stepcount += step
    print("The sorted list is:", mylist, "\n")


def strand_sort(mylist: list, step: int):
    """
    Sort the list using strand sort
    :param mylist:
    :param step:
    :return:
    """

    # prepare counter and step number
    counter = step - 1
    stepcount = 1

    print("The initial list is: ", mylist)

    # sort the list
    output = []
    sub = []

    while len(mylist):
        # insert first element into sublist
        sub.clear()
        sub.append(mylist[0])
        mylist.pop(0)
        # go through the list and append all numbers bigger than the first one of the sublist
        sublist_index = 0
        index = 0
        while index < len(mylist):
            if mylist[index] > sub[sublist_index]:
                sub.append(mylist[index])
                mylist.pop(index)
                sublist_index += 1
            else:
                index += 1

        # print the sublist and original list before merging
        counter += 1
        if counter == step and step != 0:
            print("Step", stepcount, "\noriginal list: ", mylist, "sublist: ", sub)

        # merge the sublist and the output
        output = merge_lists(output, sub)

        # manage printing by tracking steps
        if counter == step and step != 0:
            counter = 0
            stepcount += step
            print("output: ", output, "\n")

    # display final result while moving the output in the original list
    copy_list(output, mylist)
    print("The sorted list is:", mylist, "\n")


def strand_subroutine(mylist: list):
    # if list is empty, create a new one
    if not mylist:
        print("The list is empty. Please provide the desired length to create a new list.\n")
        generate_random_list(mylist)
    step = get_step()
    strand_sort(mylist, step)


def insertion_subroutine(mylist: list):
    # if list is empty, create a new one
    if not mylist:
        print("The list is empty. Please provide the desired length to create a new list.\n")
        generate_random_list(mylist)
    step = get_step()
    insertion_sort(mylist, step)


def insertion_sort_no_print(mylist: list):
    # time complexity: O(n^2)
    # BC: O(n)
    # WC and AC: O(n^2)
    # space: O(1)
    for i in range(1, len(mylist)):
        key = mylist[i]
        j = i - 1
        while j >= 0 and key < mylist[j]:

            mylist[j + 1] = mylist[j]
            j -= 1
        mylist[j + 1] = key


def strand_sort_no_print(mylist: list):
    # time complexity: O(n^2)
    # BC: O(n)
    # WC and AC: O(n^2)
    # space: O(n)
    output = []
    sub = []

    while len(mylist) != 0:
        # insert first element into sublist
        sub.clear()
        sub.append(mylist[0])
        mylist.pop(0)
        # go through the list and append all numbers bigger than the first one of the sublist
        sublist_index = 0
        index = 0
        while index < len(mylist):
            if mylist[index] >= sub[sublist_index]:
                sub.append(mylist[index])
                mylist.pop(index)
                sublist_index += 1
            else:
                index += 1
        output = merge_lists(output, sub)


def best_case():

    list1 = []
    list1_copy = []
    values = [1000, 2000, 4000, 8000, 16000]

    table = Texttable()
    table.add_row(['Term', 'Insertion Sort', 'Strand Sort'])

    for value in values:

        # generate a sorted list and copy it
        generate_random_list_no_input(list1, value)
        list1.sort()
        copy_list(list1, list1_copy)

        # start insertion sort and time it
        start_ins = timeit.default_timer()
        insertion_sort_no_print(list1)
        end_ins = timeit.default_timer()

        # start strand sort and time it
        start_str = timeit.default_timer()
        strand_sort_no_print(list1_copy)
        end_str = timeit.default_timer()

        table.add_row([value, end_ins - start_ins, end_str - start_str])
    print(table.draw())


def average_case():

    list1 = []
    list1_copy = []
    values = [1000, 2000, 4000, 8000, 16000]

    table = Texttable()
    table.add_row(['Term', 'Insertion Sort', 'Strand Sort'])

    for value in values:
        # generate a random list and copy it
        generate_random_list_no_input(list1, value)
        copy_list(list1, list1_copy)

        # start insertion sort and time it
        start_ins = timeit.default_timer()
        insertion_sort_no_print(list1)
        end_ins = timeit.default_timer()

        # start strand sort and time it
        start_str = timeit.default_timer()
        strand_sort_no_print(list1_copy)
        end_str = timeit.default_timer()

        table.add_row([value, end_ins - start_ins, end_str - start_str])
    print(table.draw())


def worst_case():

    list1 = []
    list1_copy = []
    values = [1000, 2000, 4000, 8000, 16000]

    table = Texttable()
    table.add_row(['Term', 'Insertion Sort', 'Strand Sort'])

    for value in values:
        # generate a list sorted in reverse and copy it
        generate_random_list_no_input(list1, value)
        list1.sort(reverse=True)
        copy_list(list1, list1_copy)

        # start insertion sort and time it
        start_ins = timeit.default_timer()
        insertion_sort_no_print(list1)
        end_ins = timeit.default_timer()

        # start strand sort and time it
        start_str = timeit.default_timer()
        strand_sort_no_print(list1_copy)
        end_str = timeit.default_timer()

        table.add_row([value, end_ins - start_ins, end_str - start_str])
    print(table.draw())


def print_menu():
    """
        Prints the app menu
        :param:
        :return:
    """
    mylist = []
    menu_text = ("1. Generate list\n2. Sort list using Insertion Sort\n3. Sort list using Strand Sort \n"
                 "4. Best case\n5. Average case\n6. Worst case\n7. Exit")
    while True:
        print(menu_text)
        option = input(">>>")
        try:
            option = int(option.strip())
            if option == 1:
                generate_random_list(mylist)
            elif option == 2:
                insertion_subroutine(mylist)
            elif option == 3:
                strand_subroutine(mylist)
            elif option == 4:
                best_case()
            elif option == 5:
                average_case()
            elif option == 6:
                worst_case()
            elif option == 7:
                break
            else:
                print("Invalid command")
        except ValueError:
            print("Invalid command")


if __name__ == "__main__":
    print_menu()
