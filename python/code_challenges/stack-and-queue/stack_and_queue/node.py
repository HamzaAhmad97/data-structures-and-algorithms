class Node:
    """
    A class representing a node.
    """
    def __init__(self, value = None):
        """
        The constructor method for the Node class. Initialize value and next.

        Args:
            value (any, optional): Node's value. Defaults to None.
        """
        self.value = value
        self.next = None
    def __str__(self):
        """
        Return a string representation of the node.

        Returns:
            str: A string representation for the node.
        """
        return str(self.value)
