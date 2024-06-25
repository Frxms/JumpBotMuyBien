import time

from util.Tree import Node, create_tree, Tree
from util.generator import createVis
from util.search import rec_endgame, minimax, alpha_beta, print_global


def alphabeta1Move(fen1="b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b"):
    splitted = fen1.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.1 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = alpha_beta(tree.root, 2, -10000, 10000, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"1.1 move to win took: {elapsed_time} seconds. D6-E8 --> res: {child.move}")
    print("-----------------------------")
    # for node in tree.root.children:
    #     print(f"The move: {node.move} results in a board with {node.eval}pt.")


def alphabeta1Move1(fen2="2b03/r07/3r04/6rr1/4bb3/2b04bb/3rr1rr2/5r0 b"):
    splitted = fen2.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = alpha_beta(tree.root, 2, -10000, 10000, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"1.2 move to win took: {elapsed_time} seconds. H6-G8 --> res: {child.move}")
    print("-----------------------------")


def alphabeta2Moves(fen3="b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r"):
    splitted = fen3.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=3, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = alpha_beta(tree.root, 3, -10000, 10000, True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"2 moves to win took: {elapsed_time} seconds. F3-F2 --> res: {child.move}")


def minimax1Move(fen1="b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b"):  #own test
    splitted = fen1.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.1 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimax(tree.root, 2, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"1.1 move to win took: {elapsed_time} seconds. D6-E8 --> res: {child.move}")
    # for node in tree.root.children:
    #     print(f"The move: {node.move} results in a board with {node.eval}pt.")
    print("-----------------------------")


def minimax1Move1(fen2="2b03/r07/3r04/6rr1/4bb3/2b04bb/3rr1rr2/5r0 b"):
    splitted = fen2.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimax(tree.root, 2, False)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"1.2 move to win took: {elapsed_time} seconds. H6-G8 --> res: {child.move}")
    print("-----------------------------")


def minimax2Moves(fen3="b01b03/4b03/1b03r02/3rbb03/1bb4r01/8/2r02r02/1r0r02r0 r"):
    splitted = fen3.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=3, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimax(tree.root, 3, True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"2 moves to win took: {elapsed_time} seconds. F3-F2 --> res: {child.move}")


def minimaxTest(fen3="3b01b0/3bb1b02/8/8/8/2r0b0r02/8/0r04r0 b", bestmove = "D6-D7", depth = 3):
    splitted = fen3.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimax(tree.root, depth, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"3 moves to win took: {elapsed_time} seconds {bestmove} --> res: {child.move}")
    print("-----------------------------")

def alphaBetaTest(fen3="3b01b0/3bb1b02/8/8/8/2r0b0r02/8/0r04r0 b", bestmove = "D6-D7", depth = 3):
    splitted = fen3.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not rec_endgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    create_tree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = alpha_beta(tree.root, depth, -10000, 10000, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"3 moves to win took: {elapsed_time} seconds {bestmove} --> res: {child.move}")
    print("-----------------------------")

def bothTests(fen="3b01b0/3bb1b02/8/8/8/2r0b0r02/8/0r04r0 b", bestMove = "D6-D7", depth = 3):
    minimaxTest(fen, bestMove, depth)
    alphaBetaTest(fen, bestMove, depth)
    print_global()

if __name__ == "__main__":
    # fen = "6/4b01b01/8/5b01b0/2b04r0/1b04r01/5r01rr/1r04 b"
    # bestMove = "C5-C6"
    # bothTests(fen, bestMove, 3)
    bothTests()