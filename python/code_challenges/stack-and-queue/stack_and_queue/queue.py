from inspect import currentframe
from stack_and_queue.node import Node
#from node import Node

class EmptyQueueException(Exception):
    """
    An exception representing a queue is empty.

    Args:
        Exception (class): The Exception class.
    """
    pass

class Queue():
    """
    A class representing a stack.
    """
    def __init__(self):
        """
        The constructor method for the class Queue. Initialize front and rear.
        """
        self.front = None
        self.rear = None
    def __str__(self):
        """
        Return a string representation for a queue.

        Returns:
            str: A string representation for a queue.
        """
        representation = "| "
        if not self.front:
            representation += 'Empty queue.'
        else:
            current = self.front
            while current:
                representation += f"Value: {current.value} | "
                current = current.next
            representation += "\n| "
            current = self.front
            while current:
                representation += f"Next: {current.next}  | "
                current = current.next
            return representation

    def enqueue(self, value):
        """
        Push/ enqueue nodes to the back of a queue.

        Args:
            value (any): A node's value
        """
        node = Node(value)
        node.next = None
        if not self.front:
            self.front = node
            self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        """
        Remove/ dequeue a node from the front of a queue.

        Raises:
            EmptyQueueException: If queue is empty.

        Returns:
            any: The value of the node dequeued.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty, can't dequeue.")
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        """
        Return the value of the front node.

        Raises:
            EmptyQueueException: If the queue is empty.

        Returns:
            any: The value of the front node.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty, can't peek.")
        return self.front.value

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return not self.front

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    # print(queue.dequeue())
    # print(queue.is_empty())
    # print(queue.peek())
