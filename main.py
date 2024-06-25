from util.Bitboard import Bitboard
from util.Bitboard.bbHelperFunc import reverse_mask, get_index
from util.Tree import Tree, create_tree
from util.generator import createVis
from util.search import Node, rec_endgame, alpha_beta
from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.moves import get_bits, gen_moves, a_column, h_column, ab_column, gh_column
from util.Bitboard.constants import Color, Piece
import numpy as np

def main_2_arrays(depth=3, best_move="C1-H1"):
    fen1 = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
    fen = "b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"
    fen2 = "6/rr7/4r03/8/8/8/bb7/6 r"

    splitted = fen2.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)
    create_tree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    search_value = alpha_beta(tree.root, depth, -10000, 10000, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)
    print(f"{best_move} --> {child.move}")


def main_bitboard(depth=3, best_move="C1-H1"):
    fen = "b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"
    fen1 = "b04b0/r07/8/8/8/8/8/6 r"
    board = GameBoard(fen)
    board.__str__()
    print(gen_moves(board, True))
    # todo um weitere moves zu generieren und um moves anzuwenden, immer mit board arbeiten
    node = Node(board)
    if board.is_endgame():
        print("Game already ended")
        return
    tree = Tree(node)
    tree.create_bb_tree(tree.root, board, depth)




if __name__ == "__main__":
    main_bitboard()