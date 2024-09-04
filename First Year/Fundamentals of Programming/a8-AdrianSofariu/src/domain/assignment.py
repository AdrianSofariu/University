import random
from datetime import date, timedelta

from src.domain.id_object import IdObject


class Assignment(IdObject):
    """
    This class represents an assignment characterized by an integer id, a description and a deadline
    """

    def __init__(self, assignment_id: int, description: str, deadline: date):
        # check if the parameters have correct types
        if not isinstance(assignment_id, int):
            raise TypeError("Assignment id must be an integer")

        if not isinstance(deadline, date):
            raise TypeError("Deadline must be a date")

        super().__init__(assignment_id)
        self.__description = description
        self.__deadline = deadline

    @property
    def description(self) -> str:
        return self.__description

    @property
    def deadline(self) -> date:
        return self.__deadline

    def __str__(self):
        return ("Assignment: " + str(self.id) + " - " + str(self.description) + " Deadline: "
                + str(self.deadline))

    def __repr__(self):
        return str(self)

    @staticmethod
    def generate_assignments(n: int) -> list:
        """
        Method to generate n assignments
        :param n: number of assignments to generate
        :return: list of assignment objects
        """
        result = []
        _id = 300
        assignments = ['Console-based app', 'PowerPoint Presentation', 'Speech', 'Essay', 'Project']
        for i in range(n):
            day = random.randint(1, 28)
            month = random.randint(1, 12)
            d = date(2023, month, day)
            a = Assignment(_id + i, random.choice(assignments), d)
            result.append(a)
        return result
