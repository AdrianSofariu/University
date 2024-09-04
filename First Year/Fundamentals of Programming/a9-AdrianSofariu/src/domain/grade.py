import random

from src.domain.id_object import IdObject
from src.domain.student import Student
from src.domain.assignment import Assignment


class Grade(IdObject):
    """
    This class binds a student object and an assignment object using their ID similar to a relational database
    """

    def __init__(self, grade_id: int, student_id: int, assignment_id: int, grade_val=-1):
        # check if the parameter have correct types
        if not isinstance(grade_id, int):
            raise TypeError("Grade id must be an integer")

        if not isinstance(student_id, int):
            raise TypeError("Student id must be an integer")

        if not isinstance(assignment_id, int):
            raise TypeError("Assignment id must be an integer")

        super().__init__(grade_id)
        self.__student_id = student_id
        self.__assignment_id = assignment_id
        self.__grade_value = grade_val

    @property
    def student_id(self) -> int:
        return self.__student_id

    @property
    def assignment_id(self) -> int:
        return self.__assignment_id

    @property
    def grade_value(self) -> int:
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, val: int):
        self.__grade_value = val

    def __str__(self):
        if self.grade_value != -1:
            return (str(super().id) + "  Student: " + str(self.student_id) + "  Assignment: " + str(self.__assignment_id)
                    + " Grade: " + str(self.grade_value))
        else:
            return (str(super().id) + "  Student: " + str(self.student_id) + "  Assignment: " + str(self.__assignment_id)
                    + " Grade: ungraded")

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Overwriting equality. Two grades are equal if they have the same student_id and assignment_id
        :param other:
        :return:
        """
        if self.student_id == other.student_id and self.assignment_id == other.assignment_id:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Overwriting lesser to use sort
        :param other:
        :return:
        """
        if self.grade_value < other.grade_value:
            return True
        return False

    @staticmethod
    def generate_grades(n: int, students, assignments) -> list:
        """
        Method to generate n grades
        :param assignments: list of assignments
        :param students: list of students
        :param n: number of grades to generate
        :return: a tuple with 3 lists containing students, assignments and grades
        """
        #students = Student.generate_students(20)
        #assignments = Assignment.generate_assignments(20)

        result = []
        identifier = 900
        i = 0

        student_list = []
        assignments_list = []

        for student in students:
            student_list.append(student)

        for assignment in assignments:
            assignments_list.append(assignment)

        while i < n:
            ok = 1
            g_id = identifier + i
            s_id = random.choice(student_list).id
            a_id = random.choice(assignments_list).id
            val = random.randint(-1, 10)
            g = Grade(g_id, s_id, a_id, val)
            for grade in result:
                if grade == g:
                    ok = 0
            if ok == 1:
                result.append(g)
                i += 1
        return result
