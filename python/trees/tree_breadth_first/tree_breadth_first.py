from tree_breadth_first import BinaryTree
from tree_breadth_first import Queue


def breadth_first(tree):

    queue_ = Queue()
    output = []

    if tree.root is None:
        return output

    queue_.enqueue(tree.root)

    while not queue_():

        tree.root = queue_.dequeue()

        output.append(tree.value)

        if tree.root.left is not None:

         queue_.enqueue(tree.left)

        if tree.root.right is not None:

            queue_.enqueue(tree.right)

    return output