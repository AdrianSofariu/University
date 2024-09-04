import unittest
from src.service.game_service import GameService, InvalidMoveException
from src.board.board import Board


class TestGameService(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.game_service = GameService(self.board)

    def test_get_player_piece_count(self):
        """
        Test if the initial player piece count is 9
        """
        player_count = self.game_service.get_player_piece_count()
        self.assertEqual(player_count, 9)

    def test_get_ai_piece_count(self):
        """
        Test if the initial cpu piece count is 9
        """
        ai_count = self.game_service.get_ai_piece_count()
        self.assertEqual(ai_count, 9)

    def test_place_piece(self):
        """
        Test if the piece is placed correctly
        """
        self.game_service.clear_board()

        self.game_service.place_piece('w', 1)
        self.assertEqual(self.board.get_position(1), 'w')

        self.assertRaises(InvalidMoveException, self.game_service.place_piece, 'b', 1)
        self.assertRaises(InvalidMoveException, self.game_service.place_piece, 'w', 24)
        self.game_service.clear_board()

    def test_check_mill(self):
        """
        Test if the program correctly identifies a new mill
        """
        self.game_service.clear_board()

        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 2)
        is_mill = self.game_service.check_mill(1, 'w')
        self.assertEqual(is_mill, 1)

        self.game_service.place_piece('w', 3)
        self.game_service.place_piece('w', 5)
        is_mill = self.game_service.check_mill(3, 'w')
        self.assertEqual(is_mill, 1)

        self.game_service.clear_board()

        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 2)
        self.game_service.place_piece('w', 3)
        self.game_service.place_piece('w', 5)
        self.game_service.place_piece('w', 0)
        is_mill = self.game_service.check_mill(0,'w')
        self.assertEqual(is_mill, 2)
        self.game_service.clear_board()

    def test_check_incomplete_mill(self):
        """
        Test if the game correctly identifies an incomplete mill
        """
        self.game_service.clear_board()

        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('x', 2)
        position_which_completes = self.game_service.check_incomplete_mill((0, 1, 2), 'w')
        self.assertEqual(position_which_completes, 2)

        self.game_service.place_piece('b', 2)
        position_which_completes = self.game_service.check_incomplete_mill((0, 1, 2), 'w')
        self.assertEqual(position_which_completes, -1)
        self.game_service.clear_board()

    def test_check_position(self):
        """
        Check if the game correctly returns the value at a given position
        """
        self.game_service.clear_board()

        self.game_service.place_piece('w', 1)
        position_status = self.game_service.check_position(1)
        self.assertEqual(position_status, 'w')

        self.game_service.clear_board()

    def test_remove_position(self):
        """
        Check if the game correctly removes a piece from the game
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 1)
        self.game_service.remove_position(1)
        self.assertEqual(self.game_service.check_position(1), 'x')
        self.assertEqual(self.game_service.get_player_piece_count(), 8)
        self.game_service.clear_board()

    def test_check_in_mill(self):
        """
        Check if the game correctly identifies when a piece is part of a mill and when not
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 2)
        self.game_service.place_piece('w', 5)
        is_in_mill = self.game_service.check_in_mill(1, 'w')
        self.assertTrue(is_in_mill)
        is_in_mill = self.game_service.check_in_mill(5, 'w')
        self.assertFalse(is_in_mill)
        self.game_service.clear_board()

    def test_check_in_incomplete_mill(self):
        """
        Check if the game correctly identifies when a piece is part of an incomplete mill
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('b', 1)
        self.game_service.place_piece('w', 2)
        self.game_service.place_piece('b', 3)
        self.game_service.place_piece('w', 4)
        self.game_service.place_piece('w', 5)
        self.game_service.place_piece('w', 7)
        is_in_incomplete_mill = self.game_service.check_in_incomplete_mill(0, 'w')
        self.assertFalse(is_in_incomplete_mill)
        is_in_incomplete_mill = self.game_service.check_in_incomplete_mill(5, 'w')
        self.assertTrue(is_in_incomplete_mill)
        is_in_incomplete_mill = self.game_service.check_in_incomplete_mill(7, 'w')
        self.assertTrue(is_in_incomplete_mill)
        is_in_incomplete_mill = self.game_service.check_in_incomplete_mill(4, 'w')
        self.assertFalse(is_in_incomplete_mill)
        self.game_service.clear_board()

    def test_get_removable_pieces(self):
        """
        Tests if the game can identify the removable pieces
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 2)
        self.game_service.place_piece('w', 3)
        removable_pieces = self.game_service.get_removable_pieces('w')
        self.assertEqual(removable_pieces, [3])
        self.game_service.clear_board()

    def test_get_priority_removal(self):
        """
        Tests if the game can identify all pieces inside incomplete mills
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 2)
        self.game_service.place_piece('b', 0)
        self.game_service.place_piece('w', 7)

        priority_removal = self.game_service.get_priority_removal('w')
        self.assertEqual(priority_removal, [2, 7])
        self.game_service.clear_board()

    def test_cpu_place_piece(self):
        """
        Tests if the cpu places a piece following the next strategy:
        1. if he can, he completes a mill -> he will also remove a piece (the ones in incomplete mills have priority,
        but this is not tested here)
        2. if he can't do 1, he will block the player if he can
        3. if not, random move
        :return:
        """
        # case 1 - complete his mill
        self.game_service.clear_board()
        self.game_service.place_piece('b', 0)
        self.game_service.place_piece('b', 2)
        self.game_service.cpu_place_piece()
        self.assertIn(self.game_service.check_position(1), 'b')
        self.game_service.clear_board()

        # case 2 - block opponent
        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('w', 1)
        self.game_service.cpu_place_piece()
        self.assertIn(self.game_service.check_position(2), 'b')
        self.game_service.clear_board()

        # case 3 - random
        self.game_service.cpu_place_piece()
        count = 0
        for i in range(0, 24):
            if self.game_service.check_position(i) == 'b':
                count += 1
        self.assertEqual(count, 1)
        self.game_service.clear_board()

    def test_get_incomplete_mills(self):
        """
        Test if the game can successfully identify incomplete mills
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 0)
        positions, incomplete_mills = self.game_service.get_incomplete_mills('w')
        self.assertIn(2, positions)
        self.assertIn((0, 1, 2), incomplete_mills)
        self.game_service.clear_board()

        self.game_service.place_piece('w', 5)
        self.game_service.place_piece('w', 6)
        self.game_service.place_piece('b', 7)
        positions, incomplete_mills = self.game_service.get_incomplete_mills('w')
        self.assertEqual(len(positions), 0)
        self.assertEqual(len(incomplete_mills), 0)
        self.game_service.clear_board()

    def test_cpu_remove_piece(self):
        """
        Test if the cpu can remove a piece. Pieces in incomplete mills have priority.
        """
        # remove piece with priority
        self.game_service.clear_board()
        self.game_service.place_piece('w', 5)
        self.game_service.place_piece('w', 6)
        self.game_service.cpu_remove_piece(1)
        self.assertEqual(self.game_service.check_position(5), 'x')
        self.game_service.clear_board()

        # remove normal piece
        self.game_service.place_piece('w', 5)
        self.game_service.place_piece('w', 0)
        self.game_service.cpu_remove_piece(1)
        self.assertEqual(self.game_service.check_position(0), 'x')
        self.game_service.clear_board()

        # exhaust priority pieces and swap to normal removal by removing 2 pieces, where 1 is prioritary and one not
        self.game_service.place_piece('w', 5)
        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('w', 6)
        self.game_service.cpu_remove_piece(2)
        self.assertEqual(self.game_service.check_position(0), 'x')
        self.assertEqual(self.game_service.check_position(5), 'x')
        self.game_service.clear_board()

    def test_possible_moves(self):
        """
        Test if the game can figure out which pieces can move and how
        Test first for normal move
        Test second for jump
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 0)

        # test for normal move
        possible_moves = self.game_service.possible_moves('w', 9)
        self.assertEqual(possible_moves[0], [1, 3])

        # test for jumps
        possible_moves = self.game_service.possible_moves('w', 3)
        self.assertEqual(len(possible_moves[0]), 23)
        self.game_service.clear_board()

    def test_is_movable(self):
        """
        Test if the game can recognize where a piece can move (normal move)
        :return:
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 0)
        moves = self.game_service.is_movable(0)
        self.assertEqual(moves, [1, 3])

        self.game_service.place_piece('w', 3)
        self.game_service.place_piece('w', 1)
        moves = self.game_service.is_movable(0)
        self.assertEqual(moves, [])

        self.game_service.clear_board()

    def test_move_piece(self):
        """
        Test moving a piece
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 1)
        self.game_service.move_piece(1, 2)

        self.assertEqual(self.game_service.check_position(1), 'x')
        self.assertEqual(self.game_service.check_position(2), 'w')
        self.game_service.clear_board()

    def test_all_pieces(self):
        """
        Test if the game can find all pieces of a certain symbol
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 3)
        self.game_service.place_piece('w', 15)
        all_pieces = self.game_service.all_pieces('w')
        self.assertEqual(all_pieces, [1, 3, 15])
        self.game_service.clear_board()

    def test_cpu_make_move(self):
        """
        Test if the cpu can move his pieces according to a certain strategy (we test here only normal movement)
        First, test if he can close a mill and remove a piece (which is not tested here)
        Second, test if he can block the opponent
        Third, if he cannot do either one, move random
        :return:
        """

        # test closing a mill
        self.game_service.clear_board()
        self.game_service.place_piece('w', 0)
        self.game_service.place_piece('b', 3)
        self.game_service.place_piece('b', 6)
        self.game_service.place_piece('b', 7)
        self.game_service.cpu_make_move()
        self.assertEqual(self.game_service.check_position(5), 'b')
        self.assertEqual(self.game_service.check_position(0), 'x')
        self.game_service.clear_board()

        # test blocking a mill
        self.game_service.place_piece('b', 3)
        self.game_service.place_piece('w', 6)
        self.game_service.place_piece('w', 7)
        self.game_service.cpu_make_move()
        self.assertEqual(self.game_service.check_position(5), 'b')
        self.game_service.clear_board()

        # test random move
        self.game_service.place_piece('b', 0)
        self.game_service.place_piece('b', 3)
        self.game_service.cpu_make_move()
        positions = []
        for i in range(0, 24):
            if self.game_service.check_position(i) == 'b':
                positions.append(i)
        self.assertNotEqual([0, 3], positions)
        self.game_service.clear_board()

    def test_build(self):
        """
        Test if the cpu can complete a mill
        We can test here jumps, as build is a subprogram of the cpu_make_move procedure
        """
        self.game_service.clear_board()
        self.game_service.place_piece('w', 14)
        self.game_service.place_piece('b', 22)
        self.game_service.place_piece('b', 1)
        self.game_service.place_piece('b', 2)

        # create possible jumps
        possible_moves = self.game_service.possible_moves('b', 3)
        # test if he will complete the mill with a jump

        done = self.game_service.build(possible_moves)
        self.assertTrue(done)
        self.assertEqual(self.game_service.check_position(0), 'b')
        self.assertEqual(self.game_service.check_position(14), 'x')

        self.game_service.clear_board()
        # now test the opposite
        self.game_service.place_piece('b', 22)
        self.game_service.place_piece('b', 10)
        self.game_service.place_piece('b', 2)

        possible_moves = self.game_service.possible_moves('b', 3)
        done = self.game_service.build(possible_moves)
        self.assertFalse(done)
        self.game_service.clear_board()

    def test_block(self):
        """
        Test if the cpu can block a mill
        We can test here jumps, as block is a subprogram of the cpu_make_move procedure
        :return:
        """
        self.game_service.clear_board()
        self.game_service.place_piece('b', 22)
        self.game_service.place_piece('w', 1)
        self.game_service.place_piece('w', 2)

        # create possible jumps
        possible_moves = self.game_service.possible_moves('b', 3)
        # test if he will complete the mill with a jump

        done = self.game_service.block(possible_moves)
        self.assertTrue(done)
        self.assertEqual(self.game_service.check_position(0), 'b')

        self.game_service.clear_board()
        # now test the opposite
        self.game_service.place_piece('b', 2)

        possible_moves = self.game_service.possible_moves('b', 3)
        done = self.game_service.block(possible_moves)
        self.assertFalse(done)
        self.game_service.clear_board()

    def test_check_move_to_positions(self):
        """
        Check if we can move a piece in one of the given positions
        We test with and without jumps
        """
        self.game_service.clear_board()

        # without jumps
        self.game_service.place_piece('b', 2)
        self.game_service.place_piece('b', 6)
        destinations = [0, 4, 5]

        possible_moves = self.game_service.possible_moves('b', 9)
        move_to_positions = self.game_service.check_move_to_positions(possible_moves, destinations)
        self.assertEqual(move_to_positions, (2, 4))

        # with jumps
        possible_moves = self.game_service.possible_moves('b', 3)
        move_to_positions = self.game_service.check_move_to_positions(possible_moves, destinations)
        self.assertEqual(move_to_positions, (2, 0))

        # move not possible
        destinations = [10]
        possible_moves = self.game_service.possible_moves('b', 9)
        move_to_positions = self.game_service.check_move_to_positions(possible_moves, destinations)
        self.assertEqual(move_to_positions, (-1, -1))
        self.game_service.clear_board()

    def test_check_can_build_mill(self):
        """
        Test if the game can find a move that completes a mill
        This is a variation of check_move_to_positions function, so we test in a similar manner
        """

        self.game_service.clear_board()

        # without jumps
        self.game_service.place_piece('b', 3)
        self.game_service.place_piece('b', 1)
        self.game_service.place_piece('b', 2)
        destinations, mills = self.game_service.get_incomplete_mills('b')

        possible_moves = self.game_service.possible_moves('b', 9)
        move_to_positions = self.game_service.check_can_build_mill(possible_moves, destinations, mills)
        self.assertEqual(move_to_positions, (3, 0))
        self.game_service.clear_board()

        # with jumps
        self.game_service.place_piece('b', 10)
        self.game_service.place_piece('b', 1)
        self.game_service.place_piece('b', 2)

        possible_moves = self.game_service.possible_moves('b', 3)
        move_to_positions = self.game_service.check_can_build_mill(possible_moves, destinations, mills)
        self.assertEqual(move_to_positions, (10, 0))
        self.game_service.clear_board()

        # cannot complete any mill
        self.game_service.place_piece('b', 10)
        self.game_service.place_piece('b', 1)
        self.game_service.place_piece('b', 2)

        possible_moves = self.game_service.possible_moves('b', 9)
        move_to_positions = self.game_service.check_can_build_mill(possible_moves, destinations, mills)
        self.assertEqual(move_to_positions, (-1, -1))
        self.game_service.clear_board()
