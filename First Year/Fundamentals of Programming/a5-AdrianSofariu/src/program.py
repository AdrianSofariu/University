#
# Write the implementation for A5 in this file
#
import random

#
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def create_complex_number(a: int, b: int) -> list:
    """
    Create a complex number as a list with 2 elements: real part and imaginary part
    :param a: real part
    :param b: imaginary part
    :return: complex number as list
    """
    number = [a, b]
    return number


def get_real_part(number: list) -> int:
    """
    Returns real part of a complex number stored as a list
    :param number: complex number as list
    :return: real part
    """
    return number[0]


def get_img_part(number: list) -> int:
    """
    Returns imaginary part of a complex number stored as a list
    :param number: complex number as list
    :return: imaginary part
    """
    return number[1]


def set_real_part(number: list, a: int):
    """
    Set real part of a complex number stored as a list
    :param number: complex number as list
    :param a: new real part
    """
    number[0] = a


def set_img_part(number: list, b: int):
    """
    Set imaginary part of a complex number stored as a list
    :param number: complex number as list
    :param b: new imaginary part
    """
    number[1] = b

#
#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


# def create_complex_number(a: int, b: int) -> dict:
#     """
#     Create a complex number as a dict with 2 elements: real part and imaginary part
#     :param a: real part
#     :param b: imaginary part
#     :return: complex number as dict
#     """
#     number = {"real": a, "img": b}
#     return number
#
#
# def get_real_part(number: dict) -> int:
#     """
#     Returns real part of a complex number stored as a dict
#     :param number: complex number as dict
#     :return: real part
#     """
#     return number["real"]
#
#
# def get_img_part(number: dict) -> int:
#     """
#     Returns imaginary part of a complex number stored as a dict
#     :param number: complex number as dict
#     :return: imaginary part
#     """
#     return number["img"]
#
#
# def set_real_part(number: dict, a: int):
#     """
#     Set real part of a complex number stored as a dict
#     :param number: complex number as dict
#     :param a: new real part
#     """
#     number["real"] = a
#
#
# def set_img_part(number: dict, b: int):
#     """
#     Set imaginary part of a complex number stored as a dict
#     :param number: complex number as dict
#     :param b: new imaginary part
#     """
#     number["img"] = b


def string_number(number) -> str:
    """
    Transform a complex number to a string
    :param number:
    :return: number as string
    """
    complex_string = ""
    if get_img_part(number) != 0:
        if get_img_part(number) > 0:
            complex_string = str(get_real_part(number)) + "+" + str(get_img_part(number)) + "i"
        elif get_img_part(number) < 0:
            complex_string = str(get_real_part(number)) + str(get_img_part(number)) + "i"
    else:
        complex_string = str(get_real_part(number))
    return complex_string


def fill_list(complex_list: list):
    """
    Fill a list with 10 random complex numbers
    :param complex_list:
    """
    for i in range(10):
        number = create_complex_number(random.randint(-1000, 1000), random.randint(-1000, 1000))
        complex_list.append(number)
#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def real_mountain_subarray(complex_numbers: list) -> list:
    """
    Length and elements for the longest subarray of numbers where
    their real part is in the form of a mountain (first the values increase, then they decrease).
    :param complex_numbers: list of complex numbers
    :return:
    """
    subarray = []
    maxlength = 0
    starting_from = 0
    max_starting_from = 0
    length = 0
    n = len(complex_numbers)

    for i in range(n):
        # if number is a mountain update the subarray data
        if mountain(get_real_part(complex_numbers[i])):
            if length == 0:
                starting_from = i
            length += 1
            # update maximum length
            if length > maxlength:
                maxlength = length
                max_starting_from = starting_from
        else:
            length = 0

    # generate subarray
    for i in range(max_starting_from, max_starting_from + maxlength):
        subarray.append(complex_numbers[i])

    return subarray


def mountain(number: int) -> bool:
    """
    Check if a number is in the form of a mountain
    :param number:
    :return:
    """
    aux = abs(number)
    max_dig = 0

    # find maximum digit
    while aux != 0:
        if aux % 10 > max_dig:
            max_dig = aux % 10
        aux //= 10

    aux = abs(number)
    digit = aux % 10

    # check the decreasing part of the mountain
    while digit != max_dig:
        aux //= 10
        if digit >= aux % 10:
            return False
        digit = aux % 10

    # check the increasing part of the mountain
    while aux > 9:
        aux //= 10
        if digit <= aux % 10:
            return False
        digit = aux % 10

    return True


