from typing import List

import numpy as np

from util.Bitboard import Bitboard
from util.Bitboard.moves import gen_moves
from util.engine import refactor_to_readable, calcMove
from util.generator import generateBoard


class Node:
    def __init__(self, value):
        self.value = tuple(value) if isinstance(value, list) else value  # Ensure the value is hashable
        self.children = []
        self.eval = 0
        self.move = ""
        self.parent = None

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
        self.currentBottom: Node = []
        self.counter = 0

    def get_leafs(self):
        if self.root is None:
            return []
        elif not self.root.children:
            return [self.root]
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


    def new_insert(self, parent: Node, node: Node):
        if self.root is None:
            self.root = node
            return True
        leafs = self.tree.currentBottom
        for leaf in leafs:
            if leaf == parent:
                leaf.add_child(node)
            else:
                print("could not store node")

    def create_bb_tree(self, parent: Node, board: Bitboard, depth: int):
        if depth == 0:
            return
        pboard = parent.value
        if not board.is_endgame():
            moves = gen_moves(pboard, True)
            if not moves:
                return
        else:
            return
        for move in moves:
            pboard.use_move(move)
        self.create_bb_tree(parent, board, depth)


def create_tree(parent: Node, depth: int, turn: str, tree: Tree):
    if depth == 0:
        return
    pboard = parent.value
    if rec_endgame(pboard):
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
        create_tree(child, depth, turn, tree)


def rec_endgame(board: List):
    if "r" in board[7] or "b" in board[0]:
        return False
    if not (any('r' in cell or 'rr' in cell for row in board for cell in row) and any(
            'b' in cell or 'bb' in cell for row in board for cell in row)):
        return False
    #     pass
    return True


# todo so implementieren, dass man es nicht in ein FEN umstrukturiert;
#  nur ganz am Anfang als String annehmen und dann den richtigen move zurückgeben
