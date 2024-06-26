import numpy as np

from evaluate import evaluate
from Bitboard.constants import Color, Piece
from Bitboard.moves import gen_moves, h_column, a_column
from Bitboard.Bitboard import GameBoard


def organize_moves_by_importance(board: GameBoard):
    moves = gen_moves(board, False)
    quiet_moves = []
    capture_moves = []


    #for blue
    mask_above_4th_rank = 0xFFFFFFFF00000000
    #for red
    mask_below_or_in_4th_rank = 0x00000000FFFFFFFF

    for move in moves:
        current_pos = move[1]
        target_pos = move[2]

        if ((current_pos & ~h_column) << np.uint8(1)) == target_pos or ((current_pos & ~a_column) >> np.uint8(1)) == target_pos:
            quiet_moves.append(move)

        # front move
        elif (current_pos << np.uint8(8)) == target_pos or (current_pos >> np.uint8(8)) == target_pos:
            capture_moves.append(move)

        if ((current_pos & ~mask_below_or_in_4th_rank) and board.color == Color.RED) or ((current_pos & ~mask_above_4th_rank) and board.color == Color.BLUE):
            capture_moves.append(move)

    return quiet_moves, capture_moves


def organize_moves_quiet(board: GameBoard):
    moves = gen_moves(board, False)
    non_quiet_moves = []

    for move in moves:
        current_pos = move[1]
        target_pos = move[2]

        if ((current_pos & ~h_column) << np.uint8(1)) != target_pos and ((current_pos & ~a_column) >> np.uint8(1)) != target_pos:
            non_quiet_moves.append(move)

    sortedMoves = mvv_lva(board, non_quiet_moves)
    return sortedMoves
