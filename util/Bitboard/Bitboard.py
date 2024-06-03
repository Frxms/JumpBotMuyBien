import numpy as np

from util.Bitboard.constants import Color, Piece, Rank, File


class GameBoard:
    def __init__(self):
        self.pieces = np.zeros((2, 3), dtype=np.uint64)
        # 2 sides with 2 different types of pieces stored as unique 64 integers
        self.eachSide = np.zeros(2, dtype=np.uint64)
        self.board = np.zeros(0)

    def __str__(self):
        board =[]
        for r in reversed(Rank):
            for f in File:
                field = self.field_position(r, f)
                red_piece = self.piece_check(field, Color.Red)
                blue_piece = self.piece:check(field, Color.BLUE)


    # 0b0000000000000000000000000000000000000000000000001111111101111110
    def gameStart(self):
        self.pieces[Color.BLUE][Piece.PAWN] = np.uint64(0x000000000000FF7E)
        self.pieces[Color.BLUE][Piece.TOWER] = np.uint64(0b0000000000000000)    # "bb" Tower
        self.pieces[Color.BLUE][Piece.TWOCOLTOWER] = np.uint64(0b0000000000000000)  # "rb" Tower

        self.pieces[Color.BLUE][Piece.PAWN] = np.uint64(0xFF7E000000000000)
        self.pieces[Color.BLUE][Piece.TOWER] = np.uint64(0x0000000000000000)    # "rr" Tower
        self.pieces[Color.BLUE][Piece.TWOCOLTOWER] = np.uint64(0x0000000000000000)  # "br" Tower

    def piece_check(self, field, color=None):


    def field_position(self ,r, f):
        return ((r.value << np.uint8(3)) | f.value)

#[[0 0]
# [0 0]
# [0 0]]