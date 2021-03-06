from stack_queue_brackets.node import Node


class EmptyStackException(Exception):
    """
    An exception representing a stack is empty.

    Args:
        Exception (class): The Exception class.
    """
    pass


class Stack():
    """
    A class representing a stack.
    """

    def __init__(self):
        """
        The constructor method for the class Stack. Initialize top.
        """
        self.top = None

    def __str__(self):
        """
        Return a string representation for a stack.

        Returns:
            str: A string representation for a stack.
        """
        representation = 'Empty stack.' if self.is_empty() else '________________'
        current = self.top
        while current:
            representation += f"\n\nValue: {current.value}\nNext: {str(current.next)}\n________________"
            current = current.next
        return representation

    def push(self, value):
        """
        Push nodes onto the stack.

        Args:
            value (any): A node's value
        """
        node = Node(value)
        if not self.top:
            node.next = None
            self.top = node
            return
        node.next = self.top
        self.top = node
        """
        This part of the method checks if two added brackets even out and then removes them.
        """
        try:
            if self.top.next.value + self.top.value in ['[]', '()', '{}']:
                self.pop()
                self.pop()
        except:
            pass

    def pop(self):
        """
        Pop a node from the top of a stack.

        Raises:
            EmptyStackException: If stack is empty.

        Returns:
            any: The value of the node popped.
        """
        if self.is_empty():
            raise EmptyStackException("Stack is empty, can't pop.")
        temp = self.top
        self.top = temp.next
        temp.next = None
        return temp.value

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise.
        """
        return not self.top

    def peek(self):
        """
        Return the value of the uppermost/ top node.

        Raises:
            EmptyStackException: If the stack is empty.

        Returns:
            any: The value of the top node.
        """
        if self.is_empty():
            raise EmptyStackException("Stack is empty, can't peek.")
        return self.top.value
