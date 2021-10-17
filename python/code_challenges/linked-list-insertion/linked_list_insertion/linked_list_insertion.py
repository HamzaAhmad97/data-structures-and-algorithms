class Node:
    """
    A class representing a node in a linked list

    Methods:
        __init__(value : any):
            the constructor method, takes a value argument
        __str__():
            return a string representation for the Node instance

    """

    def __init__(self, value=None):
        """
        The constructor function

        Args:
            value (any, optional): The value to be passes to the new node instance. Defaults to None.
        """
        self.value = value
        self.next_ = None

    def __str__(self):
        """
        Return a string representation of a node

        Returns:
            string: the value of a node as a string
        """
        return f"{self.value}"
