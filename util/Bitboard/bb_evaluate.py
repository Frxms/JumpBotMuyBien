import numpy as np

from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.bbHelperFunc import set_bits
from util.Bitboard.constants import Color, Piece


CENTER = np.uint64(0x183C3C180000)



def evaluate(board: GameBoard):
    # red is positive
    # blue is negative
    result = endgame(board)
    result += piece_eval(board)
    result += center_eval(board)


def piece_eval(board: GameBoard):
    pawn_count = set_bits(board.pieces[Color.RED][Piece.PAWN]) - board.pieces[Color.BLUE][Piece.PAWN]
    tower_count = set_bits(board.pieces[Color.RED][Piece.TOWER]) - set_bits(board.pieces[Color.BLUE][Piece.TOWER])
    twocol_tower_count = (set_bits(board.pieces[Color.RED][Piece.TWOCOLTOWER])
                          - set_bits(board.pieces[Color.BLUE][Piece.TWOCOLTOWER]))
    return pawn_count * 10 + tower_count * 20 + twocol_tower_count * 25

def placement_eval(board: GameBoard):
    # give more points as the piece goes forward
    # the towers in the front also get more points
    pass


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
