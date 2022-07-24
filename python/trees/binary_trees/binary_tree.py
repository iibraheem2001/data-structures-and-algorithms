class BinaryTree:

    def __init__(self, root=None):
        self.root = root
        self.max_val = self.root

    def pre_order(self, data=[]):
        def traverse(node):
            if not node:
                return
            data.append(node.value)
            traverse(node.right)
            traverse(node.left)
        traverse(self.root)
        return data
    def in_order(self):

        def traverse(root):
            if not root:
                return
            traverse(root.right)
            values.append(root.value)
            traverse(root.left)
        values = []
        traverse(self.root)
        return values


    def traverse(root):

            if not root:
                return

            traverse(root.right)
            traverse(root.left)
            values.append(root.value)
            values = []
            traverse(self.root)

            return values

    def find_maximum_value(self):
        def traverse(node):
            if not node:
                return self.max_val.value
            else:
                traverse(node.right)
                if self.max_val.value < node.value:
                    self.max_val = node
                return traverse(node.left)
        self.max_val = self.root
        return traverse(self.root)

class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

        return f"Node{self.root.value}"