from typing import Any, List
from util.engine import calcMove
from util.generator import generateBoard


class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def __repr__(self):
        return f"Key: {self.value}, Children: {self.children}"

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

    def get_leafs(self):
        if self.root is None:
            return []
        return self.root.get_leafs()

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

    def minimax(self, node, depth, alpha, beta, maximizing_player):
        if depth == 0:  #&& isGameOver(node):
            return eval(node)

        if node is None:
            return 0  # In case the node is None, return 0

        if len(node.children) == 0:
            return node.score

        if maximizing_player:
            max_eval = alpha
            for child in node.children:
                max_eval = max(max_eval, self.minimax(child, depth - 1, max_eval, beta, False))
                if max_eval >= beta:
                    break
            return max_eval

        else:
            min_eval = beta
            for child in node.children:
                min_eval = min(min_eval, self.minimax(child, depth - 1, alpha, min_eval, True))
                if min_eval <= alpha:
                    break
            return min_eval


def createTree(parent: Node, depth: int, turn: str, tree: Tree) -> Any:
    if depth == 0:
        return
    pboard = parent.value
    if recEndgame(pboard, turn):
        moves = calcMove(pboard, turn)
    else:
        return

    for move in moves:
        nboard = generateBoard(pboard, move, turn)
        node = Node(nboard)
        tree.insert(pboard, node)
    if turn == "b":
        turn = "r"
    else:
        turn = "b"
    depth -= 1
    for child in parent.get_leafs():
        createTree(child, depth, turn, tree)


def recEndgame(board: List, turn):
    # if board.__getitem__("r"):
    #     pass
    return True


if __name__ == '__main__':
    tree = Tree()