def max_subarray_sum(complex_numbers: list) -> list:
    """
    Function to determinate a maximum subarray sum
    :param complex_numbers: list of complex numbers
    :return: a subarray with the maximum sum
    """
    max_so_far = get_real_part(complex_numbers[0])
    max_ending_here = 0
    start_index = 0
    end_index = 0
    s = 0

    for i in range(len(complex_numbers)):
        max_ending_here += get_real_part(complex_numbers[i])

        # update max sum and starting and ending indexes
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start_index = s
            end_index = i

        # if sum is negative reset
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    #    curr_max = max(a[i])
    # return the subarray
    subarray = complex_numbers[start_index:end_index + 1]
    return subarray


# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities


def print_menu():
    """
    Procedure to print the menu options and receive input
    :return:
    """
    print("This app manages different tasks regarding complex numbers.\n"
          "To select an option please input the number of the option\n"
          "\t1. Read list of complex numbers\n"
          "\t2. Display currently memorized list\n"
          "\t3. Solve one of 2 assigned tasks\n"
          "\t4. Exit the app")


def read_list(complex_numbers: list) -> list:
    """
    Function to read the list of complex numbers
    :param complex_numbers: list of complex numbers created from input
    :return: the received list with new content
    """
    complex_numbers.clear()
    length = int(input("How long should the list be?\n"))

    # Build each number as a list/dict and append it
    for i in range(length):
        nr = input("Number " + str(i + 1) + ": ")
        # number in form a+bi
        if "+" in nr:
            try:
                values = nr.split("+")
                real = int(values[0])
                img = int(values[1].strip("i"))
                number = create_complex_number(real, img)
                complex_numbers.append(number)
            except ValueError:
                print("Wrong input")
        # number in form a-bi
        elif "-" in nr:
            try:
                values = nr.split("-")
                if nr[0] == "-":
                    str_real = "-".join([values[0], values[1]])
                    str_img = values[2]
                else:
                    str_real = values[0]
                    str_img = values[1]
                real = int(str_real)
                img = int("-" + str_img.strip("i"))
                number = create_complex_number(real, img)
                complex_numbers.append(number)
            except ValueError:
                print("Wrong input")
    return complex_numbers


def print_list(complex_numbers: list):
    """
    Procedure to print the list of numbers
    :param complex_numbers: list to print
    :return:
    """
    for element in complex_numbers:
        # Convert each number to its string representation
        print(string_number(element), end=", ")
    print("\n")


def option_3_split(complex_numbers: list):
    """
    Procedure to handle the 2 sub-options of the 3rd main option by awaiting new input.
    After receiving input prints data obtained from a called function.
    :param complex_numbers:
    :return:
    """
    print("1. Length and elements for the longest subarray of numbers where their real "
          "part is in the form of a mountain \n2. The length and elements of a maximum subarray sum,"
          " when considering each number's real part")
    option = int(input("Choose the number of your desired option: "))
    if option == 1:
        # Solve the first problem - the mountain numbers subarray
        print("\n")
        seq = real_mountain_subarray(complex_numbers)
        print("The length is: " + str(len(seq)))
        print("The subarray is: ")
        print_list(seq)
    if option == 2:
        # Solve the dynamic programming problem - maximum subarray sum
        print("\n")
        subarray = max_subarray_sum(complex_numbers)
        print("The length is: " + str(len(subarray)))
        print("The subarray is: ")
        print_list(subarray)


def start():
    """
    Starting point of the project
    """
    # declare our list of complex numbers
    complex_numbers = []
    # fill the list with 10 numbers at project start
    fill_list(complex_numbers)

    while True:
        # print the menu
        print_menu()
        # handle the option input
        option = int(input("Choose an option: "))
        if option == 1:
            complex_numbers = read_list(complex_numbers)
        elif option == 2:
            print_list(complex_numbers)
        elif option == 3:
            option_3_split(complex_numbers)
        elif option == 4:
            break
        else:
            print("Wrong option")


# entry point
if __name__ == "__main__":
    start()
