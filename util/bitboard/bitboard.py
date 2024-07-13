import copy

import numpy as np
import re

from util.bitboard.bb_helper import corner_check, to_bitboard, is_set, EMPTY_BB
from util.bitboard.constants import Color, Row, Column, Piece
from util.bitboard.moves import gen_moves


class GameBoard:
    def __init__(self, fen="b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"):
        self.pieces = np.zeros((2, 4), dtype=np.uint64)
        # 2 sides with 2 different types of pieces stored as unique 64 integers
        self.each_side = np.zeros(2, dtype=np.uint64)
        self.board = np.uint64(0)
        split_fen = fen.split(" ")
        self.color = self.set_col(split_fen[1])
        self.current_game_board(split_fen[0])
        self.opp_color = Color.RED if self.color == Color.BLUE else Color.BLUE

    def __str__(self):
        board = []
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
        return board

    def current_game_board(self, fen: str):  # hier mit field_index in die richtige Position einfügen
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
                    self.each_side[color] |= bb
                    self.pieces[color][piece_type] |= bb
                    if piece_type in {Piece.TOWER, Piece.TWOCOLTOWER}:
                        self.pieces[color][Piece.ALLTOWERS] |= bb

    def set_col(self, color):
        if color == "r":
            return Color.RED
        else:
            return Color.BLUE

    def change_col(self):
        if self.color == Color.RED:
            self.color = Color.BLUE
        else:
            self.color = Color.RED

    def alpha_beta_bool(self):
        if self.color == Color.BLUE:
            return False
        else:
            return True

    # 0b0000000000000000000000000000000000000000000000000111111001111110
    # msb is h8, lsb is a1, bit at msb - 7 is h7
    def gameStart(self):
        self.each_side[Color.RED] = np.uint64(0x7E7E000000000000)
        self.pieces[Color.RED][Piece.PAWN] = np.uint64(0x7E7E000000000000)
        self.pieces[Color.RED][Piece.TOWER] = np.uint64(0x0000000000000000)  # "rr" Tower
        self.pieces[Color.RED][Piece.TWOCOLTOWER] = np.uint64(0x0000000000000000)  # "br" Tower
        self.pieces[Color.RED][Piece.ALLTOWERS] = np.uint64(0x0000000000000000)

        self.each_side[Color.BLUE] = np.uint64(0x0000000000007E7E)
        self.pieces[Color.BLUE][Piece.PAWN] = np.uint64(0x0000000000007E7E)
        self.pieces[Color.BLUE][Piece.TOWER] = np.uint64(0b0000000000000000)  # "bb" Tower
        self.pieces[Color.BLUE][Piece.TWOCOLTOWER] = np.uint64(0b0000000000000000)  # "rb" Tower
        self.pieces[Color.BLUE][Piece.ALLTOWERS] = np.uint64(0x0000000000000000)

    def get_pieceboard(self, piece, color=None):
        if color is None:
            color = self.color
        return self.pieces[color][piece]

    def piece_check(self, field, color=None):  # searches for the right piece bb
        if color is None:
            color = self.color
        return next(
            (p for p in Piece if
             is_set(self.get_pieceboard(p, color), field)), None
        )

    def field_index(self, r, f):  # returns the correct position as a number (2^3 = 8)
        return ((r.value << np.uint8(3)) | f.value)

    def field_index_int(self, r, f):
        return ((np.uint8(r) << np.uint8(3)) | np.uint8(f))

    def piece_str(self, color, piece):
        if color == Color.BLUE:
            if piece == Piece.PAWN:
                return "B"
            elif piece == Piece.TOWER:
                return "bb"
            elif piece == Piece.TWOCOLTOWER:
                return "rb"
        elif color == Color.RED:
            if piece == Piece.PAWN:
                return "R"
            elif piece == Piece.TOWER:
                return "rr"
            elif piece == Piece.TWOCOLTOWER:
                return "br"

    def is_endgame(self):
        bottom_row = np.uint64(0xFF)
        top_row = np.uint64(0xFF00000000000000)
        if (((self.each_side[Color.RED] & bottom_row) != EMPTY_BB
             or (self.each_side[Color.BLUE] & top_row) != EMPTY_BB)
                or self.each_side[Color.RED] == 0 or self.each_side[Color.BLUE] == 0):
            return True
        return False

    def use_move(self, moveset):
        # moveset[0] is the piece, moveset[1] the starting point, moveset[2] the target field
        if moveset[0] == Piece.PAWN:
            return self.move_start(Piece.PAWN, moveset[1], moveset[2])
        else:
            if moveset[1] & self.pieces[self.color][Piece.TOWER] != EMPTY_BB:
                return self.move_start(Piece.TOWER, moveset[1], moveset[2])
            else:
                return self.move_start(Piece.TWOCOLTOWER, moveset[1], moveset[2])

    # handles the necessary functions for the starting field
    def move_start(self, piece: Piece, start: np.uint64, goal: np.uint64):
        if piece == Piece.PAWN:
            self.pieces[self.color][piece] ^= start
            self.each_side[self.color] ^= start
            self.board ^= start
            return piece, self.move_to_target(goal), start, goal
        elif piece == Piece.TOWER:
            self.pieces[self.color][piece] ^= start
            self.pieces[self.color][Piece.ALLTOWERS] ^= start
            self.pieces[self.color][Piece.PAWN] |= start
            return piece, self.move_to_target(goal), start, goal
        elif piece == Piece.TWOCOLTOWER:
            self.pieces[self.color][piece] ^= start
            self.pieces[self.color][Piece.ALLTOWERS] ^= start
            self.each_side[self.color] ^= start
            self.pieces[self.opp_color][Piece.PAWN] |= start
            self.each_side[self.opp_color] |= start
            return piece, self.move_to_target(goal), start, goal

    # piece represents the piece in start field
    def move_to_target(self, goal: np.uint64):
        # no own piece in goal field
        if goal & self.each_side[self.color] == EMPTY_BB:
            # an opposition piece in goal field
            if goal & self.each_side[self.opp_color] != EMPTY_BB:
                # a pawn in goal field
                if goal & self.pieces[self.opp_color][Piece.PAWN] != EMPTY_BB:
                    self.pieces[self.opp_color][Piece.PAWN] ^= goal
                    self.each_side[self.opp_color] ^= goal
                    self.pieces[self.color][Piece.PAWN] |= goal
                    self.each_side[self.color] |= goal
                    return Piece.PAWN
                # a tower in goal field
                elif goal & self.pieces[self.opp_color][Piece.TOWER] != EMPTY_BB:
                    self.pieces[self.opp_color][Piece.TOWER] ^= goal
                    self.pieces[self.opp_color][Piece.ALLTOWERS] ^= goal
                    self.each_side[self.opp_color] ^= goal
                    self.pieces[self.color][Piece.TWOCOLTOWER] |= goal
                    self.pieces[self.color][Piece.ALLTOWERS] |= goal
                    self.each_side[self.color] |= goal
                    return Piece.TOWER
                # a twocol tower in goal field
                else:
                    self.pieces[self.opp_color][Piece.TWOCOLTOWER] ^= goal
                    self.pieces[self.opp_color][Piece.ALLTOWERS] ^= goal
                    self.each_side[self.opp_color] ^= goal
                    self.pieces[self.color][Piece.TOWER] |= goal
                    self.pieces[self.color][Piece.ALLTOWERS] |= goal
                    self.each_side[self.color] |= goal
                    return Piece.TWOCOLTOWER
            # no piece in goal field
            else:
                self.pieces[self.color][Piece.PAWN] |= goal
                self.each_side[self.color] |= goal
                self.board |= goal
                return None
        # there is an own piece in the goal field
        elif goal & self.each_side[self.color] != EMPTY_BB:
            self.pieces[self.color][Piece.PAWN] ^= goal
            self.pieces[self.color][Piece.TOWER] |= goal
            self.pieces[self.color][Piece.ALLTOWERS] |= goal
            return None

