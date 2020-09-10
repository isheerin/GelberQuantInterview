# Iain Sheerin
# 1/21/19
# CS76 HW3
import chess


class HumanPlayer:
    def __init__(self):
        print("Moves can be entered using four characters. For example, d2d4 moves the piece "
              "at d2 to d4.")
        pass

    @staticmethod
    def chooseMove(board):
        myMoves = list(board.legal_moves)
        myUciMove = None

        while myUciMove not in myMoves:
            print("Please enter your move: ")
            myHumanMove = input()

            try:
                myUciMove = chess.Move.from_uci(myHumanMove)
            except ValueError:
                # illegal move format
                myUciMove = None

            if myUciMove not in myMoves:
                print("  That is not a legal move!")

        print(myUciMove in myMoves)
        return myUciMove
