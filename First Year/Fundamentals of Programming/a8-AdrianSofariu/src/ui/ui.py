from datetime import date

from colorama import Fore, Style

from src.domain.errors import InputError, BusinessLogicError
from src.repository.repository import RepositoryError
from src.services.service import Service


class UI:

    def __init__(self, ):
        self.__service = Service()

    def start(self):
        """
        Driver method of the ui which reads the user input
        :return:
        """
        while True:
            UI.print_menu()
            try:
                command = input(">>")
                UI.validate_command(command, 6)
                self.execute_command(int(command))
            except (RepositoryError, InputError, ValueError, TypeError, BusinessLogicError) as e:
                print(Fore.RED + str(e))
                print(Style.RESET_ALL)

    @staticmethod
    def print_menu():
        print("This app manages a list of students, assignments and grades.\nThe following commands are available:")
        print("\t1. Manage students")
        print("\t2. Manage assignments")
        print("\t3. Give assignment")
        print("\t4. Grade assignment")
        print("\t5. Statistics")
        print("\t0. Exit")
        print("Please input the number of your chosen command:")

    @staticmethod
    def validate_command(command: str, options: int):
        """
        Method to check if a command is valid (is numeric and 0<=command<=options).
        If invalid, raises InputError
        :return:
        """
        if command.isdigit():
            if int(command) not in range(0, options):
                raise InputError("Unknown command")
        else:
            raise InputError("Unknown command")

    def execute_command(self, command: int):
        """
        Call appropriate service functions to execute UI commands
        :param command: integer between 0 and 5
        :return:
        """
        if command == 0:
            exit()
        elif command == 1:
            self.manage_students()
        elif command == 2:
            self.manage_assignments()
        elif command == 3:
            self.give_assignments()
        elif command == 4:
            self.grade_assignment()
        elif command == 5:
            self.statistics()

    def manage_students(self):
        """
        Call methods to manage the student data in the repository
        :return:
        """
        print("\t1. Add student")
        print("\t2. Remove student")
        print("\t3. Update student")
        print("\t4. List students")
        print("\t0. Back")

        command = input("Input your choice: ")
        # validate input
        UI.validate_command(command, 5)

        # if input is ok, continue
        com = int(command)
        if com == 1:
            self.add_student()
        elif com == 2:
            self.remove_student()
        elif com == 3:
            self.update_student()
        elif com == 4:
            self.print_students()
        elif com == 0:
            pass

    def add_student(self):
        """
        Method to add student data in the repository
        :return:
        """
        identifier = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        group = int(input("Enter student group: "))
        self.__service.add_student(identifier, name, group)

    def remove_student(self):
        """
        Method to remove student data from the repository by id
        :return:
        """
        identifier = int(input("Remove student with ID: "))
        self.__service.remove_student(identifier)

    def update_student(self):
        """
        Method to update student data in the repository by id
        :return:
        """
        identifier = int(input("Update student with ID: "))
        name = input("Enter new student name: ")
        group = int(input("Enter new student group: "))
        self.__service.update_student(identifier, name, group)

    def print_students(self):
        """
        Method to list all students in the repository
        :return:
        """
        students = self.__service.list_students()
        for student in students:
            print(student)

    def manage_assignments(self):
        """
        Call methods to manage the assignment data in the repository
        :return:
        """
        print("\t1. Add assignment")
        print("\t2. Remove assignment")
        print("\t3. Update assignment")
        print("\t4. List assignment")
        print("\t0. Back")

        command = input("Input your choice: ")
        # validate input
        UI.validate_command(command, 5)

        # if input is ok, continue
        com = int(command)
        if com == 1:
            self.add_assignment()
        elif com == 2:
            self.remove_assignment()
        elif com == 3:
            self.update_assignment()
        elif com == 4:
            self.print_assignments()
        elif com == 0:
            pass

    def add_assignment(self):
        """
        Method to add a new assignment to the repository
        :return:
        """
        identifier = int(input("Enter assignment ID: "))
        desc = input("Enter assignment description: ")
        print("Give input for the deadline\n")
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))
        d = date(year, month, day)
        self.__service.add_assignment(identifier, desc, d)

    def remove_assignment(self):
        """
        Method to remove an assignment from the repository by id
        :return:
        """
        identifier = int(input("Remove assignment with ID: "))
        self.__service.remove_assignment(identifier)

    def update_assignment(self):
        """
        Method to update an assignment from the repository by id
        :return:
        """
        identifier = int(input("Enter assignment ID: "))
        desc = input("Enter new assignment description: ")
        print("Give input for the new deadline\n")
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))
        d = date(year, month, day)
        self.__service.update_assignment(identifier, desc, d)

    def print_assignments(self):
        """
        Method to print all assignments in the repository
        :return:
        """
        assignments = self.__service.list_assignments()
        for assignment in assignments:
            print(assignment)

    def give_assignments(self):
        """
        Method to give assignments to a student or a group of students
        :return:
        """
        print("\t1. Give assignment to student")
        print("\t2. Give assignment to group")
        print("\t0. Exit")

        command = input("Input your choice: ")
        # validate input
        UI.validate_command(command, 3)

        # if input is ok, continue
        com = int(command)
        if com == 1:
            self.give_assignment_student()
        elif com == 2:
            self.give_assignment_group()
        elif com == 0:
            pass

    def give_assignment_student(self):
        """
        Method to get input to give an assignment to an individual student
        :return:
        """
        student = int(input("Enter student ID: "))
        assignment = int(input("Enter assignment ID: "))
        self.__service.add_grade(student, assignment)

    def give_assignment_group(self):
        """
        Method to get input to give an assignment to a student group
        :return:
        """
        group = int(input("Enter group number: "))
        assignment = int(input("Enter assignment ID: "))
        self.__service.add_grade_for_group(group, assignment)

    def grade_assignment(self):
        """
        Method to grade an ungraded assignment of an individual student
        :return:
        raise a BusinessLogicError if the student has already been graded for all assignments or does not have any
        assignment
        """
        student = int(input("Enter student ID: "))
        ungraded_assignments = self.__service.ungraded_assignments(student)

        # check if there are any assignments to grade
        if len(ungraded_assignments) == 0:
            raise BusinessLogicError("No ungraded assignments")

        # print the options for the user
        for assignment in ungraded_assignments:
            print(assignment)

        # let him choose an assignment and a grade
        assignment = int(input("Enter assignment ID: "))
        grade = int(input("Enter the grade: "))

        # check for validity of grade
        if grade < 0 or grade > 10:
            raise BusinessLogicError("Grade must be between 0 and 10")

        # grade the assignment
        self.__service.grade_student(student, assignment, grade)

    def statistics(self):
        """
        Method to perform some statistics
        :return:
        """
        print("\t1. Print all students which have been given a certain assignment")
        print("\t2. Print all students who are late in handing in at least one assignment")
        print("\t3. Print the students with the best school situation in descending order")
        print("\t0. Exit")

        command = input("Input your choice: ")
        # validate input
        UI.validate_command(command, 4)

        # if input is ok, continue
        com = int(command)
        if com == 1:
            self.students_with_assignment()
        elif com == 2:
            self.late_students()
        elif com == 3:
            self.school_situation()
        elif com == 0:
            pass

    def students_with_assignment(self):
        """
        Method to get all students that have received an assignment given as input
        :return:
        """

        assignment_id = int(input("Enter assignment ID: "))

        assignment, students = self.__service.assignment_given(assignment_id)
        print("The assignment is --" + assignment)
        for student in students:
            print(student)

    def late_students(self):
        """
        Method to print all students who are late in handing in at least one assignment
        :return:
        """

        result = self.__service.late_assignment()

        for student in result.keys():
            print(str(student) + " -- has the following late assignments: ")
            for assignment in result[student]:
                print("\t" + str(assignment))

    def school_situation(self):
        """
        Method to print the students with the best school situation in descending order
        :return:
        """
        result = self.__service.school_situation()

        for pair in result:
            print(str(pair.student) + "-- avg: " + str(pair.avg))
