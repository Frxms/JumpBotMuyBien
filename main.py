from util.generator import createVis
from util.search import Node, Tree, createTree, recEndgame, alphaBeta


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
    search_value = alphaBeta(tree.root, 2, -1000000, 1000000, True)
    child: Node = tree.get_root_children(search_value)
    print(child.move)


def clientRun(fen: str, depth=3):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    for row in board:
        print(row)
    node = Node(board)
    if not recEndgame(board):
        return
    tree = Tree(node)
    createTree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    #print(tree.root)
    search_value = alphaBeta(tree.root, depth, -1000000, 1000000, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)
    print(child.move)
    return child.move


if __name__ == "__main__":
    fen = "2b0b0b0b0/2b03b01/1b02b0b02/1b01b04/1r0b0r0r03/2r01r0r02/3r02r01/3r0r0r0 r"
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    for row in board:
        print(row)
    print("--------------------------------------------------")
    fen = "2b0b0b0b0/2b03b01/1b02b0b02/1b01b04/1r0b0rr4/2r01r0r02/3r02r01/3r0r0r0 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    for row in board:
        print(row)
    print("--------------------------------------------------")
    fen = "2b0b0b0b0/2b03b01/1b03b02/1b01b0b03/1r0b0rr4/2r01r0r02/3r02r01/3r0r0r0 r"
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    for row in board:
        print(row)
    print("--------------------------------------------------")
