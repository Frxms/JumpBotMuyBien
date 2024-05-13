import unittest
from main import *
from models import *

class MyTestCase(unittest.TestCase):
    FEN = "r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01"
    def test_createVis(self):
        self.assertEqual(createVis(FEN), [['r', '', 'r', 'r', '', 'r'], ['', 'r', 'rr', '', 'r', 'r', 'r', ''], ['', '', '', 'r', '', '', '', ''], ['', '', 'b', '', '', '', '', ''], ['', '', '', '', 'r', 'b', '', ''], ['', '', '', '', '', '', '', ''], ['', 'b', 'b', 'b', 'b', 'b', 'b', ''], ['', 'b', 'b', 'b', 'b', '']])

    def test_calcMove(self):
        board = createVis(FEN)
        self.assertEqual(calcMove(board, "b"), [[]])

    def test_diaCalc(self):
        self.assertTrue(diaCalc("b", ['', 'r', 'rr', '', 'r', 'r', 'r', ''], 2))
        self.assertFalse(diaCalc("b", ['', 'r', 'rr', '', 'r', 'r', 'r', ''], 1))
        self.assertTrue(diaCalc("r", ['', 'b', 'bb', '', 'b', 'b', 'b', ''], 2))
        self.assertFalse(diaCalc("r", ['', 'b', 'bb', '', 'b', 'b', 'b', ''], 1))

    def test_createSpielstein(self):
        self.assertEqual(Spielstein("r").farbe, "r")
        self.assertEqual(Spielstein("r", "b", True).farbe2, "b")
        self.assertEqual(Spielstein("r", "b", True).farbe, "r")
        self.assertTrue(Spielstein("r", "b", True).isWhopper)
        self.assertFalse(Spielstein("r").isWhopper)

    def test_get_all_moves(self):
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()
