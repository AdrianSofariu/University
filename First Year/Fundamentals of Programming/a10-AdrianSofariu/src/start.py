from src.board.board import Board
from src.service.game_service import GameService
from src.ui.ui import UI

board = Board()
game_service = GameService(board)
ui = UI(game_service)


ui.start()
