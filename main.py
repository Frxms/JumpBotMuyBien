from util.Bitboard import Bitboard
from util.Bitboard.bbHelperFunc import reverse_mask
from util.generator import createVis
from util.search import Node, Tree, createTree, recEndgame, alphaBeta
from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.moves import get_bits, gen_moves, a_column, h_column, ab_column, gh_column
from util.Bitboard.constants import Color, Piece
import numpy as np

def main_2_arrays():
    fen1 = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
    fen = "b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"
    fen2 = "6/rr7/4r03/8/8/8/bb7/6 r"

    splitted = fen2.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    print(board)
    node = Node(board)
    if not recEndgame(board):
        return
    tree = Tree(node)
    createTree(parent=tree.root, depth=2, turn=turn, tree=tree)
    print(tree.root)
    search_value = alphaBeta(tree.root, 2, -1000000, 1000000, True)
    child: Node = tree.get_root_children(search_value)
    print(child.move)


def main_bitboard():
    fen1 = "b04b0/r07/8/8/8/8/8/6 b"
    fen2 = "b05/8/8/8/8/8/3b04/6 b"
    fen3 = "6/r07/8/8/8/8/b07/6 b"
    fen4 = "6/r07/8/8/8/8/b07/r05 b"
    fen5 = "6/8/8/8/8/8/8/2r03 r"
    fen6 = "b05/r07/8/8/8/8/8/6 r"
    fen7 = "6/3bb4/8/8/8/8/8/6 b"
    board = GameBoard(fen7)
    board.__str__()
    print(gen_moves(board))


def piece_test():
    board = GameBoard("5b0/r07/8/8/8/8/8/6 r")
    # board.gameStart()
    print(get_bits(board.get_pieceboard(Piece.PAWN, Color.BLUE)))


def get_moves():
    board = GameBoard("b04b0/r07/8/8/8/8/8/6 r")
    gen_moves(board)


if __name__ == "__main__":
    main_bitboard()
