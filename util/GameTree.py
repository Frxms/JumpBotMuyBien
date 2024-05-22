class GameTreeNode:
    def __init__(self, state, parent=None, children=None):
        self.state = state
        self.parent = parent
        self.children = children if children is not None else []
        self.value = None  # To store the minimax value

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

