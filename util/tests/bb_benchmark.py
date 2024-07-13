import time

from util.MCTS.mcts import MCTS
from util.bitboard.bb_search import bb_alpha_beta_count, bb_quiet_count
from util.bitboard.bitboard import GameBoard
from util.bitboard.bb_evaluate import bb_evaluate
from util.bitboard.bb_helper import get_index
from util.bitboard.constants import Color
from util.bitboard.moves import gen_moves
from util.bitboard.bb_tree import Node, Tree
from util.bitboard.bb_search import bb_alpha_beta, alpha_beta_quiet


def bb_move_test(fen, game_type):
    start_time = time.time()
    board = GameBoard(fen)
    for i in range(1000):
        gen_moves(board, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{game_type} game took: {elapsed_time} seconds")


def bb_eval_test(fen, game_type):
    board = GameBoard(fen)
    result = []
    start_time = time.time()
    for i in range(1000):
        res1 = bb_evaluate(board)
        if res1 not in result:
            result.append(res1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{game_type} game took: {elapsed_time} seconds")
    print(f"array length: {len(result)} with {result[0]}")


def bb_alpha_beta_test(fen: str, move_count: int, expected: str, depth: int, counter: bool):
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
    print(f"{move_count} move(s) to win tree took {elapsed_time1}")
    start_time = time.time()

    search_value = bb_alpha_beta(tree.root, depth, -100000, 100000, board.alpha_beta_bool())
    if counter:
        bb_alpha_beta_count()
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{move_count} move(s) to win with depth {depth} took: {elapsed_time} seconds. "
          f"{expected} --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")


def bb_alpha_beta_quiet_test(fen: str, move_count: int, expected: str, depth: int, counter: bool):
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
    print(f"{move_count} move(s) to win tree took {elapsed_time1}")
    start_time = time.time()

    search_value = alpha_beta_quiet(tree.root, depth, -100000, 100000, board.alpha_beta_bool())
    if counter:
        bb_quiet_count()
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{move_count} move(s) to win with depth {depth} took: {elapsed_time} seconds. "
          f"{expected} --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")


def bb_MCTS_test():
    board = GameBoard()
    while not board.is_terminal():
        print(f"Current player: {'Red' if board.color == Color.RED else 'Blue'}")
        best_move = get_best_move(board, iterations=1000)
        board = board.make_move(best_move)
        print(f"Move: {get_index(best_move[1], True)}-{get_index(best_move[2], True)}")
        print(f"Move: {best_move}")
        print(board)

    result = board.get_result(Color.RED)
    if result == 1:
        print("Red wins!")
    elif result == 0:
        print("Blue wins!")
    else:
        print("It's a draw!")


def get_best_move(board, iterations=1000):
    mcts = MCTS(board, iterations=iterations)
    return mcts.search()


def bb_move_perf():
    print("bitboard move generation:")
    bb_move_test("b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b", "early")
    print("-----------------------------")
    bb_move_test("b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b", "mid")
    print("-----------------------------")
    bb_move_test("3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b", "end")
    print("**************************************************************************************")


def bb_eval_perf():
    print("bitboard evaluation performance:")
    bb_eval_test("b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b", "early")
    print("-----------------------------")
    bb_eval_test("b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b", "mid")
    print("-----------------------------")
    bb_eval_test("3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b", "end")
    print("**************************************************************************************")


def bb_alpha_beta_perf(counter):
    print("bitboard alpha-beta performance")
    bb_alpha_beta_test("b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b", 1, "D6-E8", 2, counter)
    print("-----------------------------")
    bb_alpha_beta_test("2b03/r07/3r04/6rr1/4bb3/2b04bb/3rr1rr2/5r0 b", 1, "H6-G8", 2, counter)
    print("-----------------------------")
    bb_alpha_beta_test("b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", 2, "F3-F2", 3, counter)
    print("**************************************************************************************")


def bb_alpha_beta_quiet_perf(counter):
    print("bitboard alpha-beta quiet performance")
    bb_alpha_beta_quiet_test("b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", 2, "F3-F2", 3, counter)
    print("**************************************************************************************")


def bb_general_test():
    bb_move_perf()
    bb_eval_perf()
    bb_alpha_beta_perf(True)

    # depth=5 Fen String "6/1b06/5b02/2b05/2b05/4r03/2r05/6 b"


if __name__ == "__main__":
    bb_MCTS_test()
    #bb_alpha_beta_perf(True)
    #bb_alpha_beta_test("6/1b06/5b02/2b05/2b05/4r03/2r05/6 b", 3, "C4-C5", 5, True)
    #bb_alpha_beta_quiet_test("6/1b06/5b02/2b05/2b05/4r03/2r05/6 b", 3, "C4-C5", 5, True)
