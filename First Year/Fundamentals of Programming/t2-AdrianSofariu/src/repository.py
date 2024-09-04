from src.domain import Student


class RepositoryException(Exception):
    pass


class Repository:

    def __init__(self, filename: str):
        self.__filename = filename
        self.__data = []
        self.load_data()

    def load_data(self):
        """
        Load data from file
        :return:
        """
        with open(self.__filename, 'r') as file:
            students = file.readlines()
            string = 'abc'
            for student in students:
                try:
                    attributes = student.split(", ")
                    stud = Student(int(attributes[0]), attributes[1], int(attributes[2]), int(attributes[3]))
                    self.__data.append(stud)
                except ValueError:
                    print("Invalid student with id " + attributes[0])

    def find(self, identifier: int):
        """
        Find student in repo
        :param identifier:
        :return: object/none
        """
        for student in self.__data:
            if student.get_identifier() == identifier:
                return student
        return None

    def add(self, student: Student):
        """
        Add student to repo
        Raise RepositoryException if student does not have unique id
        :return:
        """
        if self.find(student.get_identifier()):
            raise RepositoryException("ID is not unique")
        else:
            self.__data.append(student)
            with open(self.__filename, 'a') as file:
                file.write(str(student))

    def update(self, id: int, bonus: int):
        student = self.find(id)
        if student is not None:
            grade = student.get_grade() + bonus
            if grade > 10:
                grade = 10
            student.set_grade(grade)

    def return_data(self):
        return self.__data

    def update_file(self):
        with open(self.__filename, 'w') as file:
            file.write('')
            for student in self.__data:
                file.write(str(student).strip("\n")+"\n")
