# linked list insertion

Write the following methods for the Linked List class:

append
arguments: new value
adds a new node with the given value to the end of the list
insert before
arguments: value, new value
adds a new node with the given new value immediately before the first node that has the value specified
insert after
arguments: value, new value
adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process

![screenshot](/python/linked-list-insertions/screenshot-6.jpg)

## Approach & Efficiency

### append:

- Make a new node "new" with the value thats been passed. Traverse the list, and find the last node. Change the .next value of the last node to the new node.

### Insert before:

- Create a new node "new" using the input value. Assign "prev" to Head. traverse the list as normal, but every step, right before traversing to the next node, save the current node to "prev". when a node is found with the target value, set prev.next to new, and set new.next to the node with the target value.  

### insert after:

- Create a new node "new" using the input value. traverse the list, until a node is found with the target value, "targetnode". set new.next to targetnode.next, and then set targetnode.next to new.
