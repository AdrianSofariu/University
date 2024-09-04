import datetime

import pytest

from src.domain.assignment import Assignment
from src.domain.errors import RepositoryError
from src.domain.student import Student
from src.repository.repository import Repository


class TestClass:

    def test_add_idobject(self):
        """
        Test if we can an idObject in a repo and if the exceptions trigger if the data is of wrong types
        :return:
        """
        student = Student(1, "John", 1)
        assignment = Assignment(2, "Desc", datetime.date.today())

        student_wrong = Student(1, "Wrong", 2)

        not_a_student = 1
        repo = Repository()
        repo.add_to_repo(student)
        repo.add_to_repo(assignment)

        # check if insertion was successful
        assert student in repo
        assert assignment in repo

        # check if adding an idObject with the same id fails
        with pytest.raises(RepositoryError) as e:
            repo.add_to_repo(student_wrong)
        assert str(e.value) == "Object already exists"

        # check if we can add something different in the repo
        with pytest.raises(TypeError) as e:
            repo.add_to_repo(1)
        assert str(e.value) == "Can only add IdObject instances"

    def test_remove_idobject(self):
        """
        Test if we can remove an idObject and if RepositoryError triggers
        if we try to remove something that doesn't exist
        :return:
        """
        student = Student(1, "John", 1)
        assignment = Assignment(2, "Desc", datetime.date.today())
        repo = Repository()
        repo.add_to_repo(student)
        repo.add_to_repo(assignment)

        repo.remove(student.id)
        # test successful removal
        assert len(repo) == 1

        repo.remove(assignment.id)
        assert len(repo) == 0

        # test exception
        with pytest.raises(RepositoryError) as e:
            repo.remove(0)
        assert str(e.value) == "Object doesn't exist."

    def test_update_idobject(self):
        """
        Test if we can update an idObject and if RepositoryError triggers if obj does not exist
        :return:
        """
        student = Student(1, "John", 1)
        assignment = Assignment(2, "Desc", datetime.date.today())
        repo = Repository()
        repo.add_to_repo(student)
        repo.add_to_repo(assignment)

        updated_student = Student(1, "John Mack", 2)
        updated_assignment = Assignment(2, "Desc", datetime.date(2023, 9, 12))

        repo.update(student.id, updated_student)
        repo.update(assignment.id, updated_assignment)

        # test if updates worked
        assert repo[student.id].name == updated_student.name
        assert repo[student.id].group == updated_student.group
        assert repo[assignment.id].deadline == updated_assignment.deadline

        # test if objects that don't exist can't be updated
        with pytest.raises(RepositoryError) as e:
            repo.update(0, student)
        assert str(e.value) == "Object doesn't exist."

    def test_find(self):
        """
        Test finding an object in the repository
        :return:
        """
        student = Student(1, "John", 1)
        assignment = Assignment(2, "Desc", datetime.date.today())
        repo = Repository()
        repo.add_to_repo(student)
        repo.add_to_repo(assignment)

        # check if we can find what we added
        assert repo.find(student.id) == student
        assert repo.find(assignment.id) == assignment

        # check if searching for objects that don't exist returns None
        assert repo.find(0) is None

    def test_list(self):
        """
        Test listing the objects in the repository
        :return:
        """

        repo = Repository()
        # test if printing an empty repo raises an error
        with pytest.raises(RepositoryError) as e:
            repo.list_records()
        assert str(e.value) == "No records found"

        student = Student(1, "John", 1)
        assignment = Assignment(2, "Desc", datetime.date.today())

        repo.add_to_repo(student)
        repo.add_to_repo(assignment)

        # check if we print 2 objects
        assert len(repo.list_records()) == 2
        # check if the strings are identical
        records = repo.list_records()
        assert records[0] == str(student) and records[1] == str(assignment)

    def test_iterating(self):
        """
        Test getting items and iterating through the repository
        :return:
        """
        student = Student(1, "John", 1)
        assignment = Assignment(2, "Desc", datetime.date.today())
        repo = Repository()
        repo.add_to_repo(student)
        repo.add_to_repo(assignment)

        assert repo[student.id] == student
        assert repo[assignment.id] == assignment

        assert len(repo) == 2

        for element in repo:
            assert isinstance(element.id, int)
