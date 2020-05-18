
class TreeNode:
    value: float

    def __init__(self, value, index):
        self.left = None
        self.right = None
        self.value = value
        self.index = index
        self.min_index = index
        self.height = 1

    @staticmethod
    def copy_to(node_from, node_to):
        if node_to is None or node_to is None:
            return
        node_to.value = node_from.value
        node_to.index = node_from.index

