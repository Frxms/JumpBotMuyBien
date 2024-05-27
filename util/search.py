from typing import Any, List
from util.engine import calcMove, refactor_to_readable
from util.generator import generateBoard
from util.evaluate import evaluate


class Node:
    def __init__(self, value):
        self.value = tuple(value) if isinstance(value, list) else value  # Ensure the value is hashable
        self.children = []
        self.eval = 0
        self.move = ""

    def __repr__(self):
        return "\n".join(self.value)


    def add_child(self, node):
        self.children.append(node)

    def get_leafs(self):
        leafs = []
        stack = [self]
        while stack:
            current_node = stack.pop()
            if not current_node.children:
                leafs.append(current_node)
            else:
                stack.extend(current_node.children)
        return leafs


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.nodes = {}


    def get_leafs(self):
        if self.root is None:
            return []
        return self.root.get_leafs()

    def get_root_children(self, minmaxVal):
        if self.root is None:
            return []
        for child in self.root.children:
            if child.eval == minmaxVal:
                return child

    def insert(self, parent_value, new_node):
        # ggf nur leafs durchsuchen wegen runtime
        if self.root is None:
            self.root = new_node
            return True
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.value == parent_value:
                current_node.add_child(new_node)
                return True
            queue.extend(current_node.children)
        return False


def minimax(node, depth, alpha, beta, maximizing_player):
    if depth == 0:  #&& isGameOver(node):
        node.eval = evaluate(node.value)
        return node.eval

    if len(node.children) == 0:
        node.eval = evaluate(node.value)
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, minimax(child, depth - 1, max_eval, beta, False))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, minimax(child, depth - 1, alpha, min_eval, True))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval

def minimaxOther(node: Node, depth: int, maximizing_player: bool):
    if depth == 0:  #&& isGameOver(node):
        node.eval = evaluate(node.value)
        return node.eval

    if len(node.children) == 0:
        node.eval = evaluate(node.value)
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        max_eval = -100000
        for child in node.children:
            max_eval = max(max_eval, minimaxOther(child, depth - 1, False))
        node.eval = max_eval
        return max_eval

    else:
        min_eval = 100000
        for child in node.children:
            min_eval = min(min_eval, minimaxOther(child, depth - 1, False))
        node.eval = min_eval
        return min_eval


def createTree(parent: Node, depth: int, turn: str, tree: Tree) -> Any:
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
        tree.insert(pboard, node)
    if turn == "b":
        turn = "r"
    else:
        turn = "b"
    depth -= 1
    for child in parent.get_leafs():
        createTree(child, depth, turn, tree)


def recEndgame(board: List):
    if "r" in board[7] or "b" in board[0]:
        return False
    if not (any('r' in cell or 'rr' in cell for row in board for cell in row) and any(
            'b' in cell or 'bb' in cell for row in board for cell in row)):
        return False
    #     pass
    return True


if __name__ == '__main__':
    a = [['X', '', '', '', '', '', '', 'X'], ['b', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''], ['X', '', '', '', '', '', '', 'X']]
    fen = "1r0r02r0/2r02r02/8/1bb4r01/3brb03/1b03r02/4b03/b01b03"
    print(recEndgame(a))
