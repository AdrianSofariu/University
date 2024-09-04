import datetime

import pytest

from src.domain.assignment import Assignment
from src.domain.student import Student


class TestClassCreation:

    def test_student_constructor(self):

        with pytest.raises(TypeError) as e:
            student = Student("a", "name", 2)
        assert str(e.value) == "Student id must be an integer"

        with pytest.raises(TypeError) as e:
            student = Student(1, "name", "wda")
        assert str(e.value) == "Group must be a number"

    def test_assignment_constructor(self):

        with pytest.raises(TypeError) as e:
            assignment = Assignment("a", "name", datetime.date.today())
        assert str(e.value) == "Assignment id must be an integer"

        with pytest.raises(TypeError) as e:
            assignment = Assignment(1, "name", 2)
        assert str(e.value) == "Deadline must be a date"

        with pytest.raises(TypeError) as e:
            assignment = Assignment(1, "name", "amadmw")
        assert str(e.value) == "Deadline must be a date"
