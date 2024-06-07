from enum import IntEnum


class Color(IntEnum):
    BLUE = 0
    RED = 1


class Piece(IntEnum):
    PAWN = 0
    TOWER = 1
    TWOCOLTOWER = 2


class Row(IntEnum):
    ONE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7


class Column(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7
