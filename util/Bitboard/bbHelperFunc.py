import numpy as np

EMPTY_BB = np.uint64(0)

def is_set(bb, sq):
    return (sq.to_bitboard() & bb) != EMPTY_BB