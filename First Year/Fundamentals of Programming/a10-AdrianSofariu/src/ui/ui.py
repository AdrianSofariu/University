from src.service.game_service import GameService, InvalidMoveException


class UI:

    def __init__(self, gs: GameService):
        self.__game_service = gs

    def start(self):
        print(self.__game_service.print_board())
        self.placing_phase()

    def check_input(self, location: str):
        """
        Checks if the input of the player is correct for a piece placement
        if the location is not numeric InvalidMoveException will
        be raised
        :param location: string representing the location of the placement
        :return: if the location is valid, an integer version of it will be returned
        """
        if not location.isnumeric():
            raise InvalidMoveException("!!Please input a valid position!!")
        else:
            position = int(location)
            return position

    def placing_phase(self):
        """
        This procedure places the 9 pieces of the player according to their input
        Each time the player inputs a piece, the ai will also place one
        After the player has placed all the pieces, the game will move to the next phase
        After each placement, the board will be printed again
        """
        to_place = 9
        while to_place > 0:
            try:

                # player places piece on board
                location = input("Where do you want to place your piece: ")
                position = self.check_input(location)
                self.__game_service.place_piece('w', position)

                # show board
                print("PLAYER TURN")
                print(self.__game_service.print_board())

                # check if player needs to remove enemy piece
                completed_mills = self.__game_service.check_mill(position, 'w')

                # remove pieces if we completed mills
                if completed_mills != 0:
                    self.remove_piece(completed_mills)

                # enemy also places a piece and removes if mills are completed
                self.__game_service.cpu_place_piece()

                # show board
                print("CPU TURN")
                print(self.__game_service.print_board())

                # 1 less piece to place
                to_place -= 1
            except InvalidMoveException as e:
                print(e)
        # continue to moving phase
        self.moving_phase()

    def moving_phase(self):
        """
        This procedure handles the rest of the game
        The player and the cpu will move one piece per turn until one of them remains with 2 pieces,
        at which point the game ends
        """
        player_piece_count = self.__game_service.get_player_piece_count()
        cpu_piece_count = self.__game_service.get_ai_piece_count()

        # while players can still build mills
        while player_piece_count > 2 and cpu_piece_count > 2:
            # make player move
            position = self.make_move()

            # show board
            print("PLAYER TURN")
            print(self.__game_service.print_board())

            if position != -1:
                # check if player needs to remove enemy piece
                completed_mills = self.__game_service.check_mill(position, 'w')
            else:
                completed_mills = 0

            # remove pieces if we completed mills
            if completed_mills != 0:
                self.remove_piece(completed_mills)
                # update cpu piece count
                cpu_piece_count = self.__game_service.get_ai_piece_count()
                if cpu_piece_count == 2:
                    break

            # enemy also moves a piece and removes if mills are completed
            self.__game_service.cpu_make_move()
            # update player piece count
            player_piece_count = self.__game_service.get_player_piece_count()

            # show board
            print("CPU TURN")
            print(self.__game_service.print_board())
        if player_piece_count == 2:
            print("CPU WINS")
        else:
            print("PLAYER WINS")

    def remove_piece(self, mills_formed: int):
        """
        Handles the input in case a mill was formed and enemy pieces need to be removed
        :return:
        """
        # remove as many enemy pieces as mills completed in this turn
        while mills_formed > 0:
            # get the cpu's removable pieces
            removable = self.__game_service.get_removable_pieces('b')
            # display them
            if len(removable) != 0:
                print("The pieces from the following positions can be removed: ")
                print(str(removable)[1:-1])
                try:
                    # get input
                    to_remove = input("Please choose a piece to remove: ")
                    # check if it is numeric
                    position = self.check_input(to_remove)

                    # check that the position is indeed a removable enemy piece
                    if position not in removable:
                        raise InvalidMoveException("!!Please input a valid position!!")

                    # remove it
                    self.__game_service.remove_position(position)
                    mills_formed -= 1
                    print("PLAYER REMOVED A PIECE")
                    print(self.__game_service.print_board())
                except InvalidMoveException as e:
                    print(e)
            else:
                print("No pieces can be removed!")
                mills_formed = 0

    def make_move(self) -> int:
        """
        Receives input from the user to make a move
        :param self:
        :return: position where the piece was placed/ -1 if all pieces are blocked which is unrealistic
        """
        possible_moves = self.__game_service.possible_moves('w', self.__game_service.get_player_piece_count())

        # if we can move
        if len(possible_moves) != 0:
            # provide player with a set of movable pieces
            movable_pieces = list(possible_moves.keys())
            print("These are the pieces you can move.")
            print(str(movable_pieces)[1:-1])

            # make sure he makes 1 valid move
            moves = 1
            while moves > 0:
                try:
                    # let him a choose a piece
                    piece = input("Choose a piece you would like to move: ")
                    to_move = self.check_input(piece)
                    if to_move not in movable_pieces:
                        raise InvalidMoveException("!!Please choose a valid piece!!")

                    # show him the available moves for the chosen piece
                    valid_moves = possible_moves[to_move]
                    print("These are the possible moves.")
                    print(str(valid_moves)[1:-1])

                    # let him choose a move
                    move = input("Choose a move: ")
                    position = self.check_input(move)
                    if position not in valid_moves:
                        raise InvalidMoveException("!!Please choose a valid move!!")

                    # make the move
                    self.__game_service.move_piece(to_move, position)
                    moves -= 1
                    return position
                except InvalidMoveException as e:
                    print(e)
        else:
            print("Player cannot move")
            return -1
