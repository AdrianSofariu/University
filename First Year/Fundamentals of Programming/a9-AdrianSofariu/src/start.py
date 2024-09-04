import os.path

from src.repository.binary_repo import BinaryRepository
from src.repository.repository import Repository
from src.repository.textfile_repo import TextFileRepository
from src.ui.ui import UI
from jproperties import Properties


def check_file(file_path):
    """
    Check if the file exists, if not, create it
    :param file_path:
    :return:
    """
    if not os.path.exists(file_path):
        with open("repository/" + file_path, 'w') as f:
            pass


if __name__ == "__main__":

    configs = Properties()
    with open('settings.properties', 'rb') as config_file:
        configs.load(config_file)

    # get repository type
    repo_type = configs.get('repository')

    if repo_type[0] == 'inmemory':
        # initialize memory repositories
        students = Repository()
        assignments = Repository()
        grades = Repository()
    elif repo_type[0] == 'textfiles':
        # initialize text file repositories
        check_file(configs.get('students')[0])
        check_file(configs.get('assignments')[0])
        check_file(configs.get('grades')[0])
        students = TextFileRepository(configs.get('students')[0])
        assignments = TextFileRepository(configs.get('assignments')[0])
        grades = TextFileRepository(configs.get('grades')[0])
    elif repo_type[0] == 'binaryfiles':
        # initialize binary file repositories
        check_file(configs.get('students')[0])
        check_file(configs.get('assignments')[0])
        check_file(configs.get('grades')[0])
        students = BinaryRepository("repository/" + configs.get('students')[0])
        assignments = BinaryRepository("repository/" + configs.get('assignments')[0])
        grades = BinaryRepository("repository/" + configs.get('grades')[0])
    else:
        raise Exception("Unknown repository type")

    my_ui = UI(students, assignments, grades)
    my_ui.start()
