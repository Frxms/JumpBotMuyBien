import copy
from typing import Any, List

from util.Bitboard.bb_evaluate import bb_evaluate
from util.Tree import Node, rec_endgame, Tree
from util.engine import calcMove, refactor_to_readable
from util.evaluate import evaluate
from util.generator import generateBoard
from util.move_ordering import organize_moves_quiet

global_count = 0
global_count_minimax = 0


def alpha_beta(node, depth, alpha, beta, maximizing_player):
    global global_count
    if depth == 0:  #&& isGameOver(node):
        node.eval = evaluate(node.value)
        #quiescenceSearch
        global_count += 1
        return node.eval

    if len(node.children) == 0:
        node.eval = evaluate(node.value)
        global_count += 1
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        global_count += 1
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, alpha_beta(child, depth - 1, max_eval, beta, False))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        global_count += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, alpha_beta(child, depth - 1, alpha, min_eval, True))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval


def quiescenceSearch(alpha, beta, depth, node):
    pat = bb_evaluate(node.value)
    #fail hard
    if (pat >= beta):
        return beta

    #fail soft
    if (alpha < pat):
        alpha = pat

    # generate all capture Moves
    allCaptureMoves = organize_moves_quiet(node.value)

    for move in allCaptureMoves:
        new_board = copy.deepcopy(node.value)
        new_board.use_move(move)
        score = quiescenceSearch(-alpha, -beta, depth-1,  Node(new_board))

        if score >= beta:
            return beta
        if score > alpha:
            alpha = score

    return alpha


def bb_alpha_beta(node, depth, alpha, beta, maximizing_player):
    global global_count
    if depth == 0:
        node.eval = bb_evaluate(node.value)
        global_count += 1
        return node.eval

    if len(node.children) == 0:
        node.eval = bb_evaluate(node.value)
        global_count += 1
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        global_count += 1
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, bb_alpha_beta(child, depth - 1, max_eval, beta, False))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        global_count += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, bb_alpha_beta(child, depth - 1, alpha, min_eval, True))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval


def alpha_beta_quiet(node, depth, alpha, beta, maximizing_player):
    global global_count
    if depth == 0:
        node.eval = quiescenceSearch(alpha, beta, 3, node)
        global_count += 1
        return node.eval

    if len(node.children) == 0:
        node.eval = bb_evaluate(node.value)
        global_count += 1
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        global_count += 1
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, alpha_beta_quiet(child, depth - 1, max_eval, beta, False))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        global_count += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, alpha_beta_quiet(child, depth - 1, alpha, min_eval, True))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval

def alphaBeta_windows(node, depth, alpha, beta, maximizing_player, window):
    global global_count
    if depth == 0:
        node.eval = quiescenceSearch(alpha, beta, node)
        global_count += 1
        return node.eval

    if len(node.children) == 0:
        node.eval = bb_evaluate(node.value)
        global_count += 1
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        global_count += 1
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, alphaBeta_windows(child, depth - 1, max_eval, beta - window, False, window))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        global_count += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, alphaBeta_windows(child, depth - 1, alpha + window, min_eval, True, window))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval


def minimax(node: Node, depth: int, maximizing_player: bool):
    global global_count_minimax
    if depth == 0:  #&& isGameOver(node):
        global_count_minimax += 1
        node.eval = evaluate(node.value)
        return node.eval

    if len(node.children) == 0:
        global_count_minimax += 1
        node.eval = evaluate(node.value)
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        global_count_minimax += 1
        max_eval = -100000
        for child in node.children:
            max_eval = max(max_eval, minimax(child, depth - 1, False))
        node.eval = max_eval
        return max_eval

    else:
        global_count_minimax += 1
        min_eval = 100000
        for child in node.children:
            min_eval = min(min_eval, minimax(child, depth - 1, True))
        node.eval = min_eval
        return min_eval

def printGlobal(p=True):
    if p:
        print("minimax:")
        print(global_count_minimax)
        print("alphabeta:")
        print(global_count)
    return global_count


def clear_global():
    global global_count
    global global_count_minimax
    global_count = 0
    global_count_minimax = 0


if __name__ == '__main__':
    a = [['X', '', '', '', '', '', '', 'X'], ['b', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''], ['X', '', '', '', '', '', '', 'X']]
    fen = "1r0r02r0/2r02r02/8/1bb4r01/3brb03/1b03r02/4b03/b01b03"
    print(rec_endgame(a))
