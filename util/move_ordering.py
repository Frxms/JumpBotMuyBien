import numpy as np

from .bitboard.constants import Color, Piece
from .bitboard.moves import gen_moves, h_column, a_column
from .bitboard.bitboard import GameBoard

#for blue
mask_above_4th_rank = np.uint64(0xFFFFFFFF00000000)
#for red
mask_below_or_in_4th_rank =np.uint64(0x00000000FFFFFFFF)
def organize_moves_by_importance(moves):
    quiet_moves = []
    first_rows_moves = []
    last_rows_moves = []

    for move in moves:
        current_pos = np.uint64(move[1])
        target_pos = np.uint64(move[2])

        if ((current_pos & ~h_column) << np.uint8(1)) == target_pos or ((current_pos & ~a_column) >> np.uint8(1)) == target_pos:
            quiet_moves.append(move)

        #important moves
        elif ((current_pos & ~mask_below_or_in_4th_rank) and ((current_pos >> np.uint8(8)) == target_pos)) or ((current_pos & ~mask_above_4th_rank) and ((current_pos << np.uint8(8)) == target_pos)):
            last_rows_moves.append(move)

        elif (current_pos & ~mask_below_or_in_4th_rank) and ((((current_pos & ~a_column) << np.uint8(7)) == target_pos) or (((current_pos & ~h_column) << np.uint8(9)) == target_pos)):
            first_rows_moves.append(move)

        elif (current_pos & ~mask_above_4th_rank)  and ((((current_pos & ~h_column) >> np.uint8(7)) == target_pos) or (((current_pos & ~a_column) >> np.uint8(9)) == target_pos)):
            first_rows_moves.append(move)
        else:
            quiet_moves.append(move)

    return last_rows_moves + first_rows_moves + quiet_moves


def organize_moves_quiet(board: GameBoard):
    moves = gen_moves(board, True)
    non_quiet_moves = []

    for move in moves:
        current_pos = np.uint64(move[1])
        target_pos = np.uint64(move[2])

        if ((current_pos & ~mask_below_or_in_4th_rank) and ((current_pos >> np.uint8(8)) == target_pos)) or ((current_pos & ~mask_above_4th_rank) and ((current_pos << np.uint8(8)) == target_pos)):
            non_quiet_moves.append(move)

        elif (current_pos & ~mask_below_or_in_4th_rank) and ((((current_pos & ~a_column) << np.uint8(7)) == target_pos) or (((current_pos & ~h_column) << np.uint8(9)) == target_pos)):
            non_quiet_moves.append(move)

        elif (current_pos & ~mask_above_4th_rank) and ((((current_pos & ~h_column) >> np.uint8(7)) == target_pos) or (((current_pos & ~a_column) >> np.uint8(9)) == target_pos)):
            non_quiet_moves.append(move)


    sortedMoves = mvv_lva(board, non_quiet_moves)
    finalmoves = []
    for move in sortedMoves:
        finalmoves.append(move[0])
    return finalmoves


point_attribution = {(Piece.PAWN, 10), (Piece.TOWER, 20), (Piece.TOWER, 25)}


# value beaten - value beater
def mvv_lva(board, moves):
    beater = 0
    beaten = 0
    movelist = []
    for move in moves:
        reverse_set = board.use_move(move)
        if reverse_set[1] is not None:
            for piece, points in point_attribution:
                if piece == reverse_set[0]:
                    beater = points
            for piece, points in point_attribution:
                if piece == reverse_set[1]:
                    beaten = points
            val1 = beaten - beater
            movelist.append((move, val1))
            board.unmove(reverse_set)
    return sorted(movelist, key=lambda x: x[1])
