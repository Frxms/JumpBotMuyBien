import numpy as np

from .bitboard.bb_helper import EMPTY_BB
from .bitboard.constants import Color, Piece
from .bitboard.moves import gen_moves, h_column, a_column, gh_column, ab_column
from .bitboard.bitboard import GameBoard


above_5th_rank = np.uint64(0xFFFFFF0000000000)
below_3rd_rank =np.uint64(0x0000000000FFFFFF)
#------------------------------------------------------
first_rank = np.uint64(0x00000000000000FF)
second_rank = np.uint64(0x000000000000FF00)
third_rank = np.uint64(0x0000000000FF0000)
fourth_rank = np.uint64(0x00000000FF000000)
fifth_rank = np.uint64(0x000000FF00000000)
sixth_rank = np.uint64(0x0000FF0000000000)
seventh_rank = np.uint64(0x00FF000000000000)
eighth_rank = np.uint64(0xFF00000000000000)

def organize_moves_by_importance(moves, color):
    first = []
    second = []
    third = []
    fourth = []
    fifth = []
    last = []
    for move in moves:
        if color == Color.BLUE:
            if move[2] & below_3rd_rank != EMPTY_BB:
                last.append(move)
            elif move[2] & fourth_rank != EMPTY_BB:
                fifth.append(move)
            elif move[2] & fifth_rank != EMPTY_BB:
                fourth.append(move)
            elif move[2] & sixth_rank != EMPTY_BB:
                third.append(move)
            elif move[2] & seventh_rank != EMPTY_BB:
                second.append(move)
            elif move[2] & eighth_rank != EMPTY_BB:
                first.append(move)

        else:
            if move[2] & above_5th_rank != EMPTY_BB:
                last.append(move)
            elif move[2] & first_rank != EMPTY_BB:
                fifth.append(move)
            elif move[2] & second_rank != EMPTY_BB:
                fourth.append(move)
            elif move[2] & third_rank != EMPTY_BB:
                third.append(move)
            elif move[2] & fourth_rank != EMPTY_BB:
                second.append(move)
            elif move[2] & fifth_rank != EMPTY_BB:
                first.append(move)

    return first + second + third + fourth + fifth + last


def organize_moves_quiet(board: GameBoard):
    moves = gen_moves(board, True)
    important_moves = []
    capture_moves = []
    other_moves = []

    for move in moves:
        current_pos = np.uint64(move[1])
        target_pos = np.uint64(move[2])

# ----------------------------------------------------- moves that are made in the last 3 rows

        if (((target_pos & ~below_3rd_rank) and ((current_pos >> np.uint8(8)) == target_pos)) or ((target_pos & ~above_5th_rank) and ((current_pos << np.uint8(8)) == target_pos))):
            important_moves.append(move)

# ------------------------------------------------------ capturing moves on first lines on own side | Red
        elif ((target_pos & ~below_3rd_rank) and ((((current_pos & ~a_column) << np.uint8(7)) == target_pos) or (((current_pos & ~h_column) << np.uint8(9)) == target_pos))):
            capture_moves.append(move)

# ----------------------------------------------------- capturing moves on first lines on own side | Blue

        elif ((target_pos & ~above_5th_rank) and ((((current_pos & ~h_column) >> np.uint8(7)) == target_pos) or (((current_pos & ~a_column) >> np.uint8(9)) == target_pos))):
            capture_moves.append(move)

# ----------------------------------------------------- Tower Moves | Red

        elif (((current_pos & ~gh_column) >> np.uint8(6)) == target_pos) or (((current_pos & ~h_column) >> np.uint8(15)) == target_pos) or (((current_pos & ~ab_column) >> np.uint8(10)) == target_pos) or (((current_pos & ~a_column) >> np.uint8(17)) == target_pos):
            other_moves.append(move)

# ----------------------------------------------------- Tower Moves | Blue

        elif ((current_pos & ~ab_column) << np.uint8(6)) == target_pos or ((current_pos & ~a_column) << np.uint8(15)) == target_pos or ((current_pos & ~gh_column) << np.uint8(10)) == target_pos or ((current_pos & ~h_column) << np.uint8(17)) == target_pos:
            other_moves.append(move)



    sortedMoves = mvv_lva(board, capture_moves)
    finalmoves = important_moves + other_moves
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
