import sys

from util.tree_node import TreeNode


class Tree:
    root: TreeNode

    def __init__(self):
        self.root = None

    def find(self, item):
        return self.__find_by_node(self.root, item)

    def add(self, index, item):
        self.root = self.__add(self.root, index, item)

    def delete(self, index, item):
        self.root = self.__delete(self.root, index, item)

    def __delete(self, node: TreeNode, index, item):
        if node is None:
            return node

        if item < node.value:
            node.left = self.__delete(node.left, index, item)
        elif item > node.value:
            node.right = self.__delete(node.right, index, item)
        elif index != node.index:
            node.left = self.__delete(node.left, index, item)
            node.right = self.__delete(node.right, index, item)
        else:
            if node.left is None or node.right is None:
                tmp_node = None
                if tmp_node == node.left:
                    tmp_node = node.right
                else:
                    tmp_node = node.left

                if tmp_node is None:
                    tmp_node = node
                    node = None
                else:
                    node = tmp_node
            else:
                tmp_node = self.__min_value_node(node.right)
                TreeNode.copy_to(tmp_node, node)
                node.right = self.__delete(node.right, tmp_node.index, tmp_node.value)

        if node is None:
            return node

        node.height = max(self.__height(node.left), self.__height(node.right)) + 1

        balance = self.__balance(node)

        if balance > 1 and self.__balance(node) >= 0:
            return self.__right_rotate(node)

        if balance > 1 and self.__balance(node.left) < 0:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        if balance < -1 and self.__balance(node.right) <= 0:
            return self.__left_rotate(node)

        if balance < -1 and self.__balance(node.right) > 0:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        self.__ajust_min_index(node)

        return node

    def __min_value_node(self, node: TreeNode):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def __find_by_node(self, node: TreeNode, item):
        if node is None:
            return sys.maxsize
        if node.value < item:
            return self.__find_by_node(node.right, item)
        if node.value > item:
            right_min_index = sys.maxsize if node.right is None else node.right.min_index
            min_index = min(
                node.index,
                right_min_index
            )
            min_index = min(
                min_index,
                self.__find_by_node(node.left, item)
            )

            return min_index

        min_index = min(
            self.__find_by_node(node.left, item),
            self.__find_by_node(node.right, item)
        )

        return min(min_index, node.index)

    def __height(self, node: TreeNode):
        if node is None:
            return 0

        return node.height

    def __balance(self, node: TreeNode):
        if node is None:
            return 0
        return self.__height(node.left) - self.__height(node.right)

    def __left_rotate(self, node: TreeNode):
        y = node.right

        if y is None:
            return node

        x = y.left

        y.left = node
        node.right = x

        node.height = max(self.__height(node.left), self.__height(node.right)) + 1
        y.height = max(self.__height(y.left), self.__height(y.right)) + 1

        self.__ajust_min_index(node)
        self.__ajust_min_index(y)

        return y

    def __right_rotate(self, node: TreeNode):
        y = node.left

        if y is None:
            return node

        x = y.right

        y.right = node
        node.left = x

        node.height = max(self.__height(node.left), self.__height(node.right)) + 1
        y.height = max(self.__height(y.left), self.__height(y.right)) + 1

        self.__ajust_min_index(node)
        self.__ajust_min_index(y)

        return y

    def __add(self, node: TreeNode, index, item):
        if node is None:
            return TreeNode(item, index)

        if item <= node.value:
            node.left = self.__add(node.left, index, item)
        else:
            node.right = self.__add(node.right, index, item)

        node.height = 1 + min(
            self.__height(node.left),
            self.__height(node.right)
        )

        balance = self.__balance(node)

        if balance > 1 and item < node.left.value:
            return self.__right_rotate(node)

        if balance < -1 and item > node.right.value:
            return self.__left_rotate(node)

        if balance > 1 and item > node.left.value:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        if balance < -1 and item < node.right.value:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        self.__ajust_min_index(node)

        return node

    def __ajust_min_index(self, node: TreeNode):
        if node is None:
            return sys.maxsize

        min_index = node.index
        left_min_index = sys.maxsize if node.left is None else node.left.min_index
        right_min_index = sys.maxsize if node.right is None else node.right.min_index

        min_index = min(min_index, left_min_index)
        min_index = min(min_index, right_min_index)

        node.min_index = min_index

        return min_index
