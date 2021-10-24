from stack_queue_pseudo.stack import Stack


class EmptyPseudoQueueException(Exception):
    """
    An exception that will get raised when dequeueing from an empty pseudo queue

    Args:
        Exception (Class): The Exception class
    """
    pass


class PseudoQueue:
    """
    A class representing a pseudo queue that does not implement any method or attribute from the original queue class.
    """

    def __init__(self):
        """
        The constructor method. Here we define two stack instances to handle the logic of enqueueing and dequeueing.
        """
        self.taker = Stack()
        self.giver = Stack()

    def enqueue(self, value):
        """
        Add/push a node given its value to the end of the pseudo queue.

        Args:
            value (any): The value of the node to be added/ pushed/ enqueued.
        """
        self.taker.push(value)
        self.migrate()

    def dequeue(self):
        """
        Get/ remove the first node added to the pseudo queue.

        Raises:
            EmptyPseudoQueueException: Gets raised when dequeueing from an empty pseudo queue.

        Returns:
            Any: The value of the first node in the pseudo queue.
        """

        if self.giver.is_empty():
            raise EmptyPseudoQueueException(
                "Pseudo queue is empty, can't dequeue.")

        popped = self.giver.pop()
        self.migrate(False)

        return popped

    def __str__(self):
        """
        Return a string representation of a pseudo queue.

        Returns:
            string: A representation of a pesudo queue as a string.
        """
        return str(self.giver)

    def migrate(self, enq=True):
        """
        Handle migrating data between taker and giver.

        Args:
            enq (bool, optional): Indicate if enqueueing or dequeueing. Defaults to True.
        """
        if enq:
            self.giver.top = None
            current = self.taker.top
            while current:
                self.giver.push(current.value)
                current = current.next
        else:
            self.taker.top = None
            current = self.giver.top
            while current:
                self.taker.push(current.value)
                current = current.next

if __name__ == "__main__":
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.dequeue()
    pseudo.dequeue()
    # pseudo.enqueue(4)
    print(pseudo)
    pseudo.enqueue(4)
    print("*****************")
    print(pseudo)
    pseudo.dequeue()
    print("*****************")
    print(pseudo)
