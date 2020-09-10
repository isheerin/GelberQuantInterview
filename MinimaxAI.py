# Iain Sheerin
# 1/21/19
# CS76 HW3

from math import inf
from TranspositionTable import Wrapper


class MinimaxAI:

    # initialization
    def __init__(self, aDepthLimit, aColor, aPrintBestMove=False):  # depth starts at 1
        self.depth_limit = aDepthLimit
        self.color = aColor

        # correct multiplier based on color
        self.multiplier = 1
        if not aColor:
            self.multiplier = -1

        self.best_move = None
        self.best_move_score = None
        self.print_best_move = aPrintBestMove

    # choosing best move
    def chooseMove(self, aBoard):
        myMoves = list(aBoard.legal_moves)     # all possible moves
        mySelectedMove = myMoves[0]    # initializing

        # tracking calls and depth, in list form so other functions can be pointed to it
        myMinimaxCalls = [0]
        myMinimaxDepth = [0]

        # iterative deepening search, going to each depth limit
        for myDepthLimit in range(1, self.depth_limit+1):
            mySelectedMoveScore = -inf    # reset valuation
            myTranspositionTable = Wrapper()     # initialize transposition table wrapper

            # look through all legal moves
            for myMove in myMoves:
                aBoard.push(myMove)    # check move
                myTempMoveScore = self.min_fn(aBoard, 1, myDepthLimit, myMinimaxCalls, myMinimaxDepth, myTranspositionTable)  # get score
                myTranspositionTable.add_board(aBoard, myTempMoveScore, 0)    # add to transposition table
                aBoard.pop()

                # if score is better than current score, change score and selected move
                if myTempMoveScore > mySelectedMoveScore:
                    mySelectedMoveScore = myTempMoveScore
                    mySelectedMove = myMove
                    self.best_move_score = mySelectedMoveScore

            # best move at depth
            self.best_move = mySelectedMove

            # if want to print move at each depth limit, print move with score
            if self.print_best_move:
                print("Best move at depth_limit " + str(myDepthLimit) + " is: " + str(self.best_move) + " with score: " + str(self.best_move_score))

        # print selected move, number of calls and depth reached
        print("Minimax recommending move " + str(mySelectedMove))
        print("Minimax calls: " + str(myMinimaxCalls[0]))
        print("Minimax max depth: " + str(myMinimaxDepth[0]))
        return mySelectedMove

    # max function
    def max_fn(self, aBoard, aDepth, aDepthLimit, aCalls, aMaxdepth, aTable):
        aCalls[0] += 1  # add one to calls

        # if depth is furthest explored, add to max depth
        if aDepth > aMaxdepth[0]:
            aMaxdepth[0] = aDepth

        # check if game is over
        if aBoard.is_game_over():

            # min score if checkmate
            if aBoard.is_checkmate():
                return -10000

            # zero if tie
            elif aBoard.is_stalemate() or aBoard.is_insufficient_material() or aBoard.is_seventyfive_moves() or aBoard.is_fivefold_repetition():
                return 0

        # if depth limit reached, return estimate from evaluation function
        elif aDepth >= aDepth:
            return self.evaluation_fn(aBoard)

        # initial score
        myScore = -inf
        # loop through moves of legal list
        for aMove in list(aBoard.legal_moves):

            # get max of score and what min function returns
            aBoard.push(aMove)

            # if board/depth already explored, get score from transposition table
            if aTable.zobrist_hash(aBoard, aDepth) in aTable.table:
                myScore = aTable.get_score(aBoard, aDepth)
                aBoard.pop()
                return myScore

            myScore = max(myScore, self.min_fn(aBoard, aDepth+1, aDepthLimit, aCalls, aMaxdepth, aTable))    # get score
            aTable.add_board(aBoard, myScore, aDepthLimit)    # add position/score to table
            aBoard.pop()

        # return function with time penalty
        return myScore - 0.01

    # minimum function
    def min_fn(self, aBoard, aDepth, aDepthLimit, aCalls, aMaxdepth, aTable):
        aCalls[0] += 1   # add one to calls

        # if depth is furthest explored, add to max depth
        if aDepth > aMaxdepth[0]:
            aMaxdepth[0] = aDepth

        # check if game is over
        if aBoard.is_game_over():

            # max score if checkmate
            if aBoard.is_checkmate():
                return 10000

            # zero if tie
            elif aBoard.is_stalemate() or aBoard.is_insufficient_material() or aBoard.is_seventyfive_moves() or aBoard.is_fivefold_repetition():
                return 0

        # if limit is reached, return estimate from evaluation function
        elif aDepth >= aDepthLimit:
            return self.evaluation_fn(aBoard)

        # inital score
        myScore = inf

        # loop through all legal moves
        for myMove in list(aBoard.legal_moves):

            # get minimum score of score and what max function returns
            aBoard.push(myMove)

            # if board/depth already explored, get score from transposition table
            if aTable.zobrist_hash(aBoard, aDepth) in aTable.table:
                myScore = aTable.get_score(aBoard, aDepth)
                aBoard.pop()
                return myScore

            myScore = min(myScore, self.max_fn(aBoard, aDepth+1, aDepthLimit, aCalls, aMaxdepth, aTable))    # get score
            aTable.add_board(aBoard, myScore, aDepth)    # add position/score to table
            aBoard.pop()

        # return score with time penalty
        return myScore - 0.01

    # evaluation function
    def evaluation_fn(self, aBoard):
        myScore = 0  # initial score

        # pieces score dictionary
        myScoreDictionary = {'r': -5, 'n': -3, 'b': -3, 'p': -1, "q": -9, "k": -100, "P": 1, "R": 5, "B": 3, "N": 3, "Q": 9, "K": 100}
        # map of pieces on board
        myPieceMap = aBoard.piece_map()

        # look at each piece and add to score based on values in dictionary
        for mySquare in myPieceMap:
            myScore += self.multiplier * myScoreDictionary[str(myPieceMap[mySquare])]

        return myScore
