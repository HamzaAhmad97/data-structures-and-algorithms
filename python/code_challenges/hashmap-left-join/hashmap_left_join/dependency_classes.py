class EmptyQueueException(Exception):
    """
    A class representing an exception that gets raised when operating on an empty queue.

    Args:
        Exception (class): The exception class.
    """
    pass

class EmptyTree(Exception):
    """
    A class representing an exception that gets raised when operating on an empty tree.

    Args:
        Exception (class): The exception class.
    """
    pass

class Node:
    """
    A class representing a node in a linked list

    Methods:
        __init__(value : any):
            the constructor method, takes a value argument
        __str__():
            return a string representation for the Node instance

    """
    def __init__(self, value, _next = None):
        self.value = value
        self.right = None
        self.left = None
        self._next = _next

class Queue:
    """
    A class representing a stack.
    """

    def __init__(self):
        """
        The constructor method for the class Queue. Initialize front and rear.
        """
        self.front = None
        self.rear = None

    def enqueue(self, node):
        """
        Push/ enqueue nodes to the back of a queue.

        Args:
            value (any): A node's value
        """
        node._next = None
        if not self.front:
            self.front = node
            self.rear = node
            return
        self.rear._next = node
        self.rear = node

    def dequeue(self):
        """
        Remove/ dequeue a node from the front of a queue.

        Raises:
            EmptyQueueException: If queue is empty.

        Returns:
            any: The value of the node dequeued.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty, can't dequeue.")
        temp = self.front
        self.front = temp._next
        temp._next = None
        return temp

    def peek(self):
        """
        Return the value of the front node.

        Raises:
            EmptyQueueException: If the queue is empty.

        Returns:
            any: The value of the front node.
        """
        if not self.front:
            raise EmptyQueueException("Queue is empty, can't peek!")
        return self.front.value

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.
        """

        return not self.front

class BinaryTree:
    """
    A class representing the base for a binary search tree.
    """

    def __init__(self):
        """
        The constructor method for the binary tree class, initializing the nodes and the root attributes.
        """
        self.nodes = []
        self.root = None

    def pre_order(self, root):
        """
        Traverse a binary tree in a pre_order method.

        Args:
            root (Node): The root node of a tree or a sub-tree.

        Raises:
            EmptyTree: If the tree is empty.

        Returns:
            list: A list containing the values of the nodes after traversing the tree in pre-order method.
        """
        if not self.root:
            raise EmptyTree("Tree is empty. Operation is invalid.")

        print(root.left, root.right)
        self.nodes.append(root.value)

        if root.left:
            self.pre_order(root.left)

        if root.right:
            self.pre_order(root.right)

        if root:
            return self.nodes

class BinarySearchTree(BinaryTree):
    """
    A class representing a binary search tree. Extends BinaryTree.

    Args:
        BinaryTree (class): The base binary tree class.
    """

    def __init__(self, *args):
        """
        The constructor method of a binary search tree, initialize the nodes list, and the root node, as well as add any node to the tree if passed as an argument.
        """
        super().__init__()
        for itm in args:
            self.add(itm)

    def add(self, value):
        """
        Add a node to a binary tree. Follows breadth first traversal.

        Args:
            value (any): The value to be stored in a node that will get connected to the tree.
        """
        if not self.root:
            self.root = Node(value)
            return
        breadth = Queue()
        breadth.enqueue(self.root)
        while breadth.peek():
            if breadth.front.left and breadth.front.right:
                breadth.enqueue(breadth.front.left)
                breadth.enqueue(breadth.front.right)
                breadth.dequeue()
            elif not breadth.front.left:
                breadth.front.left = Node(value)
                return
            elif not breadth.front.right:
                breadth.front.right = Node(value)
                return

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
    """

    def __init__(self):
        """
        The constructor method for the linked list, initializes the head property to None
        """
        self.head = None
    def insert(self,value):
        """
        Insert a node into the linked list

        Args:
            value (any): the value to be stored as the valur inside of the new node
        """
        self.head = Node(value, self.head)

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

    def get_nodes(self):
        """
        Return a list containing all the nodes that hold key/value pairs in a hashtable.

        Returns:
            list: a list containing all the nodes that hold key/value pairs in a hashtable.
        """
        container = []
        for itm in self.__buckets:
            if isinstance(itm, LinkedList):
                current = itm.head
                while current:
                    container.append(current)
                    current = current._next
        return container


def breadth_first(tree):
    """
    A function to iterate over the nodes in a binary tree and returns all the nodes in it in breadth first style.
    """
    if not tree.root:
            raise EmptyTree('Tree is empty, cannot perform max_value() on an empty tree.')
    container = []
    q = Queue()
    q.enqueue(tree.root)
    while not q.is_empty():
        front = q.dequeue()
        container.append(front.value)
        if front.left:
            q.enqueue(front.left)

        if front.right:
            q.enqueue(front.right)
    return container

if __name__ == "__main__":
    ht = Hashtable()
    ht.add("a", "a")
    ht.add("b", "b")
    ht.add("c", "c")
    print(ht.get_keys())
