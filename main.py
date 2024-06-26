from util.Bitboard import Bitboard
from util.Bitboard.bbHelperFunc import reverse_mask, get_index
from util.Tree import Tree, create_tree
from util.generator import createVis
from util.search import Node, rec_endgame, alpha_beta
from util.Bitboard.Bitboard import GameBoard, change_col
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


def test_move_user():
    fen = "6/8/3rb4/2r05/2r05/8/8/6 b"
    board = GameBoard(fen)
    print("Starting Board:")
    board.__str__()
    moveset = gen_moves(board, True)
    print(moveset)
    reverse_set = board.use_move(moveset[2])
    print(f"Applied move: {moveset[3]}")
    board.__str__()
    print(f"Revert the move: {board.unmove(reverse_set)}")
    board.__str__()

def test_tree_insert():
    fen = "6/8/3rb4/2r05/2r05/8/8/6 b"
    board = GameBoard(fen)
    print("Starting Board:")
    board.__str__()
    node = Node(board)
    tree = Tree(node)
    moves = gen_moves(board, True)
    for moveset in moves:
        reverse_set = board.use_move(moveset)
        new_node = Node(board)
        new_node.value.change_col()
        node.move = moveset[3]
        tree.insert(board, new_node)
        board.unmove(reverse_set)

def clientRun(fen: str, depth=3):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    for row in board:
        print(row)
    node = Node(board)
    if not recEndgame(board):
        return
    tree = Tree(node)
    createTree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    #print(tree.root)
    search_value = alphaBeta(tree.root, depth, -1000000, 1000000, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)
    print(child.move)
    return child.move


if __name__ == "__main__":
    test_tree_insert()