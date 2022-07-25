class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:


    def __init__(self, head=None):
        self.head = head


    def insert(self, value):
        node = Node(value)
        if self.head:
            node = self.head
        self.head = node 



    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return "value exists"
            current_node = current_node.next_node


    def __str__(self):
        str = ''
        if self.head is None:
            return 'NULL'
        else:
            str = ''
            current_node = self.head
            while current_node:
                if current_node.value == self.head.value:
                    str = '{ ' + self.head.value + ' } -> '
                else:
                    str = str + '{ ' + current_node.value + ' } -> '
                current_node = current_node.next_node

            return str + 'NULL'
