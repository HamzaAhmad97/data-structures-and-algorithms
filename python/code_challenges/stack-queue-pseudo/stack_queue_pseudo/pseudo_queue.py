from 
class EmptyPseudoQueueException(Exception):
    pass

class PseudoQueue:
    def __init__(self):
        self.taker = Stack()
        self.giver = Stack()
    def enqueue(self, value):
        self.taker.push(value)

        self.giver.top = None
        current = self.taker.top
        while current:
            self.giver.push(current.value)
            current = current.next

    def dequeue(self):
        if self.giver.is_empty():
            raise EmptyPseudoQueueException(
                "Pseudo queue is empty, can't dequeue.")

        return self.giver.pop()

    def __str__(self):
        return str(self.giver)
