from colorama import Fore, Style


class Board:

    def __init__(self):
        """
        Initialize empty board with 24 'x' characters
        """
        self.__board = []
        for i in range(24):
            self.__board.append('x')
        # Declare the tuples of 3 fields that can build valid mills
        self.__mills = [(0, 1, 2),
                        (2, 4, 7),
                        (0, 3, 5),
                        (5, 6, 7),
                        (8, 9, 10),
                        (10, 12, 15),
                        (13, 14, 15),
                        (8, 11, 13),
                        (16, 17, 18),
                        (18, 20, 23),
                        (21, 22, 23),
                        (16, 19, 21),
                        (1, 9, 17),
                        (4, 12, 20),
                        (3, 11, 19),
                        (6, 14, 22)]
        self.__neighbours = {
            0: [(1, 2), (3, 5)],
            1: [(0, 2), (9, 17)],
            2: [(0, 1), (4, 7)],
            3: [(0, 5), (11, 19)],
            4: [(2, 7), (12, 20)],
            5: [(0, 3), (6, 7)],
            6: [(5, 7), (14, 22)],
            7: [(2, 4), (6, 5)],
            8: [(9, 10), (11, 13)],
            9: [(8, 10), (1, 17)],
            10: [(8, 9), (12, 15)],
            11: [(8, 13), (3, 19)],
            12: [(10, 15), (4, 20)],
            13: [(8, 11), (14, 15)],
            14: [(13, 15), (6, 22)],
            15: [(10, 12), (14, 13)],
            16: [(17, 18), (19, 21)],
            17: [(16, 18), (9, 1)],
            18: [(16, 17), (20, 23)],
            19: [(16, 21), (11, 3)],
            20: [(18, 23), (12, 4)],
            21: [(19, 16), (22, 23)],
            22: [(14, 6), (23, 21)],
            23: [(20, 18), (21, 22)]
        }
        self.__adjacent = {
            0: [1, 3],
            1: [0, 2, 9],
            2: [1, 4],
            3: [0, 5, 11],
            4: [2, 7, 12],
            5: [3, 6],
            6: [5, 7, 14],
            7: [4, 6],
            8: [9, 11],
            9: [1, 8, 10, 17],
            10: [9, 12],
            11: [3, 8, 13, 19],
            12: [4, 10, 15, 20],
            13: [11, 14],
            14: [6, 13, 15, 22],
            15: [12, 14],
            16: [17, 19],
            17: [9, 16, 18],
            18: [17, 20],
            19: [11, 16, 21],
            20: [12, 18, 23],
            21: [19, 22],
            22: [14, 21, 23],
            23: [20, 22],
        }

    def get_position(self, position: int) -> str:
        """
        Return the piece placed at the given position
        :param position: integer signaling the position
        :return: str representing the piece placed at the given position ('w' - player, 'b' - ai, 'x' - empty)
        """
        return self.__board[position]

    def set_position(self, position: int, symbol: str):
        """
        Place a piece at the given position on the board
        :param position: integer signaling where to place the piece
        :param symbol: piece to be placed
        """
        self.__board[position] = symbol

    def get_mills(self) -> list:
        """
        Return the list of tuples representing the fields that can build mills
        :return: list
        """
        return self.__mills

    def get_neighbours(self, position) -> list:
        """
        Return the list of neighbouring positions for the given position
        :param position:
        :return:
        """
        return self.__neighbours[position]

    def get_adjacent(self, position) -> list:
        """
        Return the list of adjacent nodes for the given position
        :param position:
        :return:
        """
        return self.__adjacent[position]

    def color_symbol(self, position: int) -> str:
        if self.__board[position] == 'w':
            return f"{Fore.GREEN}w{Style.RESET_ALL}"
        elif self.__board[position] == 'b':
            return f"{Fore.RED}b{Style.RESET_ALL}"
        else:
            return 'x'

    def clear(self):
        """
        Clear the board
        """
        for i in range(0, 24):
            self.__board[i] = 'x'

    def __str__(self):
        """
        Print the board as a string
        """
        return (self.color_symbol(0) + "(00)----------------------" + self.color_symbol(1) +
                "(01)----------------------" + self.color_symbol(2) + "(02)\n" +
                "|                           |                           |\n"
                + "|                           |                           |\n"
                + "|                           |                           |\n"
                + "|       " + self.color_symbol(8) + "(08)--------------" +
                self.color_symbol(9) + "(09)--------------" + self.color_symbol(10) + "(10)     |\n"
                + "|       |                   |                    |      |\n"
                + "|       |                   |                    |      |\n"
                + "|       |                   |                    |      |\n"
                + "|       |        " + self.color_symbol(16) + "(16)-----" +
                self.color_symbol(17) + "(17)-----" + self.color_symbol(18) + "(18)       |      |\n"
                + "|       |         |                   |          |      |\n"
                + "|       |         |                   |          |      |\n"
                + "|       |         |                   |          |      |\n"
                + self.color_symbol(3) + "(03)---" + self.color_symbol(11) + "(11)----" + self.color_symbol(19)
                + "(19)               " + self.color_symbol(20) + "(20)----" + self.color_symbol(12)
                + "(12)---" + self.color_symbol(4) + "(04)\n"
                + "|       |         |                   |          |      |\n"
                + "|       |         |                   |          |      |\n"
                + "|       |         |                   |          |      |\n"
                + "|       |        " + self.color_symbol(21) + "(21)-----" +
                self.color_symbol(22) + "(22)-----" + self.color_symbol(23) + "(23)       |      |\n"
                + "|       |                   |                    |      |\n"
                + "|       |                   |                    |      |\n"
                + "|       |                   |                    |      |\n"
                + "|       " + self.color_symbol(13) + "(13)--------------" +
                self.color_symbol(14) + "(14)--------------" + self.color_symbol(15) + "(15)     |\n"
                + "|                           |                           |\n"
                + "|                           |                           |\n"
                + "|                           |                           |\n"
                + self.color_symbol(5) + "(05)----------------------" + self.color_symbol(6) +
                "(06)----------------------" + self.color_symbol(7) + "(07)\n")

