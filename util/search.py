class Node:
    def __init__(self, move):
        self.children = []
        self.value = move

    def __repr__(self):
        return f"Key: {self.value} Score: {self.score}, Children: {self.children}"

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

    def get_leafs(self):
        if self.root is None:
            return []
        return self.root.get_leafs()

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

    def minimax(self, node, depth, alpha, beta, maximizing_player):
        if depth == 0:  #&& isGameOver(node):
            return eval(node)

        if node is None:
            return 0  # In case the node is None, return 0

        if len(node.children) == 0:
            return node.score

        if maximizing_player:
            max_eval = alpha
            for child in node.children:
                max_eval = max(max_eval, self.minimax(child, depth - 1, max_eval, beta, False))
                if max_eval >= beta:
                    break
            return max_eval

        else:
            min_eval = beta
            for child in node.children:
                min_eval = min(min_eval, self.minimax(child, depth - 1, alpha, min_eval, True))
                if min_eval <= alpha:
                    break
            return min_eval


if __name__ == '__main__':
    tree = Tree()
