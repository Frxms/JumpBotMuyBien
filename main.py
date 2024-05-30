from util.generator import createVis
from util.search import recEndgame, alphaBeta
from util.Tree import Tree, createTree, Node


def main(fen="3b01b0/3bb1b02/8/8/8/2r0b0r02/8/0r04r0 b", bestMove = "D6-D7", depth = 3):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    node = Node(board)
    if not recEndgame(board):
        print("Game already ended")
        return
    tree = Tree(node)
    createTree(parent=tree.root, depth=depth, turn=turn, tree=tree)
    search_value = alphaBeta(tree.root, depth, -10000, 10000, False if turn == "b" else True)
    child: Node = tree.get_root_children(search_value)
    print(f"{bestMove} --> {child.move}")


if __name__ == "__main__":
    main()
