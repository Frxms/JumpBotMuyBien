import random

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
        return node

    def expand(self, node):
        move = random.choice(node.untried_moves)
        new_state = node.game_state.make_move(move)
        return node.add_child(move, new_state)

    def simulate(self, node):
        state = node.game_state.clone()
        while not state.is_terminal():
            move = node.rollout_policy(state.get_legal_moves())
            state = state.make_move(move)

        return bb_evaluate(state) # Use your evaluate method

    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            node.value += result if node.game_state.color == Color.RED else -result
            node = node.parent

    def get_best_move(self):
        if self.root.game_state.color == Color.RED:
            return max(self.root.children, key=lambda c: c.value / c.visits).move
        else:
            return min(self.root.children, key=lambda c: c.value / c.visits).move

