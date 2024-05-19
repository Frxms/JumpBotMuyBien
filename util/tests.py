import unittest
from main import *
from collections import Counter

class MyTestCase(unittest.TestCase):
    FEN = "b0b01b0b0b0/1b0b02b0b01/3b0b03/2b05/3r04/2r05/1r01rr1r0r01/r0r02r0r0 b"
    def test_calc_move(self):
        myList = calcMove(createVis(self.FEN), "r", True)
        expected = ['B8 - B7', 'B8 - C8', 'D8 - D7', 'D8 - C8', 'D8 - E8', 'E8 - E7', 'E8 - D8', 'E8 - F8', 'G8 - G7',
                    'G8 - F8', 'B7 - B6', 'B7 - A7', 'C7 - E6', 'C7 - A6', 'C7 - D5', 'C7 - B5', 'E7 - E6', 'E7 - D7',
                    'E7 - F7', 'F7 - F6', 'F7 - E7', 'F7 - G7', 'G7 - G6', 'G7 - F7', 'G7 - H7', 'D6 - D5', 'D6 - C5',
                    'D6 - C6', 'D6 - E6', 'E4 - E3', 'E4 - D4']
        print(myList)
        try:
            assert Counter(myList) == Counter(expected), "Lists are not equal"

        except AssertionError as e:
            print(e)
            print("Expected: ", expected)
            print("Actual: ", myList)
            self.fail()


if __name__ == '__main__':
    unittest.main()
