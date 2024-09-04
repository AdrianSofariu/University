class Student:

    def __init__(self, identifier: int, name: str, attendance_count: int, grade: int):
        self.__name = name
        self.__identifier = identifier
        self.__attendance_count = attendance_count
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def set_grade(self, ng: int):
        self.__grade = ng

    def get_identifier(self):
        return self.__identifier

    def get_attendance(self):
        return self.__attendance_count

    def __lt__(self, other):
        if self.get_grade() != other.get_grade():
            return self.get_grade() < other.get_grade()
        else:
            return self.get_name() > other.get_name()

    def __str__(self):
        return "\n" + str(self.__identifier) + ", " + self.__name + ", " + str(self.__attendance_count) + ", " + str(self.__grade)