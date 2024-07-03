import copy
from typing import List

from util.Bitboard.Bitboard import GameBoard
from util.Bitboard.moves import gen_moves
from util.Array.engine import refactor_to_readable, calcMove
from util.Array.generator import generateBoard


class Node:
    def __init__(self, value, flag=True):
        self.value: GameBoard = value
        if flag:
            self.value.change_col()
        self.move = None
        self.eval = 0
        self.children = []  # needed to reverse this board to the previous
        self.parent = None

    def __repr__(self):
        return self.value.board

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
        self.counter = 0
        self.leaf_nodes = set()


    def get_leafs(self):
        if self.root is None:
            return []
        elif not self.root.children:
            return [self.root]
        return self.root.get_leafs()

    def get_root_children(self, minimax_val):
        if self.root is None:
            return []
        for child in self.root.children:
            if child.eval == minimax_val:
                return child

    def get_minimax_moves(self, minimax_val):
        result = []
        if self.root is None:
            return []
        for child in self.root.children:
            if child.eval == minimax_val:
                result.append(child)
        return result

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

    def _insert(self, parent_value, new_node):
        if self.root is None:
            self.root = new_node
            self.leaf_nodes.add(new_node)
            return True
        return self._insert_dfs(self.root, parent_value, new_node)

    def _insert_dfs(self, current_node, parent_value, new_node):
        if current_node.value == parent_value:
            current_node.add_child(new_node)
            self.leaf_nodes.add(new_node)
            return True
        for child in current_node.children:
            if self._insert_dfs(child, parent_value, new_node):
                return True
        return False


    def create_bb_tree(self, parent: Node, depth: int):
        if depth == 0:
            return
        pboard = parent.value
        if not pboard.is_endgame():
            moves = gen_moves(pboard, True)
            if not moves:
                return
        else:
            return

        for moveset in moves:
            board_copy = copy.deepcopy(pboard)
            reverse_set = board_copy.use_move(moveset)
            new_node = Node(board_copy)
            new_node.move = moveset[1], moveset[2]
            self.insert(pboard, new_node)

        depth -= 1
        for child in parent.get_leafs():
            self.create_bb_tree(child, depth)



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
