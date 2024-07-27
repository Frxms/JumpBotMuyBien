import unittest

from util.bitboard.bb_helper import get_index
from util.bitboard.bitboard import GameBoard
from util.bitboard.moves import gen_moves


class Maintest(unittest.TestCase):
    def test_earlygame(self):
        fen = "b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b"
        board = GameBoard(fen)
        list = []
        for move in gen_moves(board, True):
            list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
        myList = sorted(list)
        expected = sorted(["B2-A2", "B2-B3", "B1-B2", "B1-C1", "C2-A3", "C2-B4", "C2-D4", "C2-E3", "D3-C3", "D3-C4",
                           "D3-D4", "D3-E3", "D1-C1", "D1-D2", "D1-E1", "E2-D2", "E2-E3", "E2-F2", "E1-D1", "E1-E2",
                           "E1-F1", "F2-E2", "F2-F3", "F2-G2", "G2-F2", "G2-G3", "G2-H2", "G1-F1", "G1-G2", "E5-D5",
                           "E5-E6"])

        try:
            assert myList == expected, "Lists are not equal"

        except AssertionError as e:
            print(e)
            print("Expected: ", expected)
            print("Actual: ", myList)
            self.fail()


    def test_MTY_midgame(self):
        fen = "b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b"
        board = GameBoard(fen)
        list = []
        for move in gen_moves(board, True):
            list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
        myList = sorted(list)
        expected = sorted(["B1-B2", "B1-C1", "E1-E2", "E1-D1", "E1-F1", "G1-G2", "G1-F1", "D2-D3", "D2-C2", "D2-E2",
                           "F2-F3", "F2-E2", "F2-G2", "A3-A4", "A3-B3", "D3-D4", "D3-C3", "D3-E3", "G3-G4", "G3-F3",
                           "G3-H3", "A4-A5", "A4-B4", "C4-C5", "C4-B4", "C4-D4"])

        try:
            assert myList == expected, "Lists are not equal"

        except AssertionError as e:
            print(e)
            print("Expected: ", expected)
            print("Actual: ", myList)
            self.fail()

    def test_endgame(self):
        fen = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
        board = GameBoard(fen)
        list = []
        for move in gen_moves(board, True):
            list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
        myList = sorted(list)
        expected = sorted(["E1-D1", "E1-E2", "E1-F1", "C2-B2", "C2-C3", "C2-D2", "B3-A3", "B3-C3", "B3-C4", "F4-E4",
                           "F4-F5", "F4-G4", "G7-F7", "G7-G8", "G7-H7"])

        try:
            assert myList == expected, "Lists are not equal"

        except AssertionError as e:
            print(e)
            print("Expected: ", expected)
            print("Actual: ", myList)
            self.fail()

class EarlyGame(unittest.TestCase):
    def test_jumpstr_earlygame(self):
        fen = "1b04/2b03b01/b01rr5/r02b01b02/1b06/1r02b03/8/1r01r0r0r0 b"
        board = GameBoard(fen)
        list = []
        for move in gen_moves(board, True):
            list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
        myList = sorted(list)
        expected = sorted(["C1-B1", "C1-D1", "C1-C2", "C2-B2", "C2-D2", "G2-F2", "G2-H2", "G2-G3", "A3-B3", "D4-C4",
                           "D4-E4", "D4-D5", "F4-E4", "F4-G4", "F4-F5", "B5-A5", "B5-C5", "E6-D6", "E6-F6", "E6-E7"])

        try:
            assert myList == expected, "Lists are not equal"

        except AssertionError as e:
            print(e)
            print("Expected: ", expected)
            print("Actual: ", myList)
            self.fail()


class Endgame(unittest.TestCase):
    def test_own_endgame(self):
        fen = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
        board = GameBoard(fen)
        list = []
        for move in gen_moves(board, True):
            list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
        myList = sorted(list)
        expected = sorted(["A2-C1", "G3-G2", "G3-F3", "G3-H3"])

        try:
            assert myList == expected, "Lists are not equal"

        except AssertionError as e:
            print(e)
            print("Expected: ", expected)
            print("Actual: ", myList)
            self.fail()


    def test_solobolo_endgame(self):
        fen = "6/2b02b02/2r02r02/8/8/2b02b02/2r02r02/6 b"
        board = GameBoard(fen)
        list = []
        for move in gen_moves(board, True):
            list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
        myList = sorted(list)
        expected = sorted(["C6-B6", "C6-D6", "F6-E6", "F6-G6", "C2-B2", "C2-D2", "F2-E2", "F2-G2"])

        try:
            assert myList == expected, "Lists are not equal"

        except AssertionError as e:
            print(e)
            print("Expected: ", expected)
            print("Actual: ", myList)
            self.fail()

    class Edgecases(unittest.TestCase):
        def test_own_edgecases(self):
            fen = "3rr1b0/7r0/r07/8/8/8/b0b0b05/6 r"
            board = GameBoard(fen)
            list = []
            for move in gen_moves(board, True):
                list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
            myList = sorted(list)
            expected = sorted(["H2-G2", "H2-G1", "A3-B3", "A3-A2"])

            try:
                assert myList == expected, "Lists are not equal"

            except AssertionError as e:
                print(e)
                print("Expected: ", expected)
                print("Actual: ", myList)
                self.fail()


        def test_mccurdy_edgecases(self):
            fen = "6/1b06/8/2b01bbb0rb1/1rbr0rr1r0r01/8/b07/6 b"
            board = GameBoard(fen)
            list = []
            for move in gen_moves(board, True):
                list.append(f"{get_index(move[1], True)}-{get_index(move[2], True)}")
            myList = sorted(list)
            expected = sorted(["B2-A2", "B2-B3", "B2-C2", "C4-B4", "C4-D4", "C4-D5", "E4-C5", "E4-D6", "E4-F6", "E4-G5",
                               "F4-G5", "G4-E5", "G4-F6", "G4-H6", "B5-A7", "B5-C7", "B5-D6", "A7-B7"])

            try:
                assert myList == expected, "Lists are not equal"

            except AssertionError as e:
                print(e)
                print("Expected: ", expected)
                print("Actual: ", myList)
                self.fail()


if __name__ == '__main__':
    unittest.main()
