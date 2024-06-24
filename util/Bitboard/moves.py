import numpy as np

from util.Bitboard import Bitboard
from util.Bitboard.constants import Color, Piece, Row, Column
from util.Bitboard.bbHelperFunc import to_bitboard, reverse_mask, get_bits

blue_a_column = np.uint64(0x8101010101010181)
blue_ab_column = np.uint64(0x8303030303030383)
blue_h_column = np.uint64(0x8180808080808081)
blue_gh_column = np.uint64(0xC1C0C0C0C0C0C0C1)
corner = np.uint64(0x8100000000000081)


def gen_moves(board: Bitboard):
    # piece: Piece, index: np.uint64
    piece = []
    legal_moves = []
    for p in Piece:
        piece = get_bits(board.pieces[board.color][p])
        for piece_bb in piece:
            legal_moves.append((piece_bb, p, piece_moves(board, piece_bb, p)))
    return legal_moves
# todo mit yield umsetzten ist wahrscheinlich schneller


def piece_moves(board: Bitboard, piece_bb: np.uint64, piece: Piece):
    if piece == Piece.PAWN:
        return pawn_moves(board, piece_bb)
    elif piece == Piece.TOWER | Piece.TWOCOLTOWER:
        return tower_moves(piece_bb) & ~board.pieces[board.color][Piece.ALLTOWERS]


def pawn_moves(board: Bitboard, piece_bb: np.uint64):
    normal = pawn_normal(piece_bb) & ~board.pieces[board.color][Piece.ALLTOWERS]
    normal &= ~board.each_side[board.opp_color]
    diag = pawn_diag(piece_bb) & board.each_side[board.opp_color]
    return normal | diag


def pawn_normal(piece_bb: np.uint64):
    right = (piece_bb & ~blue_h_column) << np.uint8(1)
    left = (piece_bb & ~blue_a_column) >> np.uint(1)
    up = piece_bb << np.uint8(8)
    return (right | left | up) & ~corner


def pawn_diag(piece_bb: np.uint64):
    left_up = (piece_bb & ~blue_a_column) << np.uint8(7)
    right_up = (piece_bb & ~blue_h_column) << np.uint8(9)
    return left_up | right_up


def tower_moves(piece_bb: np.uint64):
    left_wide = (piece_bb & ~blue_ab_column) << np.uint8(6)
    left_high = (piece_bb & ~blue_a_column) << np.uint8(15)
    right_wide = (piece_bb & ~blue_gh_column) << np.uint8(10)
    right_high = (piece_bb & ~blue_h_column) << np.uint8(17)
    return left_wide | left_high | right_wide | right_high