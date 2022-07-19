from data_structures import kary_tree


def fizz_buzz_tree(tree):
    new_tree = kary_tree()
    if not tree.root:
        return new_tree

    queue = queue()

    queue.enqueue(root)

    while not queue.is_empty():
        node = queue.dequeue()
        if root.child % 15 == 0:
            return "FizzBuzz"
        elif root.child % 3 == 0:
            return "Fizz"
        elif root.child % 5 == 0:
            return "Buzz"
        else:
            return str(root.child)
        for child in node.children:
            queue.enqueue(child)

        return new_tree

    current = tree.root
    pass
