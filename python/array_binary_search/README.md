# array binary search

- Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process

![screenshot](/python/array_binary_search/screenshot.jpg)

## Approach & Efficiency

- Find the length of the array
- Find the mid point of the array
- find if the target value is to the left of right of the midpoint
- repeat unitl midpoint is the target value
- if the target value is not in the array. Return "-1"
