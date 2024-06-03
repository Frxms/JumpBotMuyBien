import numpy as np
import Bitboard
from constants import Color, Piece, Row, Column

def get_bits(board):
    results = []
    debruijn = np.uint64(0x03f79d71b4cb0a89)
    index64 = [
        0, 1, 2, 53, 3, 7, 54, 27,
        4, 38, 41, 8, 34, 55, 48, 28,
        62, 5, 39, 46, 44, 42, 22, 9,
        24, 35, 59, 56, 49, 18, 29, 11,
        63, 52, 6, 26, 37, 40, 33, 47,
        61, 45, 43, 21, 23, 58, 17, 10,
        51, 25, 36, 32, 60, 20, 57, 16,
        50, 31, 19, 15, 30, 14, 13, 12
    ]
    while board != 0:
        ls1b = board & -board
        compB = (ls1b * debruijn) >> 58
        results.append[index64[compB]]
        board &= board -1
    return results
def move_row(pos, board):
    pass


def move_col(pos, board):
    pass


def move_diag(pos, board):
    pass


def move_antidiag(pos, board):
    pass

def get_all_moves(board):




