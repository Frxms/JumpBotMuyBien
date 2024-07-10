from util.twod_array.tree import Node, rec_endgame, Tree, create_tree
from util.twod_array.engine import calcMove
from util.twod_array.generator import create_vis
from util.twod_array.evaluate import evaluate
from util.search import alpha_beta, minimax, alpha_beta_count, minimax_count

import time


def move_test(fen, game_type):
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(create_vis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{game_type} game took: {elapsed_time} seconds")


def eval_test(fen, game_type):
    splitted = fen.split(" ")
    result = []
    start_time = time.time()
    for i in range(1000):
        res1 = evaluate(create_vis(splitted[0]))
        if res1 not in result:
            result.append(res1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{game_type} game took: {elapsed_time} seconds")
    print(f"array length: {len(result)} with {result[0]}")


def alpha_beta_test(fen: str, move_count: int, expected: str, depth: int,  counter: bool):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = create_vis(splitted[0])
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(tree.root, depth, turn, tree)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"{move_count} move(s) to win tree took {elapsed_time1}")
    start_time = time.time()

    search_value = alpha_beta(tree.root, depth, -10000, 10000, False if turn == "b" else True)
    if counter:
        alpha_beta_count()
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"{move_count} move(s) to win with depth {depth} took: {elapsed_time} seconds. {expected} --> res: {child.move}")


def minimax_test(fen: str, move_count: int, expected: str, depth: int, counter: bool):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = create_vis(splitted[0])
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(tree.root, depth, turn, tree)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"{move_count} move(s) to win tree took {elapsed_time1}")
    start_time = time.time()

    search_value = minimax(tree.root, depth,  False if turn == "b" else True)
    if counter:
        minimax_count()
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(
        f"{move_count} move(s) to win with depth {depth} took: {elapsed_time} seconds. {expected} --> res: {child.move}")


def move_perf():
    print("2D-twod_array move generation:")
    move_test("b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b", "early")
    print("-----------------------------")
    move_test("b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b", "mid")
    print("-----------------------------")
    move_test("3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b", "end")
    print("**************************************************************************************")


def eval_perf():
    print("2D-twod_array evaluation performance:")
    eval_test("b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b", "early")
    print("-----------------------------")
    eval_test("b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b", "mid")
    print("-----------------------------")
    eval_test("3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b", "end")
    print("**************************************************************************************")


def minimax_perf(counter):
    print("2D-twod_array minimax performance:")
    minimax_test("b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b", 1, "D6-E8", 2, counter)
    print("-----------------------------")
    minimax_test("2b03/r07/3r04/6rr1/4bb3/2b04bb/3rr1rr2/5r0 b", 1, "H6-G8", 2, counter)
    print("-----------------------------")
    minimax_test("b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", 2, "F3-F2", 3, counter)
    print("**************************************************************************************")


def alpha_beta_perf(counter):
    print("2D-twod_array alpha-beta performance:")
    alpha_beta_test("b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b", 1, "D6-E8", 2, counter)
    print("-----------------------------")
    alpha_beta_test("2b03/r07/3r04/6rr1/4bb3/2b04bb/3rr1rr2/5r0 b", 1, "H6-G8", 2, counter)
    print("-----------------------------")
    alpha_beta_test("b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", 2, "F3-F2", 3, counter)
    print("**************************************************************************************")


def general_test():
    move_perf()
    eval_perf()
    alpha_beta_perf(True)


if __name__ == "__main__":
    general_test()
