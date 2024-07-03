import copy

from util.bitboard.bb_evaluate import bb_evaluate
from util.twod_array.tree import Node, rec_endgame
from util.twod_array.evaluate import evaluate
from util.move_ordering import organize_moves_quiet

count_alpha_beta = 0
count_minimax = 0


def alpha_beta(node, depth, alpha, beta, maximizing_player):
    global count_alpha_beta
    if depth == 0:  #&& isGameOver(node):
        node.eval = evaluate(node.value)
        #quiescenceSearch
        count_alpha_beta += 1
        return node.eval

    if len(node.children) == 0:
        node.eval = evaluate(node.value)
        count_alpha_beta += 1
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        count_alpha_beta += 1
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, alpha_beta(child, depth - 1, max_eval, beta, False))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        count_alpha_beta += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, alpha_beta(child, depth - 1, alpha, min_eval, True))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval


def minimax(node: Node, depth: int, maximizing_player: bool):
    global count_minimax
    if depth == 0:  #&& isGameOver(node):
        count_minimax += 1
        node.eval = evaluate(node.value)
        return node.eval

    if len(node.children) == 0:
        count_minimax += 1
        node.eval = evaluate(node.value)
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        count_minimax += 1
        max_eval = -100000
        for child in node.children:
            max_eval = max(max_eval, minimax(child, depth - 1, False))
        node.eval = max_eval
        return max_eval

    else:
        count_minimax += 1
        min_eval = 100000
        for child in node.children:
            min_eval = min(min_eval, minimax(child, depth - 1, True))
        node.eval = min_eval
        return min_eval

def minimax_count():
    print("Status count:")
    print(count_minimax)


def alpha_beta_count():
    print("Status count:")
    print(count_alpha_beta)


def print_global(p=True):
    if p:
        print("minimax:")
        print(count_minimax)
        print("alphabeta:")
        print(count_alpha_beta)
    return count_alpha_beta


def clear_global():
    global count_alpha_beta
    global count_minimax
    count_alpha_beta = 0
    count_minimax = 0


if __name__ == '__main__':
    a = [['X', '', '', '', '', '', '', 'X'], ['b', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''], ['X', '', '', '', '', '', '', 'X']]
    fen = "1r0r02r0/2r02r02/8/1bb4r01/3brb03/1b03r02/4b03/b01b03"
    print(rec_endgame(a))
