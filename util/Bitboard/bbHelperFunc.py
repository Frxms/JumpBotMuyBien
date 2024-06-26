import warnings

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


bit_count_table = [bin(i).count('1') for i in range(256)]


def count_set_bits_lookup_uint64(n):
    return (bit_count_table[n & 0xff] +
            bit_count_table[(n >> 8) & 0xff] +
            bit_count_table[(n >> 16) & 0xff] +
            bit_count_table[(n >> 24) & 0xff] +
            bit_count_table[(n >> 32) & 0xff] +
            bit_count_table[(n >> 40) & 0xff] +
            bit_count_table[(n >> 48) & 0xff] +
            bit_count_table[(n >> 56) & 0xff])


def get_bits(bb: np.uint64):    # returns every piece as its own bb
    results = []
    # with warnings.catch_warnings():
    #     warnings.simplefilter("ignore", RuntimeWarning)
    while bb != EMPTY_BB:
        lsb = bb & -bb
        results.append(lsb)
        bb ^= lsb
    return results


def set_bits(bb: np.uint64):
    count = 0
    while bb:
        bb &= bb - 1  # Clear the least significant bit set
        count += 1
    return count

def reverse_mask(x: np.uint64):
    x = np.uint64(x)
    x = ((x & np.uint64(0x5555555555555555)) << np.uint8(1)) | ((x & np.uint64(0xAAAAAAAAAAAAAAAA)) >> np.uint8(1))
    x = ((x & np.uint64(0x3333333333333333)) << np.uint8(2)) | ((x & np.uint64(0xCCCCCCCCCCCCCCCC)) >> np.uint8(2))
    x = ((x & np.uint64(0x0F0F0F0F0F0F0F0F)) << np.uint8(4)) | ((x & np.uint64(0xF0F0F0F0F0F0F0F0)) >> np.uint8(4))
    x = ((x & np.uint64(0x00FF00FF00FF00FF)) << np.uint8(8)) | ((x & np.uint64(0xFF00FF00FF00FF00)) >> np.uint8(8))
    x = ((x & np.uint64(0x0000FFFF0000FFFF)) << np.uint8(16)) | ((x & np.uint64(0xFFFF0000FFFF0000)) >> np.uint8(16))
    x = ((x & np.uint64(0x00000000FFFFFFFF)) << np.uint8(32)) | ((x & np.uint64(0xFFFFFFFF00000000)) >> np.uint8(32))
    return x


field_mapper = np.array([
    "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
    "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
    "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
    "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
    "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
    "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
    "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
    "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"
], dtype='object')


def get_index(bb: np.uint64, flag: bool):
    if flag:
        return field_mapper[np.uint8(np.log2(bb))]
    else:
        return np.uint8(np.log2(bb))