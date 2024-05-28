import time
from util.engine import calcMove
from util.generator import createVis
from util.search import Node, recEndgame, Tree, createTree, minimaxOther, minimax


def alphabeta1Move(fen1="b0b0b0b0b01/1b01b02b01/2r05/2r01b03/1r06/3bb4/2r0r02r01/r01r0r0r0r0 b"):
    splitted = fen1.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    node = Node(board)
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    createTree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.1 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimax(tree.root, 2, -10000, 10000, False)
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
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    createTree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimax(tree.root, 2, -10000, 10000, False)
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
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    createTree(parent=tree.root, depth=3, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimax(tree.root, 3, -10000, 10000, True)
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
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    createTree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.1 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimaxOther(tree.root, 2, False)
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
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    createTree(parent=tree.root, depth=2, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"1.2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimaxOther(tree.root, 2, False)
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
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)

    start_time1 = time.time()

    createTree(parent=tree.root, depth=3, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimaxOther(tree.root, 3, True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"2 moves to win took: {elapsed_time} seconds. F3-F2 --> res: {child.move}")


def minimaxTest(fen3="1b01b01b0/1b06/3b04/8/4b0r02/2b03r01/3r0r03/r03r01 b"):
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

    createTree(parent=tree.root, depth=3, turn=turn, tree=tree)
    # print(tree.root)

    end_time1 = time.time()
    elapsed_time1 = end_time1 - start_time1
    print(f"2 move to win tree took {elapsed_time1}")

    start_time = time.time()

    search_value = minimaxOther(tree.root, 3, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"2 moves to win took: {elapsed_time} seconds --> res: {child.move}")
    print("-----------------------------")


if __name__ == "__main__":
    minimaxTest()
