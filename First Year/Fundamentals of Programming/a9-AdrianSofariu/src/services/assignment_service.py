import os
import re
from datetime import date

from src.domain.assignment import Assignment
from src.repository.binary_repo import BinaryRepository
from src.repository.textfile_repo import TextFileRepository
from src.services.grade_service import GradeService
from src.services.undo_service import UndoService, Command, Operation, CascadedOperation


class AssignmentService:

    def __init__(self, repo, grade_service: GradeService, undo_service: UndoService):
        self._repo = repo
        self._grade_service = grade_service
        self._undo_service = undo_service

    def add_assignment(self, identifier: int, description: str, deadline: date):
        """
        Method to add a new assignment to the repository
        :param identifier: id of the assignment to be added
        :param description: description of the assignment
        :param deadline: deadline of the assignment
        :return:
        """
        assignment = Assignment(identifier, description, deadline)
        self._repo.add_to_repo(assignment)

        undo_action = Command(self.remove_assignment, identifier)
        redo_action = Command(self.add_assignment, identifier, description, deadline)
        operation = Operation(undo_action, redo_action)
        self._undo_service.record_undo(operation)

    def update_assignment(self, identifier: int, description: str, deadline: date):
        """
        Method to update an assignment in the repository
        :param identifier: id of the assignment to be updated
        :param description: new description of the assignment
        :param deadline: new deadline of the assignment
        :return:
        """
        removed_assignment = self._repo.remove(identifier)
        assignment = Assignment(identifier, description, deadline)
        self._repo.add_to_repo(assignment)

        undo_action = Command(self.update_assignment, identifier, removed_assignment.description, removed_assignment.deadline)
        redo_action = Command(self.update_assignment, identifier, description, deadline)
        operation = Operation(undo_action, redo_action)
        self._undo_service.record_undo(operation)

    def remove_assignment(self, identifier: int):
        """
        Method to remove an assignment from the repository and all the related grades
        :param identifier: id of the assignment to be removed
        :return:
        """
        assignment_to_delete = self._repo.find(identifier)
        if assignment_to_delete is not None:
            undo_action = Command(self.add_assignment, identifier, assignment_to_delete.description, assignment_to_delete.deadline)
            redo_action = Command(self.remove_assignment, identifier)
            operation = Operation(undo_action, redo_action)
            cascade = [operation]
            grades = self._grade_service.filter_grade_by_assignment(identifier)
            for grade in grades:
                grade_operation = self._grade_service.remove_grade(grade.id)
                cascade.append(grade_operation)
            self._undo_service.record_undo(CascadedOperation(cascade))
        self._repo.remove(identifier)

    def list_assignments(self) -> list:
        """
        Method to list all assignments in the repository
        :return: list of str(Assignment)
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
                        words = re.split(": | - | ", line)
                        identifier = int(words[1])
                        description = words[2]
                        i = 3
                        while words[i] != "Deadline":
                            description += " " + words[i]
                            i += 1
                        date_info = words[i + 1].split("-")
                        deadline = date(int(date_info[0]), int(date_info[1]), int(date_info[2]))
                        assignment = Assignment(identifier, description, deadline)
                        self._repo.add_no_update(assignment)
            else:
                assignments = Assignment.generate_assignments(20)
                for assignment in assignments:
                    self._repo.add_to_repo(assignment)
        elif isinstance(self._repo, BinaryRepository):
            if os.path.getsize(self._repo.filename) != 0:
                self._repo.load_file()
            else:
                assignments = Assignment.generate_assignments(20)
                for assignment in assignments:
                    self._repo.add_to_repo(assignment)
        else:
            assignments = Assignment.generate_assignments(20)
            for assignment in assignments:
                self._repo.add_to_repo(assignment)
