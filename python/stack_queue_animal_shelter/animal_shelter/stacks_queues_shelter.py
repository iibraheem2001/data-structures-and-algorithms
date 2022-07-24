from animal_shelter.node import Node
from animal_shelter.invalid_operation import InvalidOperationError


class AnimalShelter():

    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, val):
        node = Node(val)
        front = self.rear
        front = self.front
        if rear is None:
            return
        front.next_node = node
        self.front = node

    def dequeue(self, pref):
        if self.rear is None:
            return
        while self.rear:
                return self.rear.value

    def is_empty(self):
        if not self.rear:
            return True

def Dog():
    return 'dog'

def Cat():
    return'cat'