from typing import Counter


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
        self.index = 0

    def __str__(self):
        """
        Return a string representation of a node
        Returns:
            string: the value of a node as a string
        """
        return f"{self.value}"

class OutOfRangeException(Exception):
    pass

class EmptyLinkedListException(Exception):
    pass

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
        kth_from_end(k : int)
            Get the value of the node that is k steps from the tail
    """

    def __init__(self):
        """
        The constructor method for the linked list, initializes the head property to None and the tail to None
        """
        self.head = None
        self._tail = None

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

    def __str__(self):
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

    def delete_node(self, val):
        """
        Delete a node given its value
        Args:
            val (any): The value of the node to be removed
        """
        current  = self.head
        while True:
            if current == self.head and current.value == val:
                self.head = self.head.next_
                break
            elif current.next_.value == val:
                current.next_ = current.next_.next_
                break

    def kth_from_end(self, k):
        """
        A method that returns the value of the node that is k steps from the tail of the list
        Args:
            k (Integer): The index of the node to be returned starting from the tail
        Raises:
            OutOfRangeException: If k is negative or larger than the length of the list
        Returns:
            any: The value of the node that matches
        """
        current = self.head
        increment = 0
        while True:
            current.index += increment
            increment += 1

            if not current.next_:
                self._tail = current
                break
            current = current.next_
        if k > self._tail.index or k < 0:
            raise OutOfRangeException("Distance cannot be negative or exceeding the number of nodes in the list.")
        current = self.head
        while True:

            if current.index == abs(k - self._tail.index):
                return current.value
            current = current.next_


def zip_lists(j, k):
    """
    Returns a new linked list of zipping the two passed linked lists.

    Args:
        j (LinkedList): First linked list
        k (LinkedList): Second linked list

    Raises:
        EmptyLinkedListException: If either of the lists is empty

    Returns:
        LinkedList: A new linked list of zipping the two passed linked lists
    """
    if not (j.head and k.head):
        raise EmptyLinkedListException("One or both arguments are empty linked lists.")
    curj = j.head
    curk = k.head
    new = LinkedList()
    new.insert(curj.value)
    curj = curj.next_
    while True:

        if curk:
            new.append(curk)
            curk = curk.next_
        if curj:
            new.append(curj)
            curj = curj.next_

        if not (curk or curj):
            return new

def check_palindrome(ll):
    current = ll.head
    new = LinkedList()
    while current:
        new.insert(current.value)
        current = current.next_
    return str(new) == str(ll)

if __name__ == "__main__":
    ll = LinkedList()
 
    print(ll)
    print(check_palindrome(ll))

