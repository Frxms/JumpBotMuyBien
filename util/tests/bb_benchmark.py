import time

from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.bb_helper import get_index
from util.Bitboard.moves import gen_moves
from util.Tree import Node, rec_endgame, Tree
from util.search import alpha_beta, bb_alpha_beta, alpha_beta_quiet


def bb_move_test(fen):
    start_time = time.time()
    board = GameBoard(fen)
    print(board.__str__())
    for i in range(1000):
        gen_moves(board, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"early Game took: {elapsed_time} seconds")


def bb_alpha_beta_test(fen: str, move_count: int, expected: str, depth: int):
    board = GameBoard(fen)
    node = Node(board, False)
    if board.is_endgame():
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    tree.create_bb_tree(node, depth)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.1 move to win tree took {elapsed_time1}")
    start_time = time.time()

    search_value = bb_alpha_beta(tree.root, depth, -100000, 100000, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{move_count} move(s) to win with depth {depth} took: {elapsed_time} seconds. "
          f"{expected} --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")
    print("-----------------------------")


def bb_alpha_beta_quiet_test(fen: str, move_count: int, expected: str, depth: int):
    board = GameBoard(fen)
    node = Node(board, False)
    if board.is_endgame():
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    tree.create_bb_tree(node, depth)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.1 move to win tree took {elapsed_time1}")
    start_time = time.time()

    search_value = alpha_beta_quiet(tree.root, depth, -100000, 100000, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{move_count} move(s) to win with depth {depth} took: {elapsed_time} seconds. "
          f"{expected} --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")
    print("-----------------------------")


def bb_move_perf():
    bb_move_test("b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b")
    bb_move_test("b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b")
    bb_move_test("3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b")


def bb_alpha_beta_perf():
    bb_alpha_beta_test("b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b", 1, "D6-E8", 2)
    bb_alpha_beta_test("2b03/r07/3r04/6rr1/4bb3/2b04bb/3rr1rr2/5r0 b", 1, "H6-G8", 2)
    bb_alpha_beta_test("b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", 1, "F3-F2", 3)
    
    
def bb_alpha_beta_quiet_perf():
    bb_alpha_beta_quiet_test("b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", 2, "F3-F2", 3)


if __name__ == "__main__":
    bb_move_perf()
    bb_alpha_beta_perf()
    bb_alpha_beta_quiet_perf()
