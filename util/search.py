class Node:
    def __init__(self, key, score=None):
        self.children = []
        self.value = key
        self.score = score

    def __repr__(self):
        return f"Key: {self.value} Score: {self.score}"

    def add_child(self, node):
        self.children.append(node)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, score=None):
        if self.root is None:
            self.root = Node(key, score)
        else:
            self._insert(self.root, key, score)

    def _insert(self, root, key, score):
        if key < root.value:
            if root.left is None:
                root.left = Node(key, score)
            else:
                self._insert(root.left, key, score)
        else:
            if root.right is None:
                root.right = Node(key, score)
            else:
                self._insert(root.right, key, score)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def minimax(self, node, depth, alpha, beta, maximizing_player):
        if node is None:
            return 0  # In case the node is None, return 0

        if node.left is None and node.right is None:  # Leaf node
            return node.score

        if maximizing_player:
            max_eval = float('-inf')
            if node.left:
                eval_left = self.minimax(node.left, depth + 1, False)
                max_eval = max(max_eval, eval_left)
                alpha = max(alpha, eval_left)
            if node.right:
                eval_right = self.minimax(node.right, depth + 1, False)
                max_eval = max(max_eval, eval_right)
            node.score = max_eval
            return max_eval
        else:
            min_eval = float('inf')
            if node.left:
                eval_left = self.minimax(node.left, depth + 1, True)
                min_eval = min(min_eval, eval_left)
            if node.right:
                eval_right = self.minimax(node.right, depth + 1, True)
                min_eval = min(min_eval, eval_right)
            node.score = min_eval
            return min_eval


# def minimax(state, depth, is_maximizing_player):
#     if terminal_state(state):
#         return utility(state)
#
#     if is_maximizing_player:
#         max_eval = -infinity
#         for each child in children(state):
#             eval = minimax(child, depth - 1, False)
#             max_eval = max(max_eval, eval)
#         return max_eval
#     else:
#         min_eval = infinity
#         for each child in children(state):
#             eval = minimax(child, depth - 1, True)
#             min_eval = min(min_eval, eval)
#         return min_eval
#
# def rightNode(node):
#     return node.right
#
# def leftNode(node):
#     return node.left
#
# commands = [rightNode, leftNode]
#
# def isGameOver(pos): #temporary
#     return False
# def minimax(pos, depth, maximizing_player):
#     if depth == 0 or isGameOver(pos):
#         return pos
#     if maximizing_player:
#         max_eval = -float("inf")
#         for call in commands:
#             eval = minimax(call(pos), depth - 1, False)
#             max_eval = max(max_eval, eval)
#         return max_eval
#     else:
#         min_eval = float("inf")
#         for call in commands:
#             eval = minimax(call(pos), depth - 1, True)
#             min_eval = min(min_eval, eval)
#         return min_eval


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(10, None)
    tree.insert(5, None)
    tree.insert(20, None)
    tree.insert(3, 3)  # Leaf node with score 3
    tree.insert(7, 5)  # Leaf node with score 5
    tree.insert(15, 2)  # Leaf node with score 2
    tree.insert(25, 9)  # Leaf node with score 9

    print(tree.minimax(tree.root, 2, True))
