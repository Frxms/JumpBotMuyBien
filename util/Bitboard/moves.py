import numpy as np

from util.Bitboard import Bitboard
from util.Bitboard.constants import Color, Piece, Row, Column
from util.Bitboard.bb_helper import to_bitboard, reverse_mask, get_bits, get_index

a_column = np.uint64(0x8101010101010181)
ab_column = np.uint64(0x8303030303030383)
h_column = np.uint64(0x8180808080808081)
gh_column = np.uint64(0xC1C0C0C0C0C0C0C1)
corner = np.uint64(0x8100000000000081)


# returns set of (piece, starting bit, goal bit) when false
#  and else a set of (piece, starting bit, goal bit, moveset String)
# todo weniger for loops machen
def gen_moves(board: Bitboard, moveset_flag: bool):
    legal_moves = []
    moveset = []
    for piece_type in {Piece.PAWN, Piece.ALLTOWERS}:
        for piece_bb in get_bits(board.pieces[board.color][piece_type]):
            legal_moves.append((piece_bb, piece_type, piece_moves(board, piece_bb, piece_type)))
    if moveset_flag:
        for move in legal_moves:
            for target in get_bits(move[2]):
                moveset.append((move[1], move[0], target))
        return moveset
    else:
        for move in legal_moves:
            piece_index = get_index(move[0], True)
            for target in get_bits(move[2]):
                moveset_str = piece_index + "-" + get_index(target, True)
                moveset.append((move[1], move[0], target, moveset_str))
                # moveset.append((move[1], move[0], target))
        return moveset

# todo mit yield umsetzten ist wahrscheinlich schneller


# makes Piece specific function calls
def piece_moves(board: Bitboard, piece_bb: np.uint64, piece: Piece):
    if piece == Piece.PAWN:
        return pawn_moves(board, piece_bb)
    elif piece == Piece.ALLTOWERS:
        tower_moveset = blue_tower_moves(piece_bb) if board.color == Color.BLUE else red_tower_moves(piece_bb)
        return tower_moveset & ~board.pieces[board.color][Piece.ALLTOWERS]


def pawn_moves(board: Bitboard, piece_bb: np.uint64):
    normal = blue_pawn_normal(piece_bb) if board.color == Color.BLUE else red_pawn_normal(piece_bb)
    normal &= ~(board.pieces[board.color][Piece.ALLTOWERS] | board.each_side[board.opp_color])
    diag = blue_pawn_diag(piece_bb) if board.color == Color.BLUE else red_pawn_diag(piece_bb)
    diag &= board.each_side[board.opp_color]
    return normal | diag


def blue_pawn_normal(piece_bb: np.uint64):
    right = (piece_bb & ~h_column) << np.uint8(1)
    left = (piece_bb & ~a_column) >> np.uint8(1)
    up = piece_bb << np.uint8(8)
    return (right | left | up) & ~corner


# << left bit shift and >> right bit shift
def red_pawn_normal(piece_bb: np.uint64):
    right = (piece_bb & ~a_column) >> np.uint8(1)
    left = (piece_bb & ~h_column) << np.uint8(1)
    up = piece_bb >> np.uint8(8)
    return (right | left | up) & ~corner


def blue_pawn_diag(piece_bb: np.uint64):
    left_up = (piece_bb & ~a_column) << np.uint8(7)
    right_up = (piece_bb & ~h_column) << np.uint8(9)
    return left_up | right_up


def red_pawn_diag(piece_bb: np.uint64):
    left_up = (piece_bb & ~h_column) >> np.uint8(7)
    right_up = (piece_bb & ~a_column) >> np.uint8(9)
    return left_up | right_up


def blue_tower_moves(piece_bb: np.uint64):
    left_wide = (piece_bb & ~ab_column) << np.uint8(6)
    left_high = (piece_bb & ~a_column) << np.uint8(15)
    right_wide = (piece_bb & ~gh_column) << np.uint8(10)
    right_high = (piece_bb & ~h_column) << np.uint8(17)
    return (left_wide | left_high | right_wide | right_high) & ~corner


def red_tower_moves(piece_bb: np.uint64):
    left_wide = (piece_bb & ~gh_column) >> np.uint8(6)
    left_high = (piece_bb & ~h_column) >> np.uint8(15)
    right_wide = (piece_bb & ~ab_column) >> np.uint8(10)
    right_high = (piece_bb & ~a_column) >> np.uint8(17)
    return (left_wide | left_high | right_wide | right_high) & ~corner
