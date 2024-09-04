import os

from src.domain.student import Student
from src.repository.binary_repo import BinaryRepository
from src.repository.repository import Repository
from src.repository.textfile_repo import TextFileRepository
from src.services.grade_service import GradeService

import re

from src.services.undo_service import UndoService, Command, Operation, CascadedOperation


class StudentService:

    def __init__(self, students: Repository, grade_service: GradeService, undo_service: UndoService):
        self._repo = students
        self._grade_service = grade_service
        self._undo_service = undo_service

    def add_student(self, identifier: int, name: str, group: int):
        """
        Method to add student to the repository
        :param identifier: integer id
        :param name: string name of the student
        :param group: integer group of the student
        :return:
        """
        student = Student(identifier, name, group)
        self._repo.add_to_repo(student)

        undo_action = Command(self.remove_student, identifier)
        redo_action = Command(self.add_student, identifier, name, group)
        operation = Operation(undo_action, redo_action)
        self._undo_service.record_undo(operation)

    def update_student(self, identifier: int, name: str, group: int):
        """
        Method to update student in the repository
        :param identifier: integer identifier
        :param name: new name of the student
        :param group: new group of the student
        :return:
        """
        removed_student = self._repo.remove(identifier)
        student = Student(identifier, name, group)
        self._repo.add_to_repo(student)

        undo_action = Command(self.update_student, identifier, removed_student.name, removed_student.group)
        redo_action = Command(self.update_student, identifier, name, group)
        operation = Operation(undo_action, redo_action)
        self._undo_service.record_undo(operation)

    def remove_student(self, identifier):
        """
        Method to remove the student from the repository and all his grades
        :param identifier: integer identifier
        :return:
        """

        student_to_delete = self._repo.find(identifier)
        if student_to_delete is not None:
            undo_action = Command(self.add_student, identifier, student_to_delete.name, student_to_delete.group)
            redo_action = Command(self.remove_student, identifier)
            operation = Operation(undo_action, redo_action)
            cascade = [operation]
            grades = self._grade_service.filter_grade_by_student(identifier)
            for grade in grades:
                grade_operation = self._grade_service.remove_grade(grade.id)
                cascade.append(grade_operation)
            self._undo_service.record_undo(CascadedOperation(cascade))
        self._repo.remove(identifier)

    def list_students(self) -> list:
        """
        Method to get all student objects in the repository as strings for printing
        :return: list of str(Student)
        """
        return self._repo.list_records()

    def init_repo(self):
        """
        Method to initialize the data in memory if we read from a file repo
        :return:
        """
        if isinstance(self._repo, TextFileRepository):
            if os.path.getsize(self._repo.filename) != 0:
                with open(self._repo.filename, 'r') as file:
                    lines = file.read().splitlines()
                    for line in lines:
                        line = line.strip()
                        words = re.split(": | ", line)
                        identifier = int(words[0])
                        name = words[1]
                        i = 2
                        while words[i] != "Group":
                            name += " " + words[i]
                            i += 1
                        group = int(words[i+1])
                        stud = Student(identifier, name, group)
                        self._repo.add_no_update(stud)
            else:
                students = Student.generate_students(20)
                for student in students:
                    self._repo.add_to_repo(student)
        elif isinstance(self._repo, BinaryRepository):
            if os.path.getsize(self._repo.filename) != 0:
                self._repo.load_file()
            else:
                students = Student.generate_students(20)
                for student in students:
                    self._repo.add_to_repo(student)
        else:
            students = Student.generate_students(20)
            for student in students:
                self._repo.add_to_repo(student)
