import time

from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.bb_helper import get_index
from util.Bitboard.moves import gen_moves
from util.Tree import Node, rec_endgame, Tree
from util.search import alpha_beta, bb_alpha_beta


def bb_move_performance():
    fen = "b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b"
    start_time = time.time()
    board = GameBoard(fen)
    print(board.__str__())
    for i in range(1000):
        gen_moves(board, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"early Game took: {elapsed_time} seconds")

    fen = "b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b"
    start_time = time.time()
    board = GameBoard(fen)
    print(board.__str__())
    for i in range(1000):
        gen_moves(board, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"mid Game took: {elapsed_time} seconds")

    fen = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
    board = GameBoard(fen)
    print(board.__str__())
    start_time = time.time()
    for i in range(1000):
        gen_moves(board, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"end Game took: {elapsed_time} seconds")


def alphabeta_1_move(fen="b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b", depth=2):
    board = GameBoard(fen)
    # print(board.__str__())
    node = Node(board, False)
    if board.is_endgame():
        print("Game already ended")

        return
    tree = Tree(node)
    start_time1 = time.time()

    tree.create_bb_tree(node, depth)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.1 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = bb_alpha_beta(tree.root, depth, -100000, 100000, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"1.1 move to win took: {elapsed_time} seconds. D6-E8 --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")
    print("-----------------------------")


def alphabeta_1_move_1(fen="2b03/r07/3r04/6rr1/4bb3/2b04bb/3rr1rr2/5r0 b", depth=2):
    board = GameBoard(fen)
    # print(board.__str__())
    node = Node(board, False)
    if board.is_endgame():
        print("Game already ended")

        return
    tree = Tree(node)
    start_time1 = time.time()

    tree.create_bb_tree(node, depth)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = bb_alpha_beta(tree.root, depth, -100000, 100000, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"1.2 move to win took: {elapsed_time} seconds. H6-G8 --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")
    print("-----------------------------")


def alphabeta_2_moves(fen="b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", depth=3):
    board = GameBoard(fen)
    print(board.__str__())
    node = Node(board, False)
    if board.is_endgame():
        print("Game already ended")

        return
    tree = Tree(node)
    start_time1 = time.time()

    tree.create_bb_tree(node, depth)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = bb_alpha_beta(tree.root, depth, -100000, 100000, True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"2 move to win took: {elapsed_time} seconds. F3-F2 --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")
    print("-----------------------------")


def alphabeta_2_moves_quiet(fen="b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", depth=3):
    board = GameBoard(fen)
    print(board.__str__())
    node = Node(board, False)
    if board.is_endgame():
        print("Game already ended")

        return
    tree = Tree(node)
    start_time1 = time.time()

    tree.create_bb_tree(node, depth)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = alpha_beta_quiet(tree.root, depth, -100000, 100000, True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"2 move to win took: {elapsed_time} seconds. F3-F2 --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")
    print("-----------------------------")


if __name__ == "__main__":
    alphabeta_1_move(depth=3)
