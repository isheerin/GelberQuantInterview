# Iain Sheerin
# 1/21/19
# CS76 HW3
import random


# class used to implement transposition table
class Wrapper:

    def __init__(self):
        self.table = {}
        self.hash_dict = {'r': '01', 'n': '02', 'b': '03', 'p': '04', "q": '05', "k": '06', "P": '07', "R": '08', "B": '09', "N": '10', "Q": '11', "K": '00', '.': '13', ' ': "14", '\n': "15"} # corresponding indices for characters

        # creating table for zobrist hashing
        self.ztable = []

        # go through all squares and add list
        for mySquare in range(64):
            self.ztable.append([])

            # in each square add list of each possible piece and add random 64 bit string
            for myPiece in range(12):
                self.ztable[mySquare].append([])
                self.ztable[mySquare][myPiece] = random.getrandbits(64)

    # add board/score/depth with zobrist hashing
    def add_board(self, aBoard, aScore, aDepth):
        self.table[self.zobrist_hash(aBoard, aDepth)] = aScore

    # get score from zobrist table
    def get_score(self, aBoard, aDepth):
        return self.table[self.zobrist_hash(aBoard, aDepth)]

    # hashing not using zobrist hashing
    def get_hash(self, aBoard, aDepth):
        # hash is tring
        myHash = ""

        # iterate through board and add character index plus depth
        for myCharacter in str(aBoard):
            myHash += self.hash_dict[myCharacter]
        myHash += str(aDepth)
        return myHash

    # clear table
    def reset_table(self):
        self.table = {}

    # zobrist hashing function
    def zobrist_hash(self, aBoard, aDepth):
        myHash = 0
        myPieceMap = aBoard.piece_map()    # map of pieces

        # iterate pieces
        for mySquare in myPieceMap:
            myBitString = int(self.hash_dict[str(myPieceMap[mySquare])])   # get bit string
            myHash ^= self.ztable[mySquare][myBitString]                  # XOR string

        return myHash + aDepth    # return hash value altered with depth

    # stores board/depth/score for non zobrist hashing
    def store_ids_score(self, aBoard, aDepth, aScore):
        self.table[self.get_hash(aBoard, aDepth)] = aScore

    # get score from non zobrist hashing
    def get_ids_score(self, aBoard, aDepth):
        return self.table[self.get_hash(aBoard, aDepth)]
