# Iain Sheerin
# 1/21/19
# CS76 HW3
import chess


class ChessGame:
    def __init__(self, aPlayer1, aPlayer2):
        self.board = chess.Board()
        self.players = [aPlayer1, aPlayer2]

    def make_move(self):
        myPlayer = self.players[1 - int(self.board.turn)]
        myMove = myPlayer.chooseMove(self.board)
        self.board.push(myMove)  # Make the move

    def is_game_over(self):
        return self.board.is_game_over()

    def __str__(self):
        myColumnLabels = "\n----------------\na b c d e f g h\n"
        myBoardString = str(self.board) + myColumnLabels
        myMoveString = "White to move" if self.board.turn else "Black to move"
        return myBoardString + "\n" + myMoveString + "\n"
