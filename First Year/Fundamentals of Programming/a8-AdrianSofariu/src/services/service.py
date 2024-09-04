from datetime import date

from src.domain.assignment import Assignment
from src.domain.errors import RepositoryError, BusinessLogicError
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.repository import Repository


class Service:

    def __init__(self):
        self.__student_repo = Repository()
        self.__assignments_repo = Repository()
        self.__grade_repo = Repository()
        self.__auto_id = 1000
        self.generate_data()

    @property
    def student_repo(self):
        return self.__student_repo

    @property
    def assignments_repo(self):
        return self.__assignments_repo

    def generate_data(self):
        """
        Method to generate data to test our app
        :return:
        """
        students, assignments, grades = Grade.generate_grades(20)

        for s in students:
            self.__student_repo.add_to_repo(s)

        for a in assignments:
            self.__assignments_repo.add_to_repo(a)

        for g in grades:
            self.__grade_repo.add_to_repo(g)

    def add_student(self, identifier: int, name: str, group: int):
        """
        Method to add student to the repository
        :param identifier: integer id
        :param name: string name of the student
        :param group: integer group of the student
        :return:
        """
        student = Student(identifier, name, group)
        self.__student_repo.add_to_repo(student)

    def update_student(self, identifier: int, name: str, group: int):
        """
        Method to update student in the repository
        :param identifier: integer identifier
        :param name: new name of the student
        :param group: new group of the student
        :return:
        """
        self.__student_repo.remove(identifier)
        student = Student(identifier, name, group)
        self.__student_repo.add_to_repo(student)

    def remove_student(self, identifier):
        """
        Method to remove the student from the repository and all his grades
        :param identifier: integer identifier
        :return:
        """
        self.__student_repo.remove(identifier)
        for grade in self.__grade_repo:
            if grade.student_id == identifier:
                self.__grade_repo.remove(grade.id)

    def list_students(self) -> list:
        """
        Method to get all student objects in the repository as strings for printing
        :return: list of str(Student)
        """
        return self.__student_repo.list_records()

    def add_assignment(self, identifier: int, description: str, deadline: date):
        """
        Method to add a new assignment to the repository
        :param identifier: id of the assignment to be added
        :param description: description of the assignment
        :param deadline: deadline of the assignment
        :return:
        """
        assignment = Assignment(identifier, description, deadline)
        self.__assignments_repo.add_to_repo(assignment)

    def update_assignment(self, identifier: int, description: str, deadline: date):
        """
        Method to update an assignment in the repository
        :param identifier: id of the assignment to be updated
        :param description: new description of the assignment
        :param deadline: new deadline of the assignment
        :return:
        """
        self.__assignments_repo.remove(identifier)
        assignment = Assignment(identifier, description, deadline)
        self.__assignments_repo.add_to_repo(assignment)

    def remove_assignment(self, identifier: int):
        """
        Method to remove an assignment from the repository and all the related grades
        :param identifier: id of the assignment to be removed
        :return:
        """
        self.__assignments_repo.remove(identifier)
        for grade in self.__grade_repo:
            if grade.assignment_id == identifier:
                self.__grade_repo.remove(grade.id)

    def list_assignments(self) -> list:
        """
        Method to list all assignments in the repository
        :return: list of str(Assignment)
        """
        return self.__assignments_repo.list_records()

    def grade_exists(self, grade: Grade) -> bool:
        """
        Checks if a grade already exists in the repository
        :return: True if grade exists, False otherwise
        """
        for grade_record in self.__grade_repo:
            if grade_record == grade:
                return True
        return False

    def add_grade(self, student_id: int, assignment_id: int):
        """
        Method to create and add a new grade in the repository
        :param student_id: id of the student
        :param assignment_id: id of the assignment
        :return:
        raises RepositoryError if the student or the assignment don't exist or if the grade already exists
        """
        # check if student exists
        if self.__student_repo.find(student_id) is None:
            raise RepositoryError("Student does not exist")

        # check if assignment exists
        if self.__assignments_repo.find(assignment_id) is None:
            raise RepositoryError("Assignment does not exist")

        # create a grade
        grade = Grade(self.__auto_id, student_id, assignment_id)

        # check if the grade already exists
        if self.grade_exists(grade):
            raise RepositoryError("Assignment already exists")

        # increment the auto_id for next time
        self.__auto_id += 1
        # add grade to repo
        self.__grade_repo.add_to_repo(grade)

    def add_grade_for_group(self, group: int, assignment_id: int):
        """
        Method to add a new grade in the repository for each student in a given group
        :param group: group of the students
        :param assignment_id: the given assignment
        :return:
        :raises RepositoryError if the assignment doesn't exist, if the group has no students or the assignment was
        already given to the group
        """
        added_grades = 0

        # check if assignment exists
        if self.__assignments_repo.find(assignment_id) is None:
            raise RepositoryError("Assignment does not exist")

        # go through all students
        for student in self.__student_repo:
            # if student is in given group
            if student.group == group:
                grade = Grade(self.__auto_id, student.id, assignment_id)
                # and grade does not exist
                if not self.grade_exists(grade):
                    # add it to the repo
                    self.__grade_repo.add_to_repo(grade)
                    self.__auto_id += 1
                    added_grades += 1

        # if there is no student in the given group raise an error
        if added_grades == 0:
            raise RepositoryError("Group has no students or assignment was already given to this group")

    def grade_student(self, student_id: int, assignment_id: int, grade: int):
        """
        Method that modifies the grade_value parameter of a Grade object with given student_id and assignment_id if it exists
        :param student_id: id of the student
        :param assignment_id: id of the assignment
        :param grade: new value of the grade
        :return:
        raises RepositoryError if the assignment doesn't exist or if the assignment was already graded
        """

        # check if assignment exists
        if self.__assignments_repo.find(assignment_id) is None:
            raise RepositoryError("Assignment does not exist")

        aux = Grade(-1, student_id, assignment_id)
        ok = 0

        # find the grade
        for grades in self.__grade_repo:
            # if it is ungraded, grade it
            if grades == aux and grades.grade_value == -1:
                grades.grade_value = grade
                ok = 1
            # if it is graded raise an error
            elif grades == aux and grades.grade_value != -1:
                raise BusinessLogicError("Assignment has already been graded")
        if ok == 0:
            raise BusinessLogicError("Assignment does not exist!")

    def ungraded_assignments(self, student_id: int) -> list:
        """
        Method that returns a list of all the ungraded assignments of a student
        :param student_id:
        :return: list of str(Grade)
        raises RepositoryError if the student doesn't exist
        """
        # check if student exists
        if self.__student_repo.find(student_id) is None:
            raise RepositoryError("Student does not exist")

        ungraded_assignments = []

        # add all ungraded assignments to the list
        for grade in self.__grade_repo:
            if grade.student_id == student_id and grade.grade_value == -1:
                ungraded_assignments.append(str(grade))

        return ungraded_assignments

    def list_grades(self):
        """
        Method to list all assignments in the repository
        :return: list of str(Assignment)
        """
        print(self.__grade_repo.list_records())

    def assignment_given(self, assignment_id: int) -> tuple:
        """
        Method that returns a list with all the students who received the assignment with given id, ordered descending
        by grade; ungraded students are at the end
        :return: the str(assignment), the list of str(Students) and grade
        raises RepositoryError if the assignment doesn't exist
        """

        # check if assignment exists
        assignment = self.__assignments_repo.find(assignment_id)
        if assignment is None:
            raise RepositoryError("Assignment does not exist")

        students = []
        grades = []

        # get the grades for the requested assignment
        for grade in self.__grade_repo:
            if grade.assignment_id == assignment_id:
                grades.append(grade)

        # sort the grades
        grades.sort(reverse=True)

        # get the students
        for grade in grades:
            if grade.grade_value != -1:
                students.append(str(self.__student_repo[grade.student_id]) + "-- Grade: " + str(grade.grade_value))
            else:
                students.append(str(self.__student_repo[grade.student_id]) + "-- Grade: ungraded")

        return str(assignment), students

    def late_assignment(self):
        """
        Method that returns all students that have a late assignment
        :return:
        """

        late_assignments = []
        result = {}

        # check all assignments for which the deadline has passed
        for assignment in self.__assignments_repo:
            if assignment.deadline < date.today():
                late_assignments.append(assignment.id)

        # check which late assignments are still ungraded
        # and add the student id as a dict key and all the late assignments as values
        for grade in self.__grade_repo:
            if grade.assignment_id in late_assignments and grade.grade_value == -1:
                s = self.__student_repo.find(grade.student_id)
                assignment = self.__assignments_repo.find(grade.assignment_id)
                if s not in result.keys():
                    assignments = [assignment]
                    result[s] = assignments
                else:
                    result[s].append(assignment)

        return result

    def school_situation(self):
        """
        Method that returns all students ordered descending by the average grade of their assignments
        :return:
        """

        result = []

        for student in self.__student_repo:
            situation = StudentAverageDTO(student, self.avg(student.id))
            result.append(situation)

        result.sort(reverse=True)
        return result

    def avg(self,  student_id: int) -> float:
        """
        Method that performs the average grade of a student
        :return:
        """

        total = 0
        nr = 0

        for grade in self.__grade_repo:
            if grade.student_id == student_id:
                if grade.grade_value != -1:
                    total += grade.grade_value
                    nr += 1

        if nr != 0:
            return round(total/nr, 2)
        else:
            return 0


class StudentAverageDTO:

    def __init__(self, student: Student, avg: float):
        self.__student = student
        self.__avg = avg

    @property
    def student(self) -> Student:
        return self.__student

    @property
    def avg(self) -> float:
        return self.__avg

    def __lt__(self, other):
        return self.avg < other.avg
