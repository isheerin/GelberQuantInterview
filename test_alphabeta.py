# Iain Sheerin
# 1/21/19
# CS76 HW3
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame

player1 = AlphaBetaAI(4, True, True)
player2 = HumanPlayer()
player3 = MinimaxAI(4, True, True)

# Example 1, AlphaBetaAI has mate in one as white
game = ChessGame(player1, player2)
game.board.clear_board()
game.board.set_piece_at(0, chess.Piece(6, False))
game.board.set_piece_at(17, chess.Piece(6, True))
game.board.set_piece_at(15, chess.Piece(5, True))

while not game.is_game_over():
    print(game)
    game.make_move()

# Example 2, MinimaxAI has mate in one as white
game = ChessGame(player3, player2)
game.board.clear_board()
game.board.set_piece_at(0, chess.Piece(6, False))
game.board.set_piece_at(17, chess.Piece(6, True))
game.board.set_piece_at(15, chess.Piece(5, True))

while not game.is_game_over():
    print(game)
    game.make_move()

# Example 3, AlphaBetaAI stops mate even though black queen piece is not protected
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

# Example 4, MinimaxAI stops mate even though black queen piece is not protected
game = ChessGame(player3, player2)
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
