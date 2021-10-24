# Challenge Summary

This challenge requires defining a pseudo queue class that has two methods, enqueue and dequeue, and any instance of this class should have the functionality of a normal queue but without utilizing any of the original methods or attributes in the normal queue class.

## [Latest open pull request](https://github.com/HamzaAhmad97/data-structures-and-algorithms/pull/28)

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency

In the constructor method,two stack instances get created, and for the enqueue method, the value passed gets pushed to the taker instance, and after that, the same nodes in the taker stack get pushed to the giver stack, which means that they will be in a reversed order. In the dequeue method, the top node gets popped out of the giver stack, then all the left nodes in the giver stack will be pushed again to the taker stack to maintain nodes and so on.

Both methods only iterate over one of the stacks defined for migration purposes, and they do not create any new data, so big O in terms of time is O(N), and O(1) in terms of space.

## Solution

```python
pseudo = PseudoQueue()
pseudo.enqueue(1) # value: 1, next: Null
pseudo.dequeue() # empty queue
```
