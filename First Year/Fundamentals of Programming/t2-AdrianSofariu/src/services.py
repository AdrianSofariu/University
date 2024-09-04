from src.domain import Student
from src.repository import Repository


class BusinessException(Exception):
    pass


class Service:

    def __init__(self, repository: Repository):
        self.__repo = repository

    def add(self, identifier: int, name: str, attendance: int, grade: int):
        """
        Create a new student with the given parameters and add him to repo if his id is unique
        Raise BusinessException if student attendance < 0 or grade not in [0,10]
        Raise BusinessException if student name is not made of min 2 words of min 3 letters each
        :param identifier: int, must be unique
        :param name: str
        :param attendance: int, must be positive
        :param grade: int, between 0 and 10
        :return:
        """
        if attendance < 0 or grade < 0 or grade > 10:
            raise BusinessException("Invalid attendance or grade")
        else:
            if ' ' not in name:
                raise BusinessException("Invalid name")
            else:
                words = name.split(' ')
                if len(words) < 2:
                    raise BusinessException("Invalid name")
                else:
                    for word in words:
                        if len(word) < 3:
                            raise BusinessException("Invalid name")
                    student = Student(identifier, name, attendance, grade)
                    self.__repo.add(student)

    def decreasing_order(self):
        result = []
        students = self.__repo.return_data()
        #students.sort(key=lambda student: student.get_grade(), reverse=True)
        students.sort(reverse=True)
        for student in students:
            result.append((str(student)))
        return result

    def give_bonus(self, p: int, b: int):
        students = self.__repo.return_data()
        for student in students:
            if student.get_attendance() >= p:
                self.__repo.update(student.get_identifier(), b)
        self.__repo.update_file()

    def display_by_string(self, string: str):
        sorted_studs = []
        result = []
        students = self.__repo.return_data()
        for student in students:
            if string in student.get_name().lower():
                sorted_studs.append(student)
        sorted_studs.sort(key=lambda student: student.get_name())
        for stud in sorted_studs:
            result.append(str(stud))
        return result
