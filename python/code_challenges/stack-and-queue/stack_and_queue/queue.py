from inspect import currentframe
from stack_and_queue.node import Node
#from node import Node

class EmptyQueueException(Exception):
    pass

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    def __str__(self):
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
        node = Node(value)
        node.next = None
        if not self.front:
            self.front = node
            self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty, can't dequeue.")
        temp = self.front
        self.front = temp.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty, can't peek.")
        return self.front.value

    def is_empty(self):
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
