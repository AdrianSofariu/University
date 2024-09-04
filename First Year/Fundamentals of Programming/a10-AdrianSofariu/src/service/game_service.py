import random

from src.board.board import Board


class InvalidMoveException(Exception):
    pass


class GameService:

    def __init__(self, board: Board):
        self.__board = board
        self.__current_game_state = 0
        self.__player_piece_count = 9
        self.__ai_piece_count = 9

    def clear_board(self):
        """
        Clears the board of all pieces
        """
        self.__board.clear()

    def get_player_piece_count(self) -> int:
        """
        Returns the player piece count
        :return: player_piece_count
        """
        return self.__player_piece_count

    def get_ai_piece_count(self) -> int:
        """
        Returns the ai piece count
        :return: ai_piece_count
        """
        return self.__ai_piece_count

    def print_board(self) -> str:
        """
        Return the printable board
        """
        return str(self.__board)

    def place_piece(self, piece: str, position: int):
        """
        Place piece on the board
        if the location is out of bounds or aims to overwrite another piece, InvalidMoveException will
        be raised
        :param piece: symbol of the piece ('w', 'b', 'x')
        :param position: location to place the piece on the board
        """
        if position < 0 or position > 23:
            raise InvalidMoveException("!!Please input a valid position!!")
        else:
            symbol_at_position = self.check_position(position)
            if symbol_at_position != 'x':
                raise InvalidMoveException("!!Please input a valid position!!")
            self.__board.set_position(position, piece)

    def check_mill(self, location: int, symbol: str):
        """
        Check if a new mill was formed at the location of the move
        :param symbol: player or cpu
        :param location:
        :return: number of mills formed
        """
        ct = 0
        mills = self.__board.get_mills()
        for mill in mills:
            if location in mill:
                if self.__board.get_position(mill[0]) == self.__board.get_position(mill[1]) == self.__board.get_position(mill[2]) == symbol:
                    ct += 1
        return ct

    def check_incomplete_mill(self, mill: tuple, symbol: str) -> int:
        """
        Check if a mill can be completed
        :param symbol: player/cpu pieces
        :param mill: tuple of 3 positions that form a mill
        :return: position which completes the mill
        """
        if (self.__board.get_position(mill[0]) == self.__board.get_position(mill[1]) == symbol and
                self.__board.get_position(mill[2]) == 'x'):
            return mill[2]
        if (self.__board.get_position(mill[0]) == self.__board.get_position(mill[2]) == symbol and
                self.__board.get_position(mill[1]) == 'x'):
            return mill[1]
        if (self.__board.get_position(mill[1]) == self.__board.get_position(mill[2]) == symbol and
                self.__board.get_position(mill[0]) == 'x'):
            return mill[0]
        return -1

    def check_position(self, position: int) -> str:
        """
        Returns value at location = position on the board
        :param position: int between 0 and 23
        :return:
        """
        return self.__board.get_position(position)

    def remove_position(self, position: int):
        """
        Resets the position to the default value 'x'
        According to the symbol removed, a piece will be deducted from player/cpu piece count
        :param position: int between 0 and 23
        """
        symbol = self.check_position(position)
        self.__board.set_position(position, 'x')
        if symbol == 'w':
            self.__player_piece_count -= 1
        elif symbol == 'b':
            self.__ai_piece_count -= 1

    def check_in_mill(self, position: int, symbol: str) -> bool:
        """
        Check if a piece is part of any mill
        :param position: piece location
        :param symbol: player/cpu pieces
        :return: true if part of a mill, false otherwise
        """
        ok = False
        mills = self.__board.get_mills()
        for mill in mills:
            if position in mill:
                if self.__board.get_position(mill[0]) == self.__board.get_position(mill[1]) == self.__board.get_position(mill[2]) == symbol:
                    ok = True
        return ok

    def check_in_incomplete_mill(self, position: int, symbol: str) -> bool:
        """
        Check if a piece is part of any 2-piece wannabe mill
        :param position: piece location
        :param symbol: player/cpu pieces
        :return: true if part of an incomplete mill, false otherwise
        """
        ok = False
        mills = self.__board.get_mills()
        for mill in mills:
            location = -1
            # find the position in the mill
            for i in range(0, 3):
                if position == mill[i]:
                    location = i
                    break
            # if position is in mill, check if it is an incomplete one
            if location != -1:
                if location == 0:
                    if (self.__board.get_position(mill[0]) == self.__board.get_position(mill[1]) == symbol and
                            self.__board.get_position(mill[2]) == 'x'):
                        ok = True
                    if (self.__board.get_position(mill[0]) == self.__board.get_position(mill[2]) == symbol and
                            self.__board.get_position(mill[1]) == 'x'):
                        ok = True
                if location == 1:
                    if ((self.__board.get_position(mill[0]) == self.__board.get_position(mill[1]) == symbol and
                            self.__board.get_position(mill[2]) == 'x') or
                        (self.__board.get_position(mill[1]) == self.__board.get_position(mill[2]) == symbol and
                            self.__board.get_position(mill[0]) == 'x')):
                        ok = True
                if location == 2:
                    if (self.__board.get_position(mill[1]) == self.__board.get_position(mill[2]) == symbol and
                            self.__board.get_position(mill[0]) == 'x'):
                        ok = True
                    if (self.__board.get_position(mill[0]) == self.__board.get_position(mill[2]) == symbol and
                            self.__board.get_position(mill[1]) == 'x'):
                        ok = True
        return ok

    def get_removable_pieces(self, symbol: str) -> list:
        """
        Returns a list of positions from which pieces can be removed from the board
        A piece can be removed only if it is not part of a mill
        :param symbol: symbol determines if player/cpu pieces should be removed
        :return: list of integers
        """
        removable = []
        # go through all positions
        for i in range(24):
            # handle those with the chosen pieces
            if self.__board.get_position(i) == symbol:
                in_mill = self.check_in_mill(i, symbol)
                if not in_mill:
                    removable.append(i)
        return removable

    def get_priority_removal(self, symbol: str) -> list:
        """
        Returns a list of all removable pieces that are inside incomplete mills
        :param symbol: player/cpu
        :return: list of positions with removable pieces
        """
        removable = []
        # go through all positions
        for i in range(24):
            # handle those with the chosen pieces
            if self.__board.get_position(i) == symbol:
                in_incomplete_mill = self.check_in_incomplete_mill(i, symbol)
                if in_incomplete_mill:
                    removable.append(i)
        return removable

    def cpu_place_piece(self):
        """
        This function determines where the cpu will place the next piece
        First, he checks if he can complete his own mill/s to remove pieces. If he can, he will do it
        Second, he checks if he can block the opponent. If he can, he will do it
        Third, if he cannot do the above actions, he will place a piece randomly on the board in a free position
        """
        # check if the cpu can complete a mill
        completable_mills, fodder = self.get_incomplete_mills('b')
        if len(completable_mills) != 0:
            self.__board.set_position(completable_mills[0], 'b')

            # check how many mills we actually completed
            completed_mills = self.check_mill(completable_mills[0], 'b')

            # remove as many pieces as mills completed
            self.cpu_remove_piece(completed_mills)

        # if we cannot complete, check if we can block the player
        else:
            blockable_mills, fodder = self.get_incomplete_mills('w')
            if len(blockable_mills) != 0:
                self.__board.set_position(blockable_mills[0], 'b')
            # if cant do either, play random
            else:
                # find a valid position
                ok = 0
                while ok == 0:
                    position = random.randint(0, 23)
                    if self.__board.get_position(position) == 'x':
                        ok = 1
                        self.__board.set_position(position, 'b')

    def get_incomplete_mills(self, symbol: str) -> tuple:
        """
        This function returns a list with all position which can complete a mill with the given symbol and
        for each position the corresponding mill in another list
        :param symbol: player/cpu pieces
        :return: a list of positions that will complete a mill with the given symbol and a list of mills
        """
        mills = self.__board.get_mills()
        completable_mills = []
        corresponding_mills = []
        for mill in mills:
            pos = self.check_incomplete_mill(mill, symbol)
            if pos != -1:
                completable_mills.append(pos)
                corresponding_mills.append(mill)
        return completable_mills, corresponding_mills

    def cpu_remove_piece(self, removes: int):
        """
        This procedure removes the given number of player pieces from the board
        It first computes the points that are in incomplete mills and can be removed
        If there are no such points, a random removable point will be chosen
        :param removes: number of pieces to remove
        """
        i = 0
        in_incomplete_mills = self.get_priority_removal('w')
        removable = self.get_removable_pieces('w')

        # create priority removal list
        priority_removal = set(in_incomplete_mills) & set(removable)
        priority_removal = list(priority_removal)

        # create the normal removal list
        normal_removal = set(removable) - set(in_incomplete_mills)
        normal_removal = list(normal_removal)

        while removes > 0:

            # if it is not empty, remove the first element
            if len(priority_removal) != 0:
                if i < len(priority_removal):
                    self.remove_position(priority_removal[i])
                    i += 1
                    removes -= 1
                else:
                    # if we exhaust this list move to normal removal
                    i = 0
                    if len(normal_removal) != 0:
                        self.remove_position(normal_removal[i])
                        removes -= 1
                    else:
                        removes = 0
            # if priority does not exist, use normal
            else:
                if len(normal_removal) != 0:
                    self.remove_position(normal_removal[i])
                    removes -= 1
                else:
                    removes = 0

    def possible_moves(self, symbol: str, piece_count: int) -> dict:
        """
        If piece_count > 3
        =>  returns a dict of positions with the given symbol which have an empty adjacent position
            the key is the position
            the values are the places where the symbol on the key position can be moved
        If piece_count == 3
        =>  returns a dict of positions with the given symbol
            the key is the position
            the values are the empty places where a key can jump
        :param piece_count: number of pieces left for a player
        :param symbol: player/cpu pieces 'w'/'b'
        :return: dict of possible moves
        """
        movables = {}
        if piece_count > 3:
            for i in range(0, 24):
                if self.check_position(i) == symbol:
                    moves = self.is_movable(i)
                    if len(moves) != 0:
                        movables[i] = moves
        elif piece_count == 3:
            pieces = self.all_pieces(symbol)
            destinations = self.all_pieces('x')
            for piece in pieces:
                movables[piece] = destinations
        return movables

    def is_movable(self, position: int) -> list:
        """
        Check if a position has empty adjacent positions
        :param position: int between 0 and 23 (includes 0 and 23)
        :return: the adjacent empty positions in a list
        """
        adjacent = self.__board.get_adjacent(position)
        possible_moves = []
        for value in adjacent:
            if self.check_position(value) == 'x':
                possible_moves.append(value)
        return possible_moves

    def move_piece(self, position: int, destination: int):
        """
        Moves a piece from the position to the destination
        :param position: starting position of the piece
        :param destination: destination position of the piece
        :return:
        """
        symbol = self.check_position(position)
        self.__board.set_position(destination, symbol)
        self.__board.set_position(position, 'x')

    def all_pieces(self, symbol: str) -> list:
        """
        Returns a list of all positions with pieces of a given symbol
        :param symbol: 'w'/'b'/'x' for white, black and empty
        :return: list of integers
        """
        pieces = []
        for i in range(0, 24):
            if self.check_position(i) == symbol:
                pieces.append(i)
        return pieces

    def cpu_make_move(self):
        """
        This function determines the next move of the cpu
        First, he checks if he can build a mill. If he can, he will do it
        Second, he checks if he can block an incomplete mill. If he can, he will do it
        Third, if he cannot do one of the above he makes a random move
        If the cpu has 3 pieces left, he will use jumps
        """
        possible_moves = self.possible_moves('b', self.__ai_piece_count)
        # if cpu can move
        if len(possible_moves) != 0:
            # check if the cpu can build a mill in one move
            result = self.build(possible_moves)
            # if he can't build, try to block
            if not result:
                result = self.block(possible_moves)
                # if he can't block, move random
                if not result:
                    source, destinations = random.choice(list(possible_moves.items()))
                    i = random.randint(0, len(destinations) - 1)
                    self.move_piece(source, destinations[i])

    def build(self, possible_moves: dict) -> bool:
        """
        Check if the cpu can complete a mill with a move, if it can it does it and removes accordingly
        :param self:
        :param possible_moves: dict of possible moves containing the pieces as keys and the possible movements
        as list of values
        :return: true if successful, false otherwise
        """
        completable_mills, mills = self.get_incomplete_mills('b')
        if len(completable_mills) != 0:
            # check if such a move can be done
            move = self.check_can_build_mill(possible_moves, completable_mills, mills)

            # if a move is found, execute it
            if move[0] != -1:
                self.move_piece(move[0], move[1])

                # check how many mills we actually completed
                completed_mills = self.check_mill(move[1], 'b')

                # remove as many pieces as mills completed
                self.cpu_remove_piece(completed_mills)
                return True
            else:
                return False
        return False

    def block(self, possible_moves: dict) -> bool:
        """
        Check if the cpu can block an incomplete mill with a move
        :param self:
        :param possible_moves: dict of possible moves containing the pieces as keys and the possible movements
        as list of values
        :return: true if successful, false otherwise
        """
        blockable_mills, fodder = self.get_incomplete_mills('w')
        if len(blockable_mills) != 0:
            # check if such a move can be done
            move = self.check_move_to_positions(possible_moves, blockable_mills)

            # if it is found, execute it
            if move[0] != -1:
                self.move_piece(move[0], move[1])
                return True
            # if not, return false
            else:
                return False
        return False

    def check_move_to_positions(self, possible_moves: dict, destinations: list) -> tuple:
        """
        Checks if a move can bring a piece of the given symbol in one of the given positions
        :param destinations: a list of destinations
        :param possible_moves: a dict containing all the possible moves that can be executed (key = piece, value = list
        of destinations)
        :return: tuple containing the first available move (source and destination)/ (-1,-1) if not found
        """
        i = 0
        while i != len(destinations):
            for key in possible_moves:
                for value in possible_moves[key]:
                    if value == destinations[i]:
                        return key, destinations[i]
            i += 1
        return -1, -1

    def check_can_build_mill(self, possible_moves: dict, destinations: list, mills: list) -> tuple:
        """
        A variation of the check_move_to_positions method, which takes into account that the moved piece should
        not be in the mill we are trying to build at the destination, if the destinations list is a list of positions
        that would complete a mill
        :param possible_moves: a dict containing all the possible moves that can be executed
        :param destinations: a list of points that complete a mill
        :param mills: a list of mills corresponding to the destination point, this means destinations[i] in mills[i]
        :return: tuple containing the move that completes the mill/ (-1,-1) if not possible
        """
        i = 0
        while i != len(destinations):
            for key in possible_moves:
                for value in possible_moves[key]:
                    if value == destinations[i] and key not in mills[i]:
                        return key, destinations[i]
            i += 1
        return -1, -1
