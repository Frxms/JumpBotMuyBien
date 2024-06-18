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
a_column = np.uint64(0x0101010101010101)
h_column = np.uint64(0x8080808080808080)
corner_restriction = np.uint64(0x8100000000000081)

def get_bits(board):    # returns every piece as its own bb
    results = []
    while board != empty_board:
        lsb = board & -board
        results.append(lsb)
        board ^= lsb
    return results

#field class that splits into rows and columns by /8 and get index after - mod
#returns bitboard for that
#compare current board with field board to get position and surroundings of current bit
#bit shift so see options

def gen_moves(board: Bitboard, piece: Piece):
    if piece == Piece.PAWN:
        pass # todo pawn impl
    elif piece == Piece.TOWER:
        pass
    elif piece == Piece.TWOCOLTOWER:
        pass


def move_normal(board : Bitboard, index):
    piece = to_bitboard(index)
    left = (piece & ~a_column) >> 1
    right = (piece & ~h_column) << 1
    up = piece << 8

    left_move = (left & ~board.pieces[board.color][Piece.PAWN]) == np.uint64(0)
    right_move = (right & ~board.pieces[board.color][Piece.PAWN]) == np.uint64(0)
    up_move = (up & ~board.pieces[board.color][Piece.PAWN]) == np.uint64(0)

def stack_normal(board : Bitboard, index):
    piece = to_bitboard(index)
    left = (piece & ~a_column) >> 1
    right = (piece & ~h_column) << 1
    up = piece << 8

    left_move = (left & ~board.pieces[board.color][Piece.PAWN]) != np.uint64(0)
    right_move = (right & ~board.pieces[board.color][Piece.PAWN]) != np.uint64(0)
    up_move = (up & ~board.pieces[board.color][Piece.PAWN]) != np.uint64(0)
def attack_normal(board, index):
    piece = to_bitboard(index)
    left_up = (piece & ~a_column) << 7
    right_up = (piece & ~h_column) << 9

    mycolor = board.color.value ^ 1
    left_up_move = (left_up & board.pieces[mycolor][Piece.PAWN]) != np.uint64(0)
    right_up_move = (left_up & board.pieces[mycolor][Piece.PAWN]) != np.uint64(0)


def tower_moves(board: Bitboard, index):
    piece = to_bitboard(index)
    left_short = (piece & ~a_column) << np.uint8(6)
    left_high = (piece & ~a_column) << np.uint8(15)
    right_short = (piece & ~h_column) << np.uint8(10)
    right_high = (piece & ~h_column) << np.uint8(17)
    # check needed for corners and b/g columns
    # and then check whether the target spot is occupied by a friendly tower