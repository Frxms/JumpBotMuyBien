import time
from util.engine import calcMove
from util.generator import createVis
from util.search import Node, recEndgame, Tree, createTree, minimax, global_count, \
    global_count_minimax, \
    printGlobal, clear_global, alphaBeta_windows

expected = "C5-C6"
window = 2
file_path = "aspiration_output.txt"


def alphaBetaTest_windows(fen3="3b01b0/3bb1b02/8/8/8/2r0b0r02/8/0r04r0 b", bestmove="D6-D7", depth=3, window=10):
    splitted = fen3.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    createTree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = alphaBeta_windows(tree.root, depth, -10000, 10000, False if turn == "b" else True, window)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"3 moves to win took: {elapsed_time} seconds {bestmove} --> res: {child.move}")
    print("-----------------------------")
    return child.move


if __name__ == "__main__":
    fen = "6/4b01b01/8/5b01b0/2b04r0/1b04r01/5r01rr/1r04 b"
    bestMove = "C5-C6"
    #alphaBetaTest(fen, bestMove, 4)

    while True:
        result = alphaBetaTest_windows(fen, bestMove, 4, window)
        with open(file_path, "a") as file:
            file.write(f"\n\nexpected: {expected}\nresult: {result}\namount: {printGlobal(False)}\nwindow: {window}\n")

        if result == expected:
            print(f"Expected value {expected} obtained with {printGlobal(False)} iterations and window: {window}")
            break
        else:
            print(f"Expected value {expected} not obtained with {printGlobal(False)} iterations and window: {window}")
            window -= 0.11
            clear_global()
