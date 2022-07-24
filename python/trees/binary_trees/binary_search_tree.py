from binary_tree import BinaryTree
from binary_tree import Node


class BinarySearchTree(BinaryTree):

    def __init__(self, root):
        self.root = None

    def add(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

    def contained(self, root, value):

        if self.root is None:
            return False

        def verify(value):

            if self.root.value < value:
                self.root = self.root.right

            if self.root.value > value:
                self.root = self.root.left

        verify(value, root)

        if self.root.value == value:
            return True
