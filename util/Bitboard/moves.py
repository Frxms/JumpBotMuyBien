import numpy as np

from util.Bitboard import Bitboard
from util.Bitboard.constants import Color, Piece, Row, Column
from util.Bitboard.bbHelperFunc import to_bitboard


def get_bits(board):    # returns every piece as its own bb
    results = []
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
    while board != empty_board:
        ls1b = board & -board
        res = index64[(ls1b * debruijn) >> np.uint8(58)]
        res = np.uint8(res)
        yield res
        board ^= to_bitboard(res)

#field class that splits into rows and columns by /8 and get index after - mod
#returns bitboard for that
#compare current board with field board to get position and surroundings of current bit
#bit shift so see options

empty_board = np.uint64(0)
a_column = np.uint64(0x0101010101010101)
h_column = np.uint64(0x8080808080808080)

def move_normal(board : Bitboard, index):
    piece = to_bitboard(index)
    left = (piece & ~AColumn) >> 1
    right = (piece & ~HColumn) << 1
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
    pass