from util.Bitboard import Bitboard
from util.generator import createVis
from util.search import Node, Tree, createTree, recEndgame, alphaBeta
from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.moves import get_bits
from util.Bitboard.constants import Color, Piece

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

def test():
    board = GameBoard(Color.BLUE)
    board.gameStart()
    print(get_bits(board.get_pieceboard(Piece.PAWN, Color.BLUE)))


if __name__ == "__main__":
    test()
