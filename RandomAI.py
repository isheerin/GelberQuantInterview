# Iain Sheerin
# 1/21/19
# CS76 HW3

import random
from time import sleep


class RandomAI:
    def __init__(self):
        pass

    # choose random move
    @staticmethod
    def chooseMove(aBoard):
        myMoves = list(aBoard.legal_moves)
        myMove = random.choice(myMoves)
        sleep(1)
        print(aBoard.piece_map())
        print("Random AI recommending move " + str(myMove))
        return myMove
