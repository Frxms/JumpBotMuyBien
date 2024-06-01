import numpy as np

from util.Bitboard.constants import Color, Piece


class GameBoard:
    def __init__(self):
        self.pieces = np.zeros((2, 2), dtype=np.uint64)
        # 2 sides with 2 different types of pieces stored as unique 64 integers
        self.eachSide = np.zeros(2, dtype=np.uint64)
        self.board = np.zeros(0)

    def __str__(self):


    # 0b0000000000000000000000000000000000000000000000001111111101111110
    def gameStart(self):
        self.pieces[Color.BLUE][Color.BLUE.PAWN] = np.uint64(0x000000000000FF7E)
        self.pieces[Color.BLUE][Piece.TOWER] = np.uint64(0b0000000000000000)
        self.pieces[Color.BLUE][Piece.TWOCOLTOWER] = np.uint64(0b0000000000000000)

        self.pieces[Color.BLUE][Piece.PAWN] = np.uint64(0xFF7E000000000000)
        self.pieces[Color.BLUE][Piece.TOWER] = np.uint64(0x0000000000000000)
        self.pieces[Color.BLUE][Piece.TWOCOLTOWER] = np.uint64(0x0000000000000000)

    def