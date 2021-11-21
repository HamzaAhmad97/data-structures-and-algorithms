"""
The implementation of Node class, Linked list class, InvalidNumberOfKeysError class, repeated_word function and Hashtable class. 
"""
import re
import os

class Node:
    """
    A data structure that stores a value, and references the next nodes.
    """
    def __init__(self, value, _next = None):
        """
        The constructor method for Node class, takes a value and a reference to the next node. Initializes value, and _next.

        Args:
            value (list): A list containing a key/value pair.
            _next (Node, optional): The next node to the current node. Defaults to None.
        """
        self.value = value
        self._next = _next
    def __str__(self):
        """
        Generate a string representation of a node instance.

        Returns:
            str: a representation of a node instance as a string.
        """

        return f"{self.value}"

class LinkedList:
    """
    A data structure that consists of nodes that reference each other.
    """
    def __init__(self):
        """
        The constructor method of a LinkedList instance which initializes the head property to None.
        """

        self.head = None
    def insert(self,value):
        """
        Insert a node given a value to be stored in the new node to be inserted.

        Args:
            value (any): The value to be stored in a node.
        """

        self.head = Node(value, self.head)
    def __str__(self):
        """
        Generate a string representation of a linked list instance.

        Returns:
            str: a string representation of a linked list instance.
        """

        current = self.head
        representation = ""
        while current != None:
            representation += f"{{{current}}} -> "
            if current._next == None:
                representation += f"Null"
            current = current._next
        return representation

class Hashtable:
    """
    A data structure that is used to store key/value pairs effeciently.
    """

    def __init__(self, size = 1024):
        """
        The constructor method of a Hashtable, takes size as an argument and initializes the __size property as well as the __buckets property to a list of size equals size.

        Args:
            size (int, optional): [description]. Defaults to 1024.
        """

        self.__size = size
        self.__buckets = [None for _ in range(size)]

    def __hash(self, key):
        """
        Generate a hashcode correponding to the key provided.

        Args:
            key (str): a string that we want to generate a hashcode for.

        Returns:
            int: the hashcode of a string key.
        """

        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        Add a key/value pair to a hashtable.

        Args:
            key (str): The key of a key/value pair.
            value (any): The value corresponding to the key provided.
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
            self.__buckets[index] = LinkedList()
        val = [key, value]
        self.__buckets[index].insert(val)

    def get(self, key):
        """
        Get the value corresponding to the key provided in the hashtable.

        Args:
            key (str): the key.

        Returns:
            any: the value stored corresponding to the key provided.
        """
        index = self.__hash(key)
        value = self.__buckets[index]
        if value:
            if isinstance(value, LinkedList):
                current = value.head
                while current:
                    if current.value[0] == key:
                        return current.value[1]
                    current = current._next
            return value
        return None
                
    def contains(self, key):
        """
        Check if a key/value pair is exists in a hashtable.

        Args:
            key (str): a key.

        Returns:
            bool: True if the key exists in the hashtable, and False otherwise.
        """

        index = self.__hash(key)
        value = self.__buckets[index]
        if value:
            if isinstance(value, LinkedList):
                current = value.head
                while current:
                    if current.value[0] == key:
                        return True
                    current = current._next
            return True
        return False

class InvalidNumberOfKeysError(Exception):
    """
    An exception that get raised if the number of words in the passed string is smaller than or equal to one, which makes proceeding with the algorithm invalid.

    Args:
        Exception (class): The exception class.
    """
    pass

def repeated_word(text):
    """
    A function that accepts a string, and returns the first word that occurs more than once.

    Args:
        text (str): Any string.

    Raises:
        InvalidNumberOfKeysError: An exception that gets raised if the number of words in the string passed is smaller than or equal to one.

    Returns:
        str: The first word that is repeated in among the words found in the passed string.
    """
    ht = Hashtable()
    words = list(map(lambda word : word.lower(), re.findall(r"\w+", text)))
    if len(list(words)) <= 1:
        raise InvalidNumberOfKeysError("String provided contains an invalid number of keys.")
    for word in words:
        if ht.contains(word):
            return word
        ht.add(word, None)


if __name__ == "__main__":
    os.system('clear')
    text = "a a"
    ht = Hashtable()
    print(repeated_word(text))
    print("-------------")
   
    