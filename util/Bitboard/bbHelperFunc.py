import numpy as np

EMPTY_BB = np.uint64(0)

def is_set(bb, field):
    return (to_bitboard(field) & bb) != EMPTY_BB

def to_bitboard(index): # returns the piece in a bb
    return np.uint64(1) << np.uint64(index)