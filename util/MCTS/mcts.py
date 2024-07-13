import random

import numpy as np

from util.MCTS.mcts_node import MCTSNode
from util.bitboard.bb_evaluate import bb_evaluate
from util.bitboard.constants import Color


class MCTS:
    def __init__(self, root_state, iterations=1000, exploration_weight=1.4):
        self.root = MCTSNode(root_state)
        self.iterations = iterations
        self.exploration_weight = exploration_weight

    def search(self):
        for _ in range(self.iterations):
            node = self.select(self.root)
            if not node.game_state.is_terminal():
                node = self.expand(node)
            result = self.simulate(node)
            self.backpropagate(node, result)
        return self.get_best_move()

    def select(self, node):
        while not node.game_state.is_terminal():
            if not node.fully_expanded():
                return node
            node = node.best_child(self.exploration_weight)
            reverse_set = node.game_state.use_move(node.move)
            node.reverse_set = reverse_set
        return node

    def expand(self, node):
        move = random.choice(node.untried_moves)
        reverse_set = node.game_state.use_move(move)
        child = node.add_child(move, reverse_set)
        return child

    def simulate(self, node):
        state = node.game_state
        moves_made = []
        while not state.is_terminal():
            move = node.rollout_policy(state.get_legal_moves())
            reverse_set = state.use_move(move)
            moves_made.append(reverse_set)
        result = bb_evaluate(state)
        # Undo all moves made during simulation
        for reverse_set in reversed(moves_made):
            state.unmove(reverse_set)
        return result

    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            if node.game_state.color == Color.RED:
                node.value = np.int64(node.value) + np.int64(result)
            else:
                node.value = np.int64(node.value) - np.int64(result)
            if node.parent:
                node.game_state.unmove(node.reverse_set)
            node = node.parent

    def get_best_move(self):
        if self.root.game_state.color == Color.RED:
            return max(self.root.children, key=lambda c: c.value / c.visits).move
        else:
            return min(self.root.children, key=lambda c: c.value / c.visits).move