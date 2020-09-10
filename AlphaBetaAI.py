# Iain Sheerin
# 1/21/19
# CS76 HW3
from math import inf
from TranspositionTable import Wrapper


class AlphaBetaAI:

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

    # function to choose move
    def chooseMove(self, aBoard):

        # initializations
        myReorderedMoves = self.reorder_moves(aBoard)
        mySelectedMove = None

        # keep track of total calls and max depth in lists so other functions can edit
        myMinimaxCalls = [0]
        myMinimaxDepth = [0]

        # initializing alpha and beta
        myAlpha = -inf
        myBeta = inf

        # iterative deepening search, at each level
        for myDepthLimit in range(1, self.depth_limit+1):
            mySelectedMoveScore = -inf    # reset valuation

            myTranspositionTable = Wrapper()  # initialize wrapper for transposition table

            # for every legal move
            for myMove in myReorderedMoves:

                # get score of move
                aBoard.push(myMove)
                myTempMoveScore = self.min_fn(aBoard, 1, myDepthLimit, myAlpha, myBeta, myMinimaxCalls, myMinimaxDepth, myTranspositionTable)
                myTranspositionTable.add_board(aBoard, myTempMoveScore, 0)    # add position/score to table
                aBoard.pop()

                # if score is better than that already selected, pick better move
                if myTempMoveScore > mySelectedMoveScore:
                    mySelectedMoveScore = myTempMoveScore
                    mySelectedMove = myMove
                    self.best_move_score = mySelectedMoveScore

            # if print best move is set to true, print the best move at each level with its score
            self.best_move = mySelectedMove
            if self.print_best_move:
                print("Best move at depth_limit " + str(myDepthLimit) + " is: " + str(self.best_move) + " with score: " + str(self.best_move_score))

        # print recommendation, the number of function calls and max depth reached
        print("AlphaBeta recommending move " + str(mySelectedMove))
        print("AlphaBeta calls: " + str(myMinimaxCalls[0]))
        print("AlphaBeta max depth: " + str(myMinimaxDepth[0]))
        return mySelectedMove

    # max function
    def max_fn(self, aBoard, aDepth, aDepthLimit, aAlpha, aBeta, aCalls, aMaxDepth, aTable):

        # increase number of calls and check for max depth reached
        aCalls[0] += 1
        if aDepth > aMaxDepth[0]:
            aMaxDepth[0] = aDepth

        # check if game is over
        if aBoard.is_game_over():

            # check if checkmate
            if aBoard.is_checkmate():
                return -10000

            # check if tie
            elif aBoard.is_stalemate() or aBoard.is_insufficient_material() or aBoard.is_seventyfive_moves() or aBoard.is_fivefold_repetition():
                return 0

        # if depth limit reached, return estimate of score
        elif aDepth >= aDepthLimit:
            return self.evaluation_fn(aBoard)

        myScore = -inf    # score initialization

        myReorderedMoves = self.reorder_moves(aBoard)   # reorder moves to look at captures first

        # loop through all legal moves
        for move in myReorderedMoves:

            # get score from min function
            aBoard.push(move)

            # if board/depth already explored, get score from transposition table
            if aTable.zobrist_hash(aBoard, aDepth) in aTable.table:
                score = aTable.get_score(aBoard, aDepth)
                aBoard.pop()
                return score

            myScore = max(myScore, self.min_fn(aBoard, aDepth + 1, aDepthLimit, aAlpha, aBeta, aCalls, aMaxDepth, aTable))  # get score
            aTable.add_board(aBoard, myScore, aDepth)    # add position/score to table
            aBoard.pop()

            # if score is greater than beta, no need to check, just return score
            if myScore >= aBeta:
                return myScore - 0.01

            aAlpha = max(aAlpha, myScore)   # change value for alpha if higher score

        return myScore - 0.01

    # min function
    def min_fn(self, aBoard, aDepth, aDepthLimit, aAlpha, aBeta, aCalls, aMaxDepth, aTable):

        # increase number of calls and check for max depth reached
        aCalls[0] += 1
        if aDepth > aMaxDepth[0]:
            aMaxDepth[0] = aDepth

        # check if game is over
        if aBoard.is_game_over():

            # check if checkmate
            if aBoard.is_checkmate():
                return 10000

            # check if tie
            elif aBoard.is_stalemate() or aBoard.is_insufficient_material() or aBoard.is_seventyfive_moves() or aBoard.is_fivefold_repetition():
                return 0

        # if depth limit reached, return estimate of score
        elif aDepth >= aDepthLimit:
            return self.evaluation_fn(aBoard)

        # score initialization
        myScore = inf

        # move reordering to look at captures first
        myReorderedMoves = self.reorder_moves(aBoard)

        # loop over all legal moves
        for myMove in myReorderedMoves:

            # get minimum of score and score from evaluation function
            aBoard.push(myMove)

            # if board/depth already explored, get score from transposition table
            if aTable.zobrist_hash(aBoard, aDepth) in aTable.table:
                myScore = aTable.get_score(aBoard, aDepth)
                aBoard.pop()
                return myScore

            # get score and add position/score to table
            myScore = min(myScore, self.max_fn(aBoard, aDepth+1, aDepthLimit, aAlpha, aBeta, aCalls, aMaxDepth, aTable))
            aTable.add_board(aBoard, myScore, aDepth)
            aBoard.pop()

            # if score less than alpha, return score
            if myScore <= aAlpha:
                return myScore - 0.01

            aBeta = min(myScore, aBeta)  # change beta if score is less than beta

        return myScore - 0.01

    # evaluation function
    def evaluation_fn(self, aBoard):
        myScore = 0  # initial score

        # pieces score dictionary
        myScoreDictionary = {'r': -5, 'n': -3, 'b': -3, 'p': -1, "q": -9, "k": -100, "P": 1, "R": 5, "B": 3, "N": 3, "Q": 9, "K": 100}
        myPieceMap = aBoard.piece_map()

        # look at each piece and add to score based on values in dictionary
        for mySquare in myPieceMap:
            myScore += self.multiplier * myScoreDictionary[str(myPieceMap[mySquare])]

        return myScore

    # function to reorder all legal moves, pushing moves with captures to the front of the list
    @staticmethod
    def reorder_moves(aBoard):
        myCaptures = []
        myNonCaptures = []

        # look through all moves
        for myMove in list(aBoard.legal_moves):

            # if capture add to list
            if aBoard.is_capture(myMove):
                myCaptures.append(myMove)

            # add non captures to other list
            else:
                myNonCaptures.append(myMove)

        # reorder lists and return combined lists
        myReorderedMoves = myCaptures + myNonCaptures
        return myReorderedMoves
