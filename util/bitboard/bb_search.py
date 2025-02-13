import copy

from util.bitboard.bb_evaluate import bb_evaluate
from util.bitboard.bb_tree import Node
from util.move_ordering import organize_moves_quiet#
from treelib import Tree as Other_Tree, Node as Other_Node


count_bb_alpha_beta = 0
count_bb_quiet = 0


def bb_alpha_beta(node: Node, depth, alpha, beta, maximizing_player):
    global count_bb_alpha_beta
    if depth == 0:
        node.eval = bb_evaluate(node.value)
        count_bb_alpha_beta += 1
        return node.eval

    if len(node.children) == 0:
        node.eval = bb_evaluate(node.value)
        count_bb_alpha_beta += 1
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        count_bb_alpha_beta += 1
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, bb_alpha_beta(child, depth - 1, max_eval, beta, False))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        count_bb_alpha_beta += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, bb_alpha_beta(child, depth - 1, alpha, min_eval, True))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval


def alpha_beta_quiet(node, depth, alpha, beta, maximizing_player):
    global count_bb_quiet
    if depth == 0:
        node.eval = quiescenceSearch(alpha, beta, 3, node)
        count_bb_quiet += 1
        return node.eval

    if len(node.children) == 0:
        node.eval = bb_evaluate(node.value)
        count_bb_quiet += 1
        return node.eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        count_bb_quiet += 1
        max_eval = alpha
        for child in node.children:
            max_eval = max(max_eval, alpha_beta_quiet(child, depth - 1, max_eval, beta, False))
            if max_eval >= beta:
                break
        node.eval = max_eval
        return max_eval

    else:
        count_bb_quiet += 1
        min_eval = beta
        for child in node.children:
            min_eval = min(min_eval, alpha_beta_quiet(child, depth - 1, alpha, min_eval, True))
            if min_eval <= alpha:
                break
        node.eval = min_eval
        return min_eval


def quiescenceSearch(alpha, beta, max_depth, node, depth = 0):
    if max_depth <= depth:
        bb_evaluate(node.value)

    stand_pat = bb_evaluate(node.value)
    #fail hard
    if (stand_pat >= beta):
        return beta
    #fail soft
    if (alpha < stand_pat):
        alpha = stand_pat

    # generate all capture Moves
    allCaptureMoves = organize_moves_quiet(node.value)

    for move in allCaptureMoves:
        new_board = copy.deepcopy(node.value)
        new_board.use_move(move)
        score = -quiescenceSearch(-alpha, -beta, max_depth,  Node(new_board), depth+1)

        if score >= beta:
            return beta
        if score > alpha:
            alpha = score

    return alpha


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


count_bb_other_tree = 0


def bb_ab_other_tree(node: Other_Node, depth, alpha, beta, maximizing_player, tree:Other_Tree):
    global count_bb_other_tree
    if depth == 0:
        eval = bb_evaluate(node.data[0])
        node.data = node.data, eval
        count_bb_other_tree += 1
        return eval

    if len(tree.children(node.identifier)) == 0:
        eval = bb_evaluate(node.data[0])
        node.data = node.data, eval
        count_bb_other_tree += 1
        return eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        count_bb_other_tree += 1
        max_eval = alpha
        for child in tree.children(node.identifier):
            max_eval = max(max_eval, bb_ab_other_tree(child, depth - 1, max_eval, beta, False, tree))
            if max_eval >= beta:
                break
        node.data = node.data, max_eval
        return max_eval

    else:
        count_bb_other_tree += 1
        min_eval = beta
        for child in tree.children(node.identifier):
            min_eval = min(min_eval, bb_ab_other_tree(child, depth - 1, alpha, min_eval, True, tree))
            if min_eval <= alpha:
                break
        node.data = node.data, min_eval
        return min_eval

def bb_ab_other_tree_quiet(node: Other_Node, depth, alpha, beta, maximizing_player, tree:Other_Tree):
    global count_bb_other_tree
    if depth == 0:
        eval = quiescenceSearch(alpha, beta, 4, node)
        node.data = node.data, eval
        count_bb_other_tree += 1
        return eval

    if len(tree.children(node.identifier)) == 0:
        eval = bb_evaluate(node.data[0])
        node.data = node.data, eval
        count_bb_other_tree += 1
        return eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        count_bb_other_tree += 1
        max_eval = alpha
        for child in tree.children(node.identifier):
            max_eval = max(max_eval, bb_ab_other_tree(child, depth - 1, max_eval, beta, False, tree))
            if max_eval >= beta:
                break
        node.data = node.data, max_eval
        return max_eval

    else:
        count_bb_other_tree += 1
        min_eval = beta
        for child in tree.children(node.identifier):
            min_eval = min(min_eval, bb_ab_other_tree(child, depth - 1, alpha, min_eval, True, tree))
            if min_eval <= alpha:
                break
        node.data = node.data, min_eval
        return min_eval


def bb_ab_other_tree_asp(node: Other_Node, depth, alpha, beta, maximizing_player, tree:Other_Tree, window):
    global count_bb_other_tree
    if depth == 0:
        eval = bb_evaluate(node.data[0])
        node.data = node.data, eval
        count_bb_other_tree += 1
        return eval

    if len(tree.children(node.identifier)) == 0:
        eval = bb_evaluate(node.data[0])
        node.data = node.data, eval
        count_bb_other_tree += 1
        return eval

    if node is None:
        return 0  # In case the node is None, return 0

    if maximizing_player:
        count_bb_other_tree += 1
        max_eval = alpha
        for child in tree.children(node.identifier):
            max_eval = max(max_eval, bb_ab_other_tree_asp(child, depth - 1, max_eval, beta - window, False, tree, window))
            if max_eval >= beta:
                break
        node.data = node.data, max_eval
        return max_eval

    else:
        count_bb_other_tree += 1
        min_eval = beta
        for child in tree.children(node.identifier):
            min_eval = min(min_eval, bb_ab_other_tree_asp(child, depth - 1, alpha + window, min_eval, True, tree, window))
            if min_eval <= alpha:
                break
        node.data = node.data, min_eval
        return min_eval

def bb_alpha_beta_count():
    print("Status count:")
    print(count_bb_alpha_beta)


def bb_quiet_count():
    print("Status count:")
    print(count_bb_quiet)


def bb_other_tree_count():
    print("Status count:")
    print(count_bb_other_tree)
