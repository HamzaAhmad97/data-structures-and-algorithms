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

class LinkedList:
    """
    A class representing a Linked List

    Methods:
        __init__():
            the constructor method, takes no arguments
        insert(value : any):
            creates a node and then inserts it to the linked list
        includes(value : any):
            returns True if a node exists in the list and its value equals the passed value
        to_string():
            return a string representation of the linked list
        append(val : any)
            Append a node to the end of a linked list.
        insert_before(val : any, new_val : any)
            Insert a node given its value before another node given its value.
        insert_after(val : any, new_val : any)
            Insert a node given its value after another node given its value.
    """
    def __init__(self):
        """
        The constructor method for the linked list, initializes the head property to None
        """
        self.head = None

    def insert(self, value):
        """
        Insert a node into the linked list

        Args:
            value (any): the value to be stored as the valur inside of the new node
        """
        new_node = Node()
        new_node.value = value
        new_node.next_ = self.head
        self.head = new_node

    def includes(self, value):
        """
        Check if the node with the given value exists in the linked list

        Args:
            value (any): the value to be checked

        Returns:
            Boolean: True if the a node exists and its value is equal to the passed value
        """

        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next_
        return False

    def to_string(self):
        """
        Return a string representation of the linked list

        Returns:
            string: a representation of the linked list
        """
        current = self.head
        representation = ""
        while current != None:
            representation += f"{{{current.value}}} -> "
            if current.next_ == None:
                representation += f"Null"
            current = current.next_
        return representation

    def append(self, val):
        """
        Append a node to the end of a linked list.

        Args:
            val (any): The value to be stored in a node
        """
        current = self.head
        while True:
            if not current.next_:
                new_node = Node()
                new_node.value = val
                new_node.next_ = None
                current.next_ = new_node
                break
            current = current.next_

    def insert_before(self, val, new_val):
        """
        Insert a node given its value before another node given its value.

        Args:
            val (any): The value of the node that the new node will be inserted before
            new_val (any): The value to be stored in the new node
        """
        current = self.head
        while True:
            if current.next_ == None and current == self.head and current.value == val:
                new_node = Node()
                new_node.value = new_val
                new_node.next_ = self.head
                self.head = new_node
                break
            elif current.next_.value == val:
                new_node = Node()
                new_node.value = new_val
                new_node.next_ = current.next_
                current.next_ = new_node
                break
            current = current.next_

    def insert_after(self, val, new_val):
        """
        Insert a node after another node given its value

        Args:
            val (any): The value of the node that the new node will be inserted after
            new_val (any): The value to be stored in the new node
        """
        current = self.head
        while True:
            if current.value == val:
                new_node = Node()
                new_node.value = new_val
                new_node.next_ = current.next_
                current.next_ = new_node
                break
            current = current.next_
