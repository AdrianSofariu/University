import unittest
from src.board.board import Board
from colorama import Fore, Style


class TestBoard(unittest.TestCase):
    """
    This class tests methods of the board class
    """

    def setUp(self):
        self.board = Board()

    def test_get_position(self):
        """
        Test if the get_position method returns the symbol from the given position
        """
        position = 1
        symbol = "w"
        self.board.set_position(position, symbol)
        self.assertEqual(self.board.get_position(position), symbol)

    def test_set_position(self):
        """
        Test if the set_position method sets the position equal to the given symbol
        """
        position = 2
        symbol = "b"
        self.board.set_position(position, symbol)
        self.assertEqual(self.board.get_position(position), symbol)

    def test_get_mills(self):
        """
        Test if the get_mills method returns the list of 16 tuples
        """
        mills = self.board.get_mills()
        self.assertIsInstance(mills, list)
        self.assertEqual(len(mills), 16)

    def test_get_neighbours(self):
        """
        Test if the get_neighbours method correctly returns the list of pairs which build a mill together with the given
        position
        """
        position = 3
        neighbours = self.board.get_neighbours(position)
        self.assertIsInstance(neighbours, list)
        self.assertEqual(len(neighbours), 2)
        self.assertEqual(len(neighbours[0]), 2)

        position = 16
        neighbours = self.board.get_neighbours(position)
        self.assertEqual(len(neighbours), 2)
        self.assertEqual(len(neighbours[0]), 2)

    def test_get_adjacent(self):
        """
        Test if the get_adjacent method returns the adjacent positions of the given position
        """
        position = 4
        adjacent = self.board.get_adjacent(position)
        self.assertIsInstance(adjacent, list)
        self.assertEqual(len(adjacent), 3)

        position = 14
        adjacent = self.board.get_adjacent(position)
        self.assertIsInstance(adjacent, list)
        self.assertEqual(len(adjacent), 4)

    def test_color_symbol(self):
        """
        Test if the color coding for player and cpu works
        """
        position = 5
        symbol = "b"
        self.board.set_position(position, symbol)
        colored_symbol = self.board.color_symbol(position)
        self.assertIsInstance(colored_symbol, str)
        self.assertEqual(colored_symbol, f"{Fore.RED}{symbol}{Style.RESET_ALL}")

        symbol = "w"
        self.board.set_position(position, symbol)
        colored_symbol = self.board.color_symbol(position)
        self.assertIsInstance(colored_symbol, str)
        self.assertEqual(colored_symbol, f"{Fore.GREEN}{symbol}{Style.RESET_ALL}")

