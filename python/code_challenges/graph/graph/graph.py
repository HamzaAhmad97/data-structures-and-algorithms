from collections import deque


class Vertex:
    """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """
    def __init__(self, value):
        """
    Initalization for a Vertex to hold a value.
    
    """
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendLeft(value)

    def dequeue(self):
        self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
		Store the passed value in a node and then push the node on top of the stack.
		
		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
        self.dq.append(value)

    def pop(self):
        """
		Return the top node in a stack.
		"""
        self.dq.pop()


