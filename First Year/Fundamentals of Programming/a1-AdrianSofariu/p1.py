# Solve the problem from the first set here
"""

3. For a given natural number n find the minimal natural number m formed with the same digits. (e.g. n=3658, m=3568).

"""


def find_number(nr_string: str) -> int:
    appearance_list = []
    for i in '0123456789':
        appearance_list.append(nr_string.count(i))
    new_number = 0
    for i in range(0, 10):
        # this version cuts all 0 digits from the final version
        if appearance_list[i] != 0:
            while appearance_list[i] != 0:
                new_number = new_number * 10 + i
                appearance_list[i] = appearance_list[i] - 1
    return new_number


def print_menu():
    while True:
        nr_string = input("Choose a number:\n")
        if nr_string == "exit":
            break
        else:
            try:
                nr = int(nr_string)
                result = find_number(nr_string)
                print(result)
            except ValueError:
                print("Please choose a valid number")


if __name__ == '__main__':
    print("This program finds the minimum number that can be created using the digits of a given number."
          " To exit the program type 'exit'")
    print_menu()
