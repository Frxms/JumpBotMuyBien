from util.engine import calcMove, refactor_to_readable
from util.generator import createVis, generateFEN
from util.search import Node, Tree, createTree, recEndgame, minimax


def perfTest():
    import time
    fen = "b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"early Game took: {elapsed_time} seconds")

    fen = "b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"mid Game took: {elapsed_time} seconds")

    fen = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"end Game took: {elapsed_time} seconds")


def test():
    # r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01 r
    FEN1 = "1b04/2b03b01/b01rr5/r02b01b02/1b06/1r02b03/8/1r01r0r0r0 b"  # 36 Züge
    FEN2 = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
    FEN3 = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
    a = [['X', '', 'r', 'r', 'r', '', 'r', 'X'], ['', 'r', 'rr', '', 'r', 'r', 'r', ''],
         ['', '', '', 'r', '', '', '', ''], ['', '', 'b', '', '', '', '', ''], ['', '', '', '', 'r', 'b', '', ''],
         ['', '', '', '', '', '', '', ''], ['', 'b', 'b', 'b', 'b', 'b', 'b', ''],
         ['X', '', 'b', 'b', 'b', 'b', '', 'X']]
    splitted = FEN3.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    moves = calcMove(board, turn)
    print(moves)
    # chosen_one = random.choice(moves)
    # print(refactor_to_readable(chosen_one), chosen_one)
    # print(generateFEN(board, chosen_one, turn))
    # print(generateFEN(board, chosen_one, turn))
    for move in moves:
        print(f"this move: {move}")
        print(f"was converted to: {refactor_to_readable(move)}")
        print(generateFEN(board, move, turn))
    perfTest()


def allMoves(fen):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    if not recEndgame():
        moves = calcMove(board, turn)
    return moves


def main():
    fen1 = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
    fen = "6/rr7/8/8/8/8/bb7/6 r"
    fen2 = "6/rr7/2r05/8/8/8/bb7/6 r"

    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    print(board)
    node = Node(board)
    if not recEndgame(board):
        return
    tree = Tree(node)
    createTree(parent=tree.root, depth=2, turn=turn, tree=tree)
    print(tree.root)
    search_value = minimax(tree.root, 2, -1000000, 1000000, True)
    child: Node = tree.get_root_children(search_value)
    print(child.move)


    # for move in moves:
    #     new_board = generateBoard(board, move, turn)
    #     if not boards:
    #         node = Node(new_board)
    #         tree.insert(parent_value=tree.root, new_node=node)
    #         boards.append(node)
    #     else:
    #         node = Node(new_board)
    #         tree.insert(parent_value=boards[-1], new_node=node)
    #         boards.append(node)


if __name__ == "__main__":
    main()
