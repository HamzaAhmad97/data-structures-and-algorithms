class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.next = None

    def __str__(self):
        return f"Value: {self.value}"
