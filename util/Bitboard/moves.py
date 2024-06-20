import numpy as np

from util.Bitboard import Bitboard
from util.Bitboard.constants import Color, Piece, Row, Column
from util.Bitboard.bbHelperFunc import to_bitboard

debruijn = np.uint64(0x03f79d71b4cb0a89)
index64 = np.array([
    0, 1, 2, 53, 3, 7, 54, 27,
    4, 38, 41, 8, 34, 55, 48, 28,
    62, 5, 39, 46, 44, 42, 22, 9,
    24, 35, 59, 56, 49, 18, 29, 11,
    63, 52, 6, 26, 37, 40, 33, 47,
    61, 45, 43, 21, 23, 58, 17, 10,
    51, 25, 36, 32, 60, 20, 57, 16,
    50, 31, 19, 15, 30, 14, 13, 12
], dtype=np.uint8)
empty_board = np.uint64(0)
a_column = np.uint64(0x8101010101010181)
ab_column = np.uint64(0x8303030303030383)
h_column = np.uint64(0x8180808080808081)
gh_column = np.uint64(0xC1C0C0C0C0C0C0C1)
corner = np.uint64(0x8100000000000081)


def get_bits(bb: np.uint64):    # returns every piece as its own bb
    results = []
    while bb != empty_board:
        lsb = bb & -bb
        results.append(lsb)
        bb ^= lsb
    return results


#field class that splits into rows and columns by /8 and get index after - mod
#returns bitboard for that
#compare current board with field board to get position and surroundings of current bit
#bit shift so see options

#
def gen_moves(board: Bitboard):
    # piece: Piece, index: np.uint64
    piece = []
    legal_moves = []
    for p in Piece:
        piece = get_bits(board[board.color][p])
        for piece_bb in piece:
            legal_moves.append((piece_bb, p, piece_moves(board, piece_bb, p)))
    return legal_moves


def piece_moves(board: Bitboard, piece_bb: np.uint64, piece: Piece):
    if piece == Piece.PAWN:
        move_bb = pawn_moves(board, piece_bb)
    elif piece == Piece.TOWER | Piece.TWOCOLTOWER:
        move_bb = tower_moves(piece_bb) & ~board.pieces[board.color][Piece.ALLTOWERS]


def pawn_moves(board: Bitboard, piece_bb: np.uint64):
    normal = pawn_normal(piece_bb) & ~board.pieces[board.color][Piece.ALLTOWERS]
    normal &= ~board.each_side[board.opp_color]
    diag = pawn_diag(piece_bb) & ~board.each_side[board.color]
    return normal | diag


def pawn_normal(piece_bb: np.uint64):
    right = (piece_bb & ~h_column) << np.uint8(1)
    left = (piece_bb & ~a_column) >> np.uint(1)
    up = piece_bb << np.uint8(8)
    return right | left | up


def pawn_diag(piece_bb: np.uint64):
    left_up = (piece_bb & ~a_column) << np.uint8(7)
    right_up = (piece_bb & ~h_column) << np.uint8(9)
    return left_up | right_up


    # check needed for corners and b/g columns and then check whether the target spot is occupied by a friendly tower
def tower_moves(piece_bb: np.uint64):
    left_wide = (piece_bb & ~ab_column) << np.uint8(6)
    left_high = (piece_bb & ~a_column) << np.uint8(15)
    right_wide = (piece_bb & ~gh_column) << np.uint8(10)
    right_high = (piece_bb & ~h_column) << np.uint8(17)
    return left_wide | left_high | right_wide | right_high