import numpy as np

from util.bitboard.bitboard import GameBoard
from util.bitboard.bb_helper import set_bits, get_bits
from util.bitboard.constants import Color, Piece

CENTER = np.uint64(0x183C3C180000)
red_pawn = np.array(
    [0, 0, 0, 0, 0, 0, 0, 0,
     5, 5, 5, 5, 5, 5, 5, 5,
     10, 10, 10, 10, 10, 10, 10, 10,
     10, 10, 10, 15, 15, 10, 10, 10,
     10, 15, 15, 20, 20, 15, 15, 10,
     10, 15, 20, 20, 20, 20, 15, 10,
     20, 20, 25, 30, 30, 25, 20, 20,
     0, 100, 100, 100, 100, 100, 100, 0
     ], dtype='uint64')
blue_pawn = np.array(
    [0, 100, 100, 100, 100, 100, 100, 0,
     20, 20, 25, 30, 30, 25, 20, 20,
     10, 15, 20, 20, 20, 20, 15, 10,
     10, 15, 15, 20, 20, 15, 15, 10,
     10, 10, 10, 15, 15, 10, 10, 10,
     10, 10, 10, 10, 10, 10, 10, 10,
     5, 5, 5, 5, 5, 5, 5, 5,
     0, 0, 0, 0, 0, 0, 0, 0,
     ], dtype='uint64')
red_tower = np.array(
    [0, 0, 0, 0, 0, 0, 0, 0,
     5, 5, 5, 5, 5, 5, 5, 5,
     10, 10, 10, 15, 15, 10, 10, 10,
     10, 15, 15, 20, 20, 15, 15, 10,
     10, 15, 20, 20, 20, 20, 15, 10,
     20, 20, 25, 30, 30, 25, 20, 20,
     20, 20, 25, 30, 30, 25, 20, 20,
     0, 100, 100, 100, 100, 100, 100, 0
     ], dtype='uint64')
blue_tower = np.array(
    [0, 100, 100, 100, 100, 100, 100, 0,
     20, 20, 25, 30, 30, 25, 20, 20,
     20, 20, 25, 30, 30, 25, 20, 20,
     10, 15, 20, 20, 20, 20, 15, 10,
     10, 15, 15, 20, 20, 15, 15, 10,
     10, 10, 10, 15, 15, 10, 10, 10,
     10, 10, 10, 10, 10, 10, 10, 10,
     0, 0, 0, 0, 0, 0, 0, 0,
     ], dtype='uint64')


def bb_evaluate(board: GameBoard):
    # red is positive
    # blue is negative
    result = np.int64(0)
    result += np.int64(endgame(board))
    result += np.int64(piece_eval(board))
    result += np.int64(center_eval(board))
    result += np.int64(placement_eval(board))
    return result


def piece_eval(board: GameBoard):
    pawn_count = set_bits(board.pieces[Color.RED][Piece.PAWN]) - set_bits(board.pieces[Color.BLUE][Piece.PAWN])
    tower_count = set_bits(board.pieces[Color.RED][Piece.TOWER]) - set_bits(board.pieces[Color.BLUE][Piece.TOWER])
    twocol_tower_count = (set_bits(board.pieces[Color.RED][Piece.TWOCOLTOWER])
                          - set_bits(board.pieces[Color.BLUE][Piece.TWOCOLTOWER]))
    return pawn_count * 10 + tower_count * 20 + twocol_tower_count * 25


def placement_eval(board):
    blue_p = get_bits(board.pieces[Color.BLUE][Piece.PAWN])
    blue_t = get_bits(board.pieces[Color.BLUE][Piece.ALLTOWERS])
    red_p = get_bits(board.pieces[Color.RED][Piece.PAWN])
    red_t = get_bits(board.pieces[Color.RED][Piece.ALLTOWERS])
    blue_eval = np.uint64(0)
    red_eval = np.uint64(0)
    for piece in blue_p:
        blue_eval += np.uint64(blue_pawn[np.uint8(np.log2(piece))])
    for piece in blue_t:
        blue_eval += np.uint64(blue_tower[np.uint8(np.log2(piece))])
    for piece in red_p:
        red_eval += np.uint64(red_pawn[np.uint8(np.log2(piece))])
    for piece in red_t:
        red_eval += np.uint64(red_tower[np.uint8(np.log2(piece))])
    return np.int64(red_eval) - np.int64(blue_eval)  # Convert to signed int64 before subtraction


def center_eval(board: GameBoard):
    red_center = set_bits(board.each_side[Color.RED] & CENTER)
    blue_center = set_bits(board.each_side[Color.BLUE] & CENTER)
    return red_center * 5 - blue_center * 5


def endgame(board: GameBoard):
    if board.is_endgame():
        if board.color == Color.RED:
            return -10000
        else:
            return 10000
    else:
        return 0
