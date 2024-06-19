import numpy as np
import re

from util.Bitboard.bbHelperFunc import corner_check, to_bitboard, is_set
from util.Bitboard.constants import Color, Row, Column, Piece


class GameBoard:
    def __init__(self, fen="b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"):
        self.pieces = np.zeros((2, 3), dtype=np.uint64)
        # 2 sides with 2 different types of pieces stored as unique 64 integers
        self.eachSide = np.zeros(2, dtype=np.uint64)
        self.board = np.uint64(0)
        split_fen = fen.split(" ")
        self.color = self.set_col(split_fen[1])
        self.current_game_board(split_fen[0])

    def __str__(self):
        board =[]
        for r in reversed(Row):
            for c in Column:
                field = self.field_index(r, c)
                red_piece = self.piece_check(field, Color.RED)
                blue_piece = self.piece_check(field, Color.BLUE)
                corner = corner_check(field)
                if red_piece is not None:
                    board.append(self.piece_str(Color.RED, red_piece))
                elif blue_piece is not None:
                    board.append(self.piece_str(Color.BLUE, blue_piece))
                elif corner is not None:
                    board.append("X")
                else:
                    board.append(".")
            board.append("\n")
        board = ''.join(board)
        print(board)

    def current_game_board(self, fen: str): # hier mit field_index in die richtige Position einfügen
        # gleichzeitig in mehrere Bitboards eintragen (All, Farbe, Piece/Tower/TwoColTower)
        piece_mapping = {
            "r0": (Color.RED, Piece.PAWN),
            "rr": (Color.RED, Piece.TOWER),
            "br": (Color.RED, Piece.TWOCOLTOWER),
            "b0": (Color.BLUE, Piece.PAWN),
            "bb": (Color.BLUE, Piece.TOWER),
            "rb": (Color.BLUE, Piece.TWOCOLTOWER)
        }
        lines = fen.split("/")
        for i1, row in enumerate(lines):
            line = re.split(r'(r0|b0|rr|bb|rb|br)', row)
            counter = 0
            for i2, field in enumerate(line):
                index = self.field_index_int(i1, counter)
                bb = to_bitboard(index)
                if bb & np.uint64(0x8100000000000081) != np.uint64(0):
                    counter += 1
                if field.isdigit():
                    counter += int(field)
                elif field in piece_mapping:
                    counter += 1
                    color, piece_type = piece_mapping[field]
                    self.board |= bb
                    self.eachSide[color] |= bb
                    self.pieces[color][piece_type] |= bb


    def set_col(self, color):
        if color == "r":
            return Color.RED
        else:
            return Color.BLUE

    # 0b0000000000000000000000000000000000000000000000000111111001111110
    # msb is h8, lsb is a1, bit at msb - 7 is h7
    def gameStart(self):
        self.eachSide[Color.RED] = np.uint64(0x7E7E000000000000)
        self.pieces[Color.RED][Piece.PAWN] = np.uint64(0x7E7E000000000000)
        self.pieces[Color.RED][Piece.TOWER] = np.uint64(0x0000000000000000)  # "rr" Tower
        self.pieces[Color.RED][Piece.TWOCOLTOWER] = np.uint64(0x0000000000000000)  # "br" Tower

        self.eachSide[Color.BLUE] = np.uint64(0x0000000000007E7E)
        self.pieces[Color.BLUE][Piece.PAWN] = np.uint64(0x0000000000007E7E)
        self.pieces[Color.BLUE][Piece.TOWER] = np.uint64(0b0000000000000000)    # "bb" Tower
        self.pieces[Color.BLUE][Piece.TWOCOLTOWER] = np.uint64(0b0000000000000000)  # "rb" Tower

    def get_pieceboard(self, piece, color=None):
        if color is None:
            color = self.color
        return self.pieces[color][piece]

    def piece_check(self, field, color=None):   # searches for the right piece bb
        if color is None:
            color = self.color
        return next(
            (p for p in Piece if
                is_set(self.get_pieceboard(p, color), field)), None
        )

    def field_index(self, r, f):     # returns the correct position as a number (2^3 = 8)
        return ((r.value << np.uint8(3)) | f.value)

    def field_index_int(self, r, f):
        return ((np.uint8(r) << np.uint8(3)) | np.uint8(f))

    def piece_str(self, color, piece):
        if color == Color.BLUE:
            if piece == Piece.PAWN:
                return "b"
            elif piece == Piece.TOWER:
                return "bb"
            elif piece == Piece.TWOCOLTOWER:
                return "rb"
        elif color == Color.RED:
            if piece == Piece.PAWN:
                return "r"
            elif piece == Piece.TOWER:
                return "rr"
            elif piece == Piece.TWOCOLTOWER:
                return "br"