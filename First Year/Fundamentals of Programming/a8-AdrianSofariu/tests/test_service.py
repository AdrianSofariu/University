import datetime

from src.services.service import Service


class TestService:

    def test_add_student(self):
        """
        Test that a student can be added to the repository in a service
        :return:
        """
        service = Service()
        identifier = 1
        name = "Test"
        group = 1

        service.add_student(identifier, name, group)
        assert service.student_repo.find(identifier) is not None

    def test_remove_student(self):
        """
        Test that a student can be removed from the repository in a service
        :return:
        """
        service = Service()
        identifier = 1
        name = "Test"
        group = 1

        service.add_student(identifier, name, group)
        service.remove_student(identifier)
        assert service.student_repo.find(identifier) is None

    def test_update_student(self):
        """
        Test that a student can be updated in the repository of a service
        :return:
        """
        service = Service()
        identifier = 1
        name = "Test"
        group = 1

        service.add_student(identifier, name, group)
        assert service.student_repo.find(identifier).group == 1

        service.update_student(identifier, name, 2)
        assert service.student_repo.find(identifier).group == 2

    def test_list_student(self):
        """
        Test that the student repo in a service can be listed correctly
        :return:
        """
        service = Service()
        studs = service.list_students()
        for i in range(len(studs)):
            assert studs[i] == str(service.student_repo[100 + i])

    def test_add_assignment(self):
        """
        Test that an assignment can be added to the repository in a service
        :return:
        """
        service = Service()
        identifier = 1
        description = "Test"
        deadline = datetime.date.today()

        service.add_assignment(identifier, description, deadline)
        assert service.assignments_repo.find(identifier) is not None

    def test_remove_assignment(self):
        """
        Test that an assignment can be removed from the repository in a service
        :return:
        """
        service = Service()
        identifier = 1
        description = "Test"
        deadline = datetime.date.today()

        service.add_assignment(identifier, description, deadline)
        service.remove_assignment(identifier)
        assert service.assignments_repo.find(identifier) is None

    def test_update_assignment(self):
        """
        Test that an assignment can be updated in the repository of a service
        :return:
        """
        service = Service()
        identifier = 1
        description = "Test"
        deadline = datetime.date.today()

        service.add_assignment(identifier, description, deadline)
        assert service.assignments_repo.find(identifier).deadline == datetime.date.today()

        service.update_assignment(identifier, description, deadline + datetime.timedelta(days=10))
        assert service.assignments_repo.find(identifier).deadline == datetime.date.today() + datetime.timedelta(days=10)

    def test_list_assignments(self):
        """
        Test that the assignments repo in a service can be listed correctly
        :return:
        """
        service = Service()
        assignments = service.list_assignments()
        for i in range(len(assignments)):
            assert assignments[i] == str(service.assignments_repo[300 + i])
