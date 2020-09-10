# Iain Sheerin
# 1/21/19
# CS76 HW3
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from AlphaBetaAI_Qsearch import AlphaBetaAIQSearch

player1 = AlphaBetaAIQSearch(4, True, True, 1)
player2 = HumanPlayer()
player3 = AlphaBetaAI(4, True, True)


# Example 1, AlphaBetaAI captures pieces even though not good
game = ChessGame(player1, player2)
game.board.clear_board()
game.board.set_piece_at(3, chess.Piece(4, True))
game.board.set_piece_at(6, chess.Piece(6, True))
game.board.set_piece_at(11, chess.Piece(5, True))
game.board.set_piece_at(13, chess.Piece(1, True))
game.board.set_piece_at(22, chess.Piece(1, True))
game.board.set_piece_at(15, chess.Piece(1, True))
game.board.set_piece_at(19, chess.Piece(4, True))
game.board.set_piece_at(43, chess.Piece(5, False))
game.board.set_piece_at(47, chess.Piece(1, False))
game.board.set_piece_at(51, chess.Piece(4, False))
game.board.set_piece_at(52, chess.Piece(2, False))
game.board.set_piece_at(53, chess.Piece(1, False))
game.board.set_piece_at(54, chess.Piece(1, False))
game.board.set_piece_at(57, chess.Piece(3, False))
game.board.set_piece_at(59, chess.Piece(4, False))
game.board.set_piece_at(62, chess.Piece(6, False))

# while not game.is_game_over():
#   print(game)
#   game.make_move()

# Example 2, AlphaBetaAIQSearch does not capture pieces
game = ChessGame(player1, player2)
game.board.clear_board()
game.board.set_piece_at(3, chess.Piece(4, True))
game.board.set_piece_at(6, chess.Piece(6, True))
game.board.set_piece_at(11, chess.Piece(5, True))
game.board.set_piece_at(13, chess.Piece(1, True))
game.board.set_piece_at(22, chess.Piece(1, True))
game.board.set_piece_at(15, chess.Piece(1, True))
game.board.set_piece_at(19, chess.Piece(4, True))
game.board.set_piece_at(43, chess.Piece(5, False))
game.board.set_piece_at(47, chess.Piece(1, False))
game.board.set_piece_at(51, chess.Piece(4, False))
game.board.set_piece_at(52, chess.Piece(2, False))
game.board.set_piece_at(53, chess.Piece(1, False))
game.board.set_piece_at(54, chess.Piece(1, False))
game.board.set_piece_at(57, chess.Piece(3, False))
game.board.set_piece_at(59, chess.Piece(4, False))
game.board.set_piece_at(62, chess.Piece(6, False))

# while not game.is_game_over():
#    print(game)
#    game.make_move()

# Example 3, AlphaBetaAIQsearch stops mate even though black queen piece is not protected
game = ChessGame(player1, player2)
game.board.clear_board()
game.board.set_piece_at(1, chess.Piece(6, True))
game.board.set_piece_at(57, chess.Piece(6, False))
game.board.set_piece_at(58, chess.Piece(4, False))
game.board.set_piece_at(49, chess.Piece(1, False))
game.board.set_piece_at(50, chess.Piece(1, False))
game.board.set_piece_at(48, chess.Piece(1, False))
game.board.set_piece_at(8, chess.Piece(1, True))
game.board.set_piece_at(9, chess.Piece(1, True))
game.board.set_piece_at(10, chess.Piece(1, True))
game.board.set_piece_at(4, chess.Piece(2, True))
game.board.set_piece_at(7, chess.Piece(4, False))
game.board.set_piece_at(33, chess.Piece(5, False))
game.board.set_piece_at(34, chess.Piece(5, True))

while not game.is_game_over():
    print(game)
    game.make_move()