# piece is the piece that was moved, goal_piece is the piece that was changed
    def unmove(self, reverse_set):
        # start_piece: Piece, goal_piece: Piece, start: np.uint64, goal: np.uint64
        # a pawn in goal field means, current color also has a pawn in this field
        if reverse_set[1] == Piece.PAWN:
            self.pieces[self.color][Piece.PAWN] ^= reverse_set[3]
            self.each_side[self.color] ^= reverse_set[3]
            self.pieces[self.opp_color][Piece.PAWN] |= reverse_set[3]
            self.each_side[self.opp_color] |= reverse_set[3]
            return self.unmove_start(reverse_set[0], reverse_set[2])
        # a tower in goal field means, current color has a twocol tower in this field
        elif reverse_set[1] == Piece.TOWER:
            self.pieces[self.color][Piece.TWOCOLTOWER] ^= reverse_set[3]
            self.pieces[self.color][Piece.ALLTOWERS] ^= reverse_set[3]
            self.each_side[self.color] ^= reverse_set[3]
            self.pieces[self.opp_color][Piece.TOWER] |= reverse_set[3]
            self.pieces[self.opp_color][Piece.ALLTOWERS] |= reverse_set[3]
            self.each_side[self.color] |= reverse_set[3]
            return self.unmove_start(reverse_set[0], reverse_set[2])
        # a twocol tower in goal field means, current color has a tower in this field
        elif reverse_set[1] == Piece.TWOCOLTOWER:
            self.pieces[self.color][Piece.TOWER] ^= reverse_set[3]
            self.pieces[self.color][Piece.ALLTOWERS] ^= reverse_set[3]
            self.each_side[self.color] ^= reverse_set[3]
            self.pieces[self.opp_color][Piece.TWOCOLTOWER] |= reverse_set[3]
            self.pieces[self.opp_color][Piece.ALLTOWERS] |= reverse_set[3]
            self.each_side[self.color] |= reverse_set[3]
            return self.unmove_start(reverse_set[0], reverse_set[2])
        # if goal matches with one tower, there had to be a pawn of the same color here before
        if reverse_set[3] & self.pieces[self.color][Piece.TOWER] != EMPTY_BB:
            self.pieces[self.color][Piece.TOWER] ^= reverse_set[3]
            self.pieces[self.color][Piece.ALLTOWERS] ^= reverse_set[3]
            self.pieces[self.color][Piece.PAWN] |= reverse_set[3]
            return self.unmove_start(reverse_set[0], reverse_set[2])
        else:
            self.pieces[self.color][Piece.PAWN] ^= reverse_set[3]
            self.each_side[self.color] ^= reverse_set[3]
            self.board ^= reverse_set[3]
            return self.unmove_start(reverse_set[0], reverse_set[2])
            # todo diesen Aufruf nach ganz vorne

    def unmove_start(self, start_piece: Piece, start: np.uint64):
            if start_piece == Piece.PAWN:
                self.pieces[self.color][start_piece] |= start
                self.each_side[self.color] |= start
                self.board |= start
                return True
            elif start_piece == Piece.TOWER:
                self.pieces[self.color][Piece.PAWN] ^= start
                self.pieces[self.color][start_piece] |= start
                self.pieces[self.color][Piece.ALLTOWERS] |= start
                return True
            elif start_piece == Piece.TWOCOLTOWER:
                self.pieces[self.opp_color][Piece.PAWN] ^= start
                self.each_side[self.opp_color] ^= start
                self.pieces[self.color][start_piece] |= start
                self.pieces[self.color][Piece.ALLTOWERS] |= start
                self.each_side[self.color] |= start
                return True

    def is_terminal(self):
        return self.is_endgame()

    def get_legal_moves(self):
        return gen_moves(self, True)

    def make_move(self, move):
        new_board = copy.deepcopy(self)
        new_board.use_move(move)
        new_board.change_col()
        return new_board

    def pieces_in_end_zone(self, color):
        end_zone = 0xFF if color == Color.RED else 0xFF00000000000000
        return bin(self.each_side[color] & end_zone).count('1')

    def distance_to_end_zone(self, color):
        pieces = self.each_side[color]
        if color == Color.RED:
            return min(7 - (i // 8) for i in range(64) if (pieces & (1 << i)))
        else:
            return min(i // 8 for i in range(64) if (pieces & (1 << i)))

    def get_result(self, player):
        if self.is_endgame():
            if self.pieces_in_end_zone(player) > 0:
                return 1  # Win for the current player
            elif self.pieces_in_end_zone(Color.RED if player == Color.BLUE else Color.BLUE) > 0:
                return 0  # Loss for the current player
        return 0.5  # Game not ended or draw

    def clone(self):
        return copy.deepcopy(self)



