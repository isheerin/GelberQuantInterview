# brew install pyqt
import random
import sys

import chess
import chess.svg
from PyQt5 import QtSvg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication

from ChessGame import ChessGame
from HumanPlayer import HumanPlayer
from RandomAI import RandomAI


class ChessGui:
    def __init__(self, aPlayer1, aPlayer2):
        self.player1 = aPlayer1
        self.player2 = aPlayer2
        self.game = ChessGame(aPlayer1, aPlayer2)
        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()

    def start(self):
        myTimer = QTimer()
        myTimer.timeout.connect(self.make_move)
        myTimer.start(10)
        self.display_board()

    def display_board(self):
        mySvgBoard = chess.svg.board(self.game.board)
        mySvgBytes = QByteArray()
        mySvgBytes.append(mySvgBoard)
        self.svgWidget.load(mySvgBytes)

    def make_move(self):
        print("making move, white turn " + str(self.game.board.turn))
        self.game.make_move()
        self.display_board()


if __name__ == "__main__":
    random.seed(1)
    # to do: gui does not work well with HumanPlayer, due to input() use on stdin conflict with event loop.
    player1 = HumanPlayer()
    player2 = RandomAI()

    game = ChessGame(player1, player2)
    gui = ChessGui(player1, player2)
    gui.start()
    sys.exit(gui.app.exec_())
