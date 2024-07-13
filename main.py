from util.bitboard.bb_helper import get_index
from util.bitboard.bb_search import bb_alpha_beta
# from util.twod_array.tree import Tree, create_tree
from util.bitboard.bb_tree import Tree, Node
from util.search import rec_endgame, alpha_beta
from util.bitboard.bitboard import GameBoard
from util.bitboard.moves import gen_moves


# def main_2_arrays(depth=3, best_move="C1-H1"):
#     fen1 = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
#     fen = "b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"
#     fen2 = "6/rr7/4r03/8/8/8/bb7/6 r"
#
#     splitted = fen2.split(" ")
#     turn = splitted[1]
#     board = create_vis(splitted[0])
#     node = Node(board)
#     if not rec_endgame(board):
#         print("Game already ended")
#         return
#     tree = Tree(node)
#     create_tree(parent=tree.root, depth=depth, turn=turn, tree=tree)
#     search_value = alpha_beta(tree.root, depth, -10000, 10000, False if turn == "b" else True)
#     child: Node = tree.get_root_children(search_value)
#     print(f"{best_move} --> {child.move}")


def main_bitboard(depth=3, best_move="C1-H1"):
    fen = "b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"
    fen1 = "b04b0/r07/8/8/8/8/8/6 r"
    board = GameBoard(fen)
    board.__str__()
    print(gen_moves(board, True))
    # todo um weitere moves zu generieren und um moves anzuwenden, immer mit board arbeiten


def test_move_user():
    fen = "6/8/3rb4/2r05/2r05/8/8/6 b"
    board = GameBoard(fen)
    print("Starting Board:")
    print(board.__str__())
    moveset = gen_moves(board, True)
    print(moveset)
    reverse_set = board.use_move(moveset[2])
    print(f"Applied move: {moveset[3]}")
    print(board.__str__())
    print(f"Revert the move: {board.unmove(reverse_set)}")
    print(board.__str__())


def test_tree_insert(depth=2):
    fen = "b0b0b0b0b0b0/1b0b0b0b0b0b01/8/8/8/8/1r0r0r0r0r0r01/r0r0r0r0r0r0 b"
    board = GameBoard(fen)
    if board.is_endgame():
        print("Game already ended")
        return
    node = Node(board, False)
    tree = Tree(node)
    tree.create_bb_tree(tree.root, depth=depth)

def client_run(fen, depth=3):
    board = GameBoard(fen)
    node = Node(board, False)
    tree = Tree(node)
    tree.create_bb_tree(node, 3)
    search_value = bb_alpha_beta(tree.root, 3, -100000, 100000, board.alpha_beta_bool())
    child: Node = tree.get_root_children(search_value)
    return f"{get_index(child.move[0], True)}-{get_index(child.move[1], True)}"

if __name__ == "__main__":
    test_tree_insert()
