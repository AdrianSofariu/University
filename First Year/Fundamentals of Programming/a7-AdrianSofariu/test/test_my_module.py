import pickle

from src.repository.binary_file_repository import BinaryFileRepository
from src.repository.memory_repository import MemoryRepository
from src.repository.text_file_repository import TextFileRepository
from src.services.service import Service
from src.domain.expense import Expense


def test_add_to_repository():
    serv = Service(MemoryRepository())
    serv.add_to_repository(20, 1000, "trip")
    expense = Expense(20, 1000, "trip")
    assert expense in serv.get_expenses()


def test_add_entry_memory():
    """
    Method to test the add_entry method
    :return:
    """
    mem_rep = MemoryRepository()
    expense = Expense(10, 1000, "food")
    mem_rep.add_entry(expense)
    assert expense in mem_rep.get_records()

    expense2 = Expense(20, 50, "games")
    mem_rep.add_entry(expense2)
    assert expense2 in mem_rep.get_records()

    mem_rep.undo()
    assert expense2 not in mem_rep.get_records()


def test_add_entry_file():
    """
    Method to test the add_entry method
    :return:
    """
    file_rep = TextFileRepository()
    expense = Expense(10, 1000, "food")
    file_rep.add_entry(expense, "src/repository/test.txt")
    assert expense in file_rep.get_records()

    with open("src/repository/test.txt", 'r') as file:
        content = file.read()
    expenses = content.strip("\n").split("\n")
    assert str(expense) == expenses[-1]

    with open("src/repository/test.txt", 'w') as file:
        file.write("")


def test_add_entry_binary():
    """
    Method to test the add_entry method
    :return:
    """
    bin_rep = BinaryFileRepository()
    expense = Expense(10, 1000, "food")
    bin_rep.add_entry(expense, "src/repository/test.txt")
    assert expense in bin_rep.get_records()

    prev = Expense(1, 1, "fodder")

    with open("src/repository/test.txt", 'rb') as file:
        try:
            while True:
                content = pickle.load(file)
                prev = content
        except EOFError:
            pass
    assert expense == prev

    with open("src/repository/test.txt", 'wb') as file:
        file.write(b"")
