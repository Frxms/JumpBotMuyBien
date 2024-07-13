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
        self.player = game_state.color

    def add_child(self, move, game_state):
        child = MCTSNode(game_state, self, move)
        self.untried_moves.remove(move)
        self.children.append(child)
        return child

    def update(self, result):
        self.visits += 1
        self.value += result

    def fully_expanded(self):
        return len(self.untried_moves) == 0

    def best_child(self, c_param=1.4):
        choices_weights = [
            (c.value / c.visits) + c_param * math.sqrt((2 * math.log(self.visits) / c.visits))
            if c.visits > 0 else float('inf')
            for c in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

    def rollout_policy(self, possible_moves):
        # Prioritize moves that advance pieces towards the end zone
        advancing_moves = [m for m in possible_moves if self.game_state.distance_to_end_zone(self.player) > self.game_state.make_move(m).distance_to_end_zone(self.player)]
        if advancing_moves:
            return random.choice(advancing_moves)
        return random.choice(possible_moves)


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
        current_player = node.player
        while not state.is_terminal():
            moves = state.get_legal_moves()
            if moves:
                # Prioritize moves that advance pieces towards the end zone
                advancing_moves = [m for m in moves if
                                   state.distance_to_end_zone(current_player) > state.make_move(m).distance_to_end_zone(
                                       current_player)]
                if advancing_moves:
                    move = random.choice(advancing_moves)
                else:
                    move = random.choice(moves)
                state = state.make_move(move)
            current_player = Color.RED if current_player == Color.BLUE else Color.BLUE
        return (evaluate_position(state, node.player) + 1000) / 2000

    def backpropagate(self, node, result):
        while node is not None:
            node.update(result)
            result = 1 - result  # Flip the result for the opponent
            node = node.parent

    def get_best_move(self):
        return max(self.root.children, key=lambda c: c.visits).move


def evaluate_position(board, player):
    opponent = Color.RED if player == Color.BLUE else Color.BLUE
    player_end_zone = board.pieces_in_end_zone(player)
    opponent_end_zone = board.pieces_in_end_zone(opponent)
    player_distance = board.distance_to_end_zone(player)
    opponent_distance = board.distance_to_end_zone(opponent)

    # Heavily reward reaching the end zone
    if player_end_zone > 0:
        return 1000 + player_end_zone * 10
    if opponent_end_zone > 0:
        return -1000 - opponent_end_zone * 10

    # Reward advancing towards the end zone
    score = (7 - player_distance) * 10 - (7 - opponent_distance) * 10

    # Small reward for having more pieces (as a tiebreaker)
    score += (bin(board.each_side[player]).count('1') - bin(board.each_side[opponent]).count('1'))

    return score
