# pip3 install python-chess
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


import sys


player1 = HumanPlayer()
# player2 = RandomAI()
player2 = AlphaBetaAIQSearch(5, False, True)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()


# print(hash(str(game.board)))
