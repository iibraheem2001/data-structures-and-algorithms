# Reverse an Array

Write a function called fizz buzz tree and determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original

## Whiteboard Process

![fizz_buzz_tree](/python/code_challenges/fizz_buzz/fizz_buzz.jpg)

## Approach & Efficiency

define a k-ary tree function with values
define a function as fizz_buzz_tree that returns a new tree with the value of each node that is  divisable by three as "fizz" and values divisable by 5 as "buzz" and values divisable by both as "fizz buzz" traverse through original tree using enqueue and dequeue
read the values of the nodes and determine what it is divisible by and enqueue into new tree
return new tree
