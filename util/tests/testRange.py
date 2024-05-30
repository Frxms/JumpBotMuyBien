import time
from typing import Any
from util.Tree import Node, Tree, createTree
from util.engine import calcMove, refactor_to_readable
from util.generator import generateBoard, createVis
from util.search import recEndgame, minimax


def testNewInsert(parent: Node, depth: int, turn: str, tree: Tree) -> Any:
    if depth == 0:
        return
    pboard = parent.value
    if recEndgame(pboard):
        moves = calcMove(pboard, turn)
        if not moves:
            return
    else:
        return
    for move in moves:
        nboard = generateBoard(pboard, move, turn)
        node = Node(nboard)
        node.move = refactor_to_readable(move)
        tree.newInsert(parent, node)
    if turn == "b":
        turn = "r"
    else:
        turn = "b"

    depth -= 1
    tree.currentBottom = tree.get_leafs()
    for child in tree.currentBottom:
        testNewInsert(child, depth, turn, tree)

def testRun(fen="3b01b0/3bb1b02/8/8/8/2r0b0r02/8/0r04r0 b", bestMove = "D6-D7", depth = 3):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    node = Node(board)
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)
    start = time.time()
    testNewInsert(parent=tree.root, depth=depth, turn=turn, tree=tree)
    end = time.time()
    print(f"it took {end - start} seconds")
    search_value = minimax(tree.root, 4, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)
    print(f"{bestMove} --> {child.move}")

def oldInsertTest(fen="3b01b0/3bb1b02/8/8/8/2r0b0r02/8/0r04r0 b", bestMove = "D6-D7", depth = 3):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    node = Node(board)
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)
    start = time.time()
    createTree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    end = time.time()
    print(f"it took {end - start} seconds")
    search_value = minimax(tree.root, 4, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)
    print(f"{bestMove} --> {child.move}")

if __name__ == "__main__":
    testRun(fen="6/4b01b01/8/5b01b0/2b04r0/1b04r01/5r01rr/1r04 b", bestMove="C5-C6 oder C5-B5", depth=4)
    # oldInsertTest(fen="6/4b01b01/8/5b01b0/2b04r0/1b04r01/5r01rr/1r04 b", bestMove="C5-C6 oder C5-B5", depth=4)