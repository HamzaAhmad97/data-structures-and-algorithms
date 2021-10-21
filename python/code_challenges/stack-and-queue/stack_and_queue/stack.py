from stack_and_queue.node import Node
#from node import Node


class EmptyStackException(Exception):
    pass


class Stack():
    def __init__(self):
        self.top = None

    def __str__(self):
        representation = 'Empty stack.' if self.is_empty() else '________________'
        current = self.top
        while current:
            representation += f"\n\nValue: {current.value}\nNext: {str(current.next)}\n________________"
            current = current.next
        return representation

    def push(self, value):
        node = Node(value)
        if not self.top:
            node.next = None
            self.top = node
            return
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Stack is empty, can't pop.")
        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    def is_empty(self):
        return not self.top

    def peek(self):
        if self.is_empty():
            raise EmptyStackException("Stack is empty, can't peek.")
        return self.top.value


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.is_empty())
    print(stack.peek())
