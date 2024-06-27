import copy
from typing import Any, List

from util.Bitboard.bb_evaluate import bb_evaluate
from util.Tree import Node, rec_endgame, Tree
from util.engine import calcMove, refactor_to_readable
from util.evaluate import evaluate
from util.generator import generateBoard
from util.move_ordering import organize_moves_by_importance, organize_moves_quiet

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


def quiescenceSearch(alpha, beta, node):
    pat = evaluate(node.value)
    #fail hard
    if (pat >= beta):
        return beta

    #fail soft
    if (alpha < pat):
        alpha = pat

    # generate all capture Moves

    for move in allCaptureMoves:
        score = quiescenceSearch(-beta, -alpha, child)
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score

    return alpha


def bb_alpha_beta(node, depth, alpha, beta, maximizing_player):
    global global_count
    if depth == 0:
        node.eval = bb_evaluate(node.value)
        #quiescenceSearch
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



def alphaBeta_windows(node, depth, alpha, beta, maximizing_player, window):
    global global_count
    if depth == 0:  #&& isGameOver(node):
        node.eval = evaluate(node.value)

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
            max_eval = max(max_eval,
                           alphaBeta_windows(child, depth - 1, max_eval, beta - window, False, window))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        global_count += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval,
                           alphaBeta_windows(child, depth - 1, alpha + window, min_eval, True, window))
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


def createTree(parent: Node, depth: int, turn: str, tree: Tree) -> Any:
    if depth == 0:
        return
    pboard = parent.value
    if recEndgame(pboard):
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
        createTree(child, depth, turn, tree)


def recEndgame(board: List):
    if "r" in board[7] or "b" in board[0]:
        return False
    if not (any('r' in cell or 'rr' in cell for row in board for cell in row) and any(
            'b' in cell or 'bb' in cell for row in board for cell in row)):
        return False
    #     pass
    return True


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
