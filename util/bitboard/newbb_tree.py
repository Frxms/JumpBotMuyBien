import copy

from treelib import Node, Tree

from util.bitboard.moves import gen_moves
from util.move_ordering import organize_moves_by_importance

global_count = 0


def create_other_bb_tree(tree: Tree, parent: Node, depth: int):
    global global_count
    if depth == 0:
        return
    if parent.identifier == tree.root:
        pboard = parent.data
    else:
        pboard = parent.data[0]
    if not pboard.is_endgame():
        moves = gen_moves(pboard, True)
        if not moves:
            return
    else:
        return

    moves = organize_moves_by_importance(moves, pboard.color)

    for moveset in moves:
        global_count += 1
        board_copy = copy.deepcopy(pboard)
        board_copy.use_move(moveset)
        board_copy.change_col()
        move = moveset[1], moveset[2]
        data_set = board_copy, move
        tree.create_node(global_count, global_count, parent=parent.identifier, data=data_set)

    depth -= 1
    for child in tree.children(parent.identifier):
        parent = tree.get_node(child.identifier)
        create_other_bb_tree(tree, parent, depth)


def get_eval_move(tree: Tree, eval_num):
    moves = []
    for node in tree.children(tree.root):
        if node.data[len(node.data)-1] == eval_num:
            moves.append(node.identifier)
    return moves


def get_eval_one_move(tree: Tree, eval_num):
    for node in tree.children(tree.root):
        if node.data[len(node.data) - 1] == eval_num:
            return node.identifier
