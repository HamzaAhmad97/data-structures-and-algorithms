# Stacks and Queues

Stacks and queues are types of sequencial data structures. They contain nodes that hold a reference to each other but only in one direction. Each node in a stack or a queue holds a value and a reference to the next node via the next property. The difference between stacks and queues is that in stacks, the last node to be pushed will be the first to be popped LIFO, and the first node added will be the last to popped FILO. While, in queues, the first node added to the queue will be the first to be dequeued or removed FIFO, and the last node enqueued or added to the queue will be the last to be dequeued or removed LILO.

## [Latest Open Pull Request](https://github.com/HamzaAhmad97/data-structures-and-algorithms/pull/27)

## Challenge

The challenge requires defining classes representing a stack, a queue and a node, as well as implementing their attributes and methods like push(), pop(), is_empty(), and peek() for a stack, and a enqueue(), dequeue(), is_empty(), and peek() for a queue. A node does not have any methods on its own, just the attributes value and next. It is also requried to add all necessary tests to check the functionality and all these test should pass.

## Approach & Efficiency

For all of the methods related to adding and removing nodes from both a stack and a queue, the approach does not include defining any new data types other than a stack, a queue or a node. And these methods do not rely on the size of the data structure, so thier space and time effeciencies are O(1), except for the `__str__` methods, which have big O complexities of O(N) in terms of time and space since they iteratoe over all the nodes in a stack or a queue and create a string representation for them.

## API

1. Stack

    - `__str__()`: Return a string representation for a stack.
    - `push(value)`: Push nodes onto the stack.
    - `pop()`: Pop a node from the top of a stack.
    - `is_empty()`: Check if the stack is empty.
    - `peek()`: Return the value of the uppermost/ top node.

2. Queue

    - `__str__()`: Return a string representation for a queue.
    - `enqueue(value)`: Push/ enqueue nodes to the back of a queue.
    - `dequeue()`: Remove/ dequeue a node from the front of a queue.
    - `is_empty()`: Check if the queue is empty.
    - `peek()`: Return the value of the front node.

```python
    queue = Queue()
    queue.enqueue(1)
    print(queue) # value: 1 next: Null
    print(queue.dequeue()) # 1
    print(queue.is_empty()) # True
    print(queue.peek()) # EmptyStackException

    stack = Stack()
    stack.push(1)
    print(stack) # Value: 1 next: Null
    print(stack.pop()) # 1
    print(stack.is_empty()) # True
    print(stack.peek()) # EmptyQueueException
```
