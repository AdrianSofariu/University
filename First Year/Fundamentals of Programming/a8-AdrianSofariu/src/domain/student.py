import random

from src.domain.id_object import IdObject


class Student(IdObject):
    """
    This class represents a student characterized by an integer id, a name and an integer group
    It also inherits the structure of the IdObject class
    """

    def __init__(self, student_id: int, name: str, group: int):
        # check if the parameters have correct types
        if not isinstance(student_id, int):
            raise TypeError("Student id must be an integer")

        if not isinstance(group, int):
            raise TypeError("Group must be a number")

        super().__init__(student_id)
        self.__name = name
        self.__group = group

    @property
    def name(self) -> str:
        return self.__name

    @property
    def group(self) -> int:
        return self.__group

    def __str__(self):
        return str(self.id) + ": " + self.name + " Group: " + str(self.group)

    def __repr__(self):
        return str(self)

    @staticmethod
    def generate_students(n: int) -> list:
        """
        Method to generate n students
        :param n: number of students to generate
        :return: list of student objects
        """
        result = []
        _id = 100
        family_names = ['Smith', 'Jones', 'Williams', 'Taylor', 'Brown', 'Wilson', 'Davies', 'Evans', 'Thomas',
                        'Johnson']
        given_names = ["Oliver", "William", "Jack", "Harry", "Leo", "Olivia", "Amelia", "Evelyn", "Grace", "Sophie"]
        for i in range(n):
            g = random.randint(1, 7)
            stud = Student(_id + i, random.choice(family_names) + " " + random.choice(given_names), g)
            result.append(stud)
        return result
