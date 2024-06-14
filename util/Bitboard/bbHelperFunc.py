import numpy as np

EMPTY_BB = np.uint64(0)

def is_set(bb, field):
    return (to_bitboard(field) & bb) != EMPTY_BB

def corner_check(field):
    corner_restriction = np.uint64(0x8100000000000081)
    return None if (to_bitboard(field) & ~corner_restriction) != EMPTY_BB else True


def to_bitboard(index): # returns the piece in a bb
    return np.uint64(1) << np.uint8(index)