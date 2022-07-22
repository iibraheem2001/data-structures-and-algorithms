# stacks and queues

- for enqueue we'll need to target the top of the stack

and look at it using peek. then we'll need to traverese

and move nodes into a temporary stack using pop

 until there are  no more nodes in the original stack.

Once that happens then we'll insert the node we want

to enqueue and bring back the nodes in reverse order

using push

## Whiteboard Process

![screenshot](/python/stacks_queues/screenshot.jpg)

## Approach & Efficiency

- Find the length of the linked list
- traverse through list
- move values out of list into a new temporary list usuing pop
- repeat until original list is empty
- enqueue value at the front of empty list
- return values in reverse order usuing push
