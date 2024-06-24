import numpy as np

EMPTY_BB = np.uint64(0)

def to_bitboard(index): # returns the piece in a bb
    return np.uint64(1) << np.uint8(index)

def is_set(bb, field):
    return (to_bitboard(field) & bb) != EMPTY_BB


def corner_check(field):
    # return true, if the field is in a corner field
    corner_restriction = np.uint64(0x8100000000000081)
    return None if (to_bitboard(field) & ~corner_restriction) != EMPTY_BB else True


def get_bits(bb: np.uint64):    # returns every piece as its own bb
    empty_board = np.uint64(0)
    results = []
    while bb != empty_board:
        lsb = bb & -bb
        results.append(lsb)
        bb ^= lsb
    return results


def reverse_mask(x: np.uint64):
    x = np.uint64(x)
    x = ((x & np.uint64(0x5555555555555555)) << np.uint8(1)) | ((x & np.uint64(0xAAAAAAAAAAAAAAAA)) >> np.uint8(1))
    x = ((x & np.uint64(0x3333333333333333)) << np.uint8(2)) | ((x & np.uint64(0xCCCCCCCCCCCCCCCC)) >> np.uint8(2))
    x = ((x & np.uint64(0x0F0F0F0F0F0F0F0F)) << np.uint8(4)) | ((x & np.uint64(0xF0F0F0F0F0F0F0F0)) >> np.uint8(4))
    x = ((x & np.uint64(0x00FF00FF00FF00FF)) << np.uint8(8)) | ((x & np.uint64(0xFF00FF00FF00FF00)) >> np.uint8(8))
    x = ((x & np.uint64(0x0000FFFF0000FFFF)) << np.uint8(16)) | ((x & np.uint64(0xFFFF0000FFFF0000)) >> np.uint8(16))
    x = ((x & np.uint64(0x00000000FFFFFFFF)) << np.uint8(32)) | ((x & np.uint64(0xFFFFFFFF00000000)) >> np.uint8(32))
    return x


def piece_index(bb):
    pass