class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=none):
        # initialization here
        self.head = head

    def insert(self, value):
        new_node =Node(value, self.head)
        self.head = new_node

    def includes(self, value):
        current = self.head
        does_include = False
        while current:
            if current.value == value:
                does_include = True
            current = current.next
        return does_include

    def to_string(self):
        current = self.head
        string = ""
        while current:
            string += "{" + str(current.value) + "} -> "
            current = current.next
        string += "NULL"
        return s

    def __str__(self):
        current = self.head
        string = ""
        while current:
            string += "{ " + str(current.value) + "} -> "
            current = current.next
        string += "NULL"
        return string


    class Node:

        def __init__(self, value, next=None):
            self.value = valueself.next = next

