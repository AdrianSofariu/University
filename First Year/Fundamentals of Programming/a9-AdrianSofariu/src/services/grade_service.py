import os.path
import re
from datetime import date

from src.domain.errors import RepositoryError, BusinessLogicError
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.binary_repo import BinaryRepository
from src.repository.repository import Repository
from src.repository.textfile_repo import TextFileRepository
from src.services.undo_service import UndoService, Command, Operation, CascadedOperation


class GradeService:

    def __init__(self, students: Repository(), assignments: Repository(), grades: Repository(), undo_service: UndoService):
        self.__student_repo = students
        self.__assignments_repo = assignments
        self.__grade_repo = grades
        self.__auto_id = 0
        self.__undo_service = undo_service

    @property
    def student_repo(self):
        return self.__student_repo

    @property
    def assignments_repo(self):
        return self.__assignments_repo

    def grade_exists(self, grade: Grade) -> bool:
        """
        Checks if a grade already exists in the repository
        :return: True if grade exists, False otherwise
        """
        for grade_record in self.__grade_repo:
            if grade_record == grade:
                return True
        return False

    def add_grade(self, student_id: int, assignment_id: int, value: int = -1,  grade_id: int = 0):
        """
        Method to create and add a new grade in the repository
        :param value: grade value
        :param grade_id: optional parameter
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
        if grade_id != 0:
            grade = Grade(grade_id, student_id, assignment_id, value)
        else:
            grade = Grade(self.__auto_id, student_id, assignment_id, value)

        # check if the grade already exists
        if self.grade_exists(grade):
            raise RepositoryError("Assignment already exists")

        # record for undo/redo
        undo_action = Command(self.remove_grade, self.__auto_id)
        if grade_id != 0:
            redo_action = Command(self.add_grade, student_id, assignment_id, value, grade_id)
        else:
            redo_action = Command(self.add_grade, student_id, assignment_id, -1, self.__auto_id)
            self.__auto_id += 1
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record_undo(operation)
        # add grade to repo
        self.__grade_repo.add_to_repo(grade)

    def add_grade_for_group(self, group: int, assignment_id: int):
        """
        Method to add a new grade in the repository for each student in a given group
        :param group: group of the students
        :param assignment_id: the given assignment
        :return:
        raises RepositoryError if the assignment doesn't exist, if the group has no students or the assignment was
        already given to the group
        """
        added_grades = 0

        # check if assignment exists
        if self.__assignments_repo.find(assignment_id) is None:
            raise RepositoryError("Assignment does not exist")

        # go through all students
        cascade = []
        for student in self.__student_repo:
            # if student is in given group
            if student.group == group:
                grade = Grade(self.__auto_id, student.id, assignment_id)
                # and grade does not exist
                if not self.grade_exists(grade):
                    # record grade for undo/redo
                    undo_action = Command(self.remove_grade, self.__auto_id)
                    redo_action = Command(self.add_grade, student.id, assignment_id, -1, self.__auto_id)
                    operation = Operation(undo_action, redo_action)
                    cascade.append(operation)

                    # add it to the repo
                    self.__grade_repo.add_to_repo(grade)
                    self.__auto_id += 1
                    added_grades += 1
        self.__undo_service.record_undo(CascadedOperation(cascade))

        # if there is no student in the given group raise an error
        if added_grades == 0:
            raise RepositoryError("Group has no students or assignment was already given to this group")

    def remove_grade(self, identifier) -> Operation:
        """
        Method to remove a grade from the repository
        :param identifier: grade id
        :return: grade
        """
        grade_to_delete = self.__grade_repo.find(identifier)
        if grade_to_delete is not None:
            redo = Command(self.remove_grade, identifier)
            undo = Command(self.add_grade, grade_to_delete.student_id, grade_to_delete.assignment_id, grade_to_delete.grade_value, identifier)
            operation = Operation(undo, redo)
            self.__grade_repo.remove(identifier)
            return operation

    def update_grade(self, identifier: int, student_id: int, assignment_id: int, value: int):
        """
        Method to update a grade in the repository
        :param value: new value
        :param assignment_id: new assignment id
        :param student_id: new student id
        :param identifier:
        :return:
        """
        removed_grade = self.__grade_repo.remove(identifier)
        grade = Grade(identifier, student_id, assignment_id, value)
        self.__grade_repo.add_to_repo(grade)

        undo_action = Command(self.update_grade, identifier, removed_grade.student_id, removed_grade.assignment_id, removed_grade.grade_value)
        redo_action = Command(self.update_grade, identifier, student_id, assignment_id, value)
        operation = Operation(undo_action, redo_action)
        self.__undo_service.record_undo(operation)

    def filter_grade_by_student(self, student_id: int = 0) -> list:
        """
        Method to return all grades from the repository for a student
        :param student_id: id of student for which to return grades, default = 0 (for all students)
        :return:
        """
        # check if student exists
        if self.__student_repo.find(student_id) is None:
            raise RepositoryError("Student does not exist")

        # filter
        grades = []
        for grade in self.__grade_repo:
            if grade.student_id == student_id:
                grades.append(grade)
        return grades

    def filter_grade_by_assignment(self, assignment_id: int = 0) -> list:
        """
        Method to return all grades from the repository for a given assignment
        :param assignment_id: id of the assignment for which to return grades, default = 0 (return all grades at this
        assignment)
        :return:
        """

        # check if assignment exists
        if self.__assignments_repo.find(assignment_id) is None:
            raise RepositoryError("Assignment does not exist")

        # remove
        grades = []
        for grade in self.__grade_repo:
            if grade.assignment_id == assignment_id:
                grades.append(grade)
        return grades

    def grade_student(self, student_id: int, assignment_id: int, grade: int):
        """
        Method that modifies the grade_value parameter of a Grade object with given student_id and assignment_id if it
        exists
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
                identifier = grades.id
                ok = 1
                self.update_grade(identifier, grades.student_id, grades.assignment_id, grade)
                # grade it
                # self.__grade_repo.update(identifier, Grade(identifier, student_id, assignment_id, grade))
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
        return self.__grade_repo.list_records()

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

    def init_repo(self):
        """
        Method to initialize the data in memory if we read from a file repo
        :return:
        """
        if isinstance(self.__grade_repo, TextFileRepository):
            if os.path.getsize(self.__grade_repo.filename) != 0:
                with open(self.__grade_repo.filename, 'r') as file:
                    lines = file.read().splitlines()
                    for line in lines:
                        line = line.strip()
                        words = re.split(": | {2}| ", line)
                        grade_id = int(words[0])
                        stud_id = int(words[2])
                        assignment_id = int(words[4])
                        if words[6] == "ungraded":
                            value = -1
                        else:
                            value = int(words[6])
                        grade = Grade(grade_id, stud_id, assignment_id, value)
                        self.__grade_repo.add_no_update(grade)
            else:
                grades = Grade.generate_grades(20, self.__student_repo, self.__assignments_repo)
                for grade in grades:
                    self.__grade_repo.add_to_repo(grade)
        elif isinstance(self.__grade_repo, BinaryRepository):
            if os.path.getsize(self.__grade_repo.filename) != 0:
                self.__grade_repo.load_file()
            else:
                grades = Grade.generate_grades(20, self.__student_repo, self.__assignments_repo)
                for grade in grades:
                    self.__grade_repo.add_to_repo(grade)
        else:
            grades = Grade.generate_grades(20, self.__student_repo, self.__assignments_repo)
            for grade in grades:
                self.__grade_repo.add_to_repo(grade)
        self.__auto_id = self.compute_auto_id()

    def compute_auto_id(self):
        maxi = 999
        for obj in self.__grade_repo:
            if obj.id > maxi:
                maxi = obj.id
        return maxi+1


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
