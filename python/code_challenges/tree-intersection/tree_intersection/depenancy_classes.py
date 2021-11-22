class EmptyQueueException(Exception):
    pass

class EmptyTree(Exception):
    pass

class Node:
    def __init__(self, value, _next = None):
        self.value = value
        self.right = None
        self.left = None
        self._next = _next

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, node):
        node._next = None
        if not self.front:
            self.front = node
            self.rear = node
            return
        self.rear._next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty, can't dequeue.")
        temp = self.front
        self.front = temp._next
        temp._next = None
        return temp

    def peek(self):
        if not self.front:
            raise EmptyQueueException("Queue is empty, can't peek!")
        return self.front.value

    def is_empty(self):

        return not self.front

class BinaryTree:

    def __init__(self):
        self.nodes = []
        self.root = None

    def pre_order(self, root):
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

    def __init__(self, *args):
        super().__init__()
        for itm in args:
            self.add(itm)

    def add(self, value):
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

    def __init__(self):
        self.head = None
    def insert(self,value):
        self.head = Node(value, self.head)

class Hashtable:

    def __init__(self, size = 1024):
        self.__size = size
        self.__buckets = [None for _ in range(size)]

    def __hash(self, key):
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        index = self.__hash(key)

        if not self.__buckets[index]:
            self.__buckets[index] = LinkedList()
        val = [key, value]
        self.__buckets[index].insert(val)

    def get(self, key):
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

def breadth_first(tree):
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
