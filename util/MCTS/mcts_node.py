import math
import random

from util.bitboard.constants import Color


class MCTSNode:
    def __init__(self, game_state, parent=None, move=None):
        self.game_state = game_state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.value = 0
        self.untried_moves = game_state.get_legal_moves()

    def add_child(self, move, game_state):
        child = MCTSNode(game_state, self, move)
        self.untried_moves.remove(move)
        self.children.append(child)
        return child

    def fully_expanded(self):
        return len(self.untried_moves) == 0

    def best_child(self, c_param=1.4):
        choices_weights = [
            (c.value / c.visits) + c_param * ((2 * math.log(self.visits) / c.visits) ** 0.5)
            if c.visits > 0 else float('inf')
            for c in self.children
        ]
        if self.game_state.color == Color.RED:
            return self.children[choices_weights.index(max(choices_weights))]
        else:
            return self.children[choices_weights.index(min(choices_weights))]

    def rollout_policy(self, possible_moves):
        return random.choice(possible_moves)