import copy
from typing import List

from util.bitboard.bitboard import GameBoard
from util.bitboard.moves import gen_moves
from util.move_ordering import organize_moves_by_importance

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

        # moves = organize_moves_by_importance(moves)
        # if depth == 1:
        #     print("hi")

        for moveset in moves:
            board_copy = copy.deepcopy(pboard)
            board_copy.use_move(moveset)
            new_node = Node(board_copy)
            new_node.move = moveset[1], moveset[2]
            self.insert(pboard, new_node)

        depth -= 1
        for child in parent.get_leafs():
            self.create_bb_tree(child, depth)