# Solve the problem from the third set here
"""

Determine the age of a person, in number of days. Take into account leap years, as well as the date of birth and
current date (year, month, day). Do not use Python's inbuilt date/time functions.

"""
cal = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def year_is_leap(year: int) -> bool:
    """
    Check if a year is a leap year
    :param year:
    :return:
    """
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def determine_age(birth_date_string: str) -> int:
    """
    Compute the age in days
    :param birth_date_string:
    :return:
    """

    age_in_days = 0

    # assume current date is 13th October 2023
    current_date = [13, 10, 2023]

    # convert the birthdate in a list of numbers
    dmy = birth_date_string.split()
    birth_date = []
    for word in dmy:
        birth_date.append(int(word))

    # if birthdate and current date are not in the same year, add the whole years
    for year in range(birth_date[2] + 1, current_date[2]):
        if year_is_leap(year):
            age_in_days += 366
        else:
            age_in_days += 365

    # if birthdate and current date are not in the same year, add the whole months
    if birth_date[2] < current_date[2]:
        # add months until the end of the birth-year
        for month in range(birth_date[1] + 1, 13):
            if month == 2 and year_is_leap(birth_date[2]):
                age_in_days += cal[2] + 1
            else:
                age_in_days += cal[month]
        # add months in the current year
        for month in range(1, current_date[1]):
            if month == 2 and year_is_leap(current_date[2]):
                age_in_days += cal[2] + 1
            else:
                age_in_days += cal[month]
    # if birthdate and current date are in the same year, add the months
    else:
        for month in range(birth_date[1] + 1, current_date[1]):
            if month == 2 and year_is_leap(birth_date[2]):
                age_in_days += cal[2] + 1
            else:
                age_in_days += cal[month]

    # if birthdate and current date are in the same month, compute the day difference
    if birth_date[1] == current_date[1]:
        age_in_days += current_date[0] - birth_date[0]
    # else, add the number of days until the end of the birth-month and the current date
    else:
        if year_is_leap(birth_date[2]) and birth_date[1] == 2:
            age_in_days += cal[birth_date[1]] + 1 - birth_date[0]
        age_in_days += cal[birth_date[1]] - birth_date[0]
        age_in_days += current_date[0]

    # return the final result
    return age_in_days


def print_menu():
    while True:
        birth_date_string = input("Please input the birth date in the following format: dd mm yyyy\n")
        if birth_date_string == "exit":
            exit()
        else:
            try:
                age_in_days = determine_age(birth_date_string)
                print(age_in_days)
            except (ValueError, IndexError):
                print("Mind the format and choose a valid date!")


if __name__ == "__main__":
    print("This program determines the age of a person in number of days."
          "To exit type 'exit'")
    print_menu()
