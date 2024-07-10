import time

from util.bitboard.bitboard import GameBoard
from util.bitboard.bb_helper import get_index
from util.search import Node, Tree, print_global, clear_global, alphaBeta_windows

expected = "C5-C6"
window = 100
file_path = "aspiration_output.txt"


def alphaBetaTest_windows(fen3="b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r", bestmove="D6-D7", depth=3, window=10):
    board = GameBoard(fen3)
    #print(board.__str__())
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

    search_value = alphaBeta_windows(tree.root, depth, -10000, 10000, True, window)
    #search_value = bb_alpha_beta(tree.root, depth, -10000, 10000, True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(
        f"2 move to win took: {elapsed_time} seconds. F3-F2 --> res: {get_index(child.move[0], True)}-{get_index(child.move[1], True)}")
    print("-----------------------------")
    return f"{get_index(child.move[0], True)}-{get_index(child.move[1], True)}"

if __name__ == "__main__":
    fen = "b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r"
    bestMove = "F3-F2"
    #alphaBetaTest(fen, bestMove, 4)

    while True:
        result = alphaBetaTest_windows(fen, bestMove, 3, window)
        with open(file_path, "a") as file:
            file.write(f"\n\nexpected: {expected}\nresult: {result}\namount: {print_global(False)}\nwindow: {window}\n")

        if result == expected:
            print(f"Expected value {expected} obtained with {print_global()} iterations and window: {window}")
            break
        else:
            print(f"Expected value {expected} not obtained with {print_global()} iterations and window: {window}")
            window -= 2
            clear_global()
