from src.repository import Repository, RepositoryException
from src.services import Service, BusinessException


class UI:

    def __init__(self, serv: Service):
        self.__service = serv

    def print_menu(self):
        print("1. Add student")
        print("2. Students in order of grades, decreasing")
        print("3. Give bonus")
        print("4. Display by string")
        print("0. Exit")

    def start(self):
        while True:
            self.print_menu()
            try:
                choice = input("Enter your option: ")
                if choice == "1":
                    self.add_student()
                if choice == "2":
                    self.display_decreasing_grade()
                if choice == "3":
                    self.bonuses()
                if choice == "4":
                    self.display_by_str()
                if choice == "0":
                    exit()
                else:
                    print("Invalid option")
            except (ValueError, RepositoryException, BusinessException) as err:
                print(err)

    def add_student(self):
        """
        UI procedure to add a student to the repository
        It validates if id, attendance and grade are integers
        :return:
        """
        try:
            identifier = int(input("Enter an id:"))
            name = input("Enter a name: ")
            attendance = int(input("Enter attendance count:"))
            grade = int(input("Enter a grade: "))
            self.__service.add(identifier, name, attendance, grade)
        except ValueError:
            print("Invalid attributes")

    def display_decreasing_grade(self):
        to_display = self.__service.decreasing_order()
        for student in to_display:
            print(student)

    def bonuses(self):
        try:
            bonus = int(input("Enter a bonus:"))
            attendances = int(input("Enter min number of attendances:"))
            self.__service.give_bonus(attendances, bonus)
        except ValueError:
            print("Invalid bonus/attendances")

    def display_by_str(self):
        string = input("Enter the string: ")
        result = self.__service.display_by_string(string)
        for student in result:
            print(student)