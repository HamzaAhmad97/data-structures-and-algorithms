import math
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

    def __init__(self, value = None):
        self.value = value
        self.children = []
        self.next = None

    def __str__(self):
        return f"{self.value}"

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
        self.max = -math.inf

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

    def in_order(self, root):
        """
        Traverse a binary tree in an in-order method.

        Args:
            root (Node): The root node of a tree or a sub-tree.

        Raises:
            EmptyTree: If the tree is empty.

        Returns:
            list: A list containing the values of the nodes after traversing the tree in in-order method.
        """
        if not self.root:
            raise EmptyTree("Tree is empty. Operation is invalid.")

        if root.left:
            self.in_order(root.left)

        print(root.value)
        self.nodes.append(root.value)
        if root.right:
            self.in_order(root.right)

        if root:
            return self.nodes

    def post_order(self, root):
        """
        Traverse a binary tree in an pre-order method.

        Args:
            root (Node): The root node of a tree or a sub-tree.

        Raises:
            EmptyTree: If the tree is empty.

        Returns:
            list: A list containing the values of the nodes after traversing the tree in pre-order method.
        """
        if not self.root:
            raise EmptyTree("Tree is empty. Operation is invalid.")

        if root.left:
            self.post_order(root.left)

        if root.right:
            self.post_order(root.right)

        print(root.value)

        self.nodes.append(root.value)
        if root == self.root:
            return self.nodes

class KTree(BinaryTree):
    """
    A class representing a binary search tree. Extends BinaryTree.

    Args:
        BinaryTree (class): The base binary tree class.
    """

    def __init__(self,k=2, *args):
        """
        The constructor method of a binary search tree, initialize the nodes list, and the root node, as well as add any node to the tree if passed as an argument.
        """
        super().__init__()
        self.k = k
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
        elif len(self.root.children) < self.k :
            self.root.children.append(Node(value))
            return

        q = Queue()
        q.enqueue(self.root)
        while q.peek():
            
            if len(q.front.children) == self.k:
                for child in q.front.children:
                    q.enqueue(child)
                q.dequeue()
            else:
                q.front.children.append(Node(value))
                return

    def __str__(self):
        """
        Construct and return a string representation of a tree.

        Returns:
            str: A string representation of a tree.
        """
        if not self.root:
            return 'Empty tree.'
        q = Queue()
        q.enqueue(self.root)
        representation = ""
        while not q.is_empty():
            front = q.dequeue()
            representation += f"(Value > {front.value} %%% children > {[str(child) for child in front.children]}) \n"
            for child in front.children:
                if child:
                    q.enqueue(child)
        return representation


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

    def __str__(self):
        """
        Return a string representation for a queue.

        Returns:
            str: A string representation for a queue.
        """
        representation = "| "
        if not self.front:
            representation += 'Empty queue.'
        else:
            current = self.front
            while current:
                representation += f"    Value: {current.value}    | "
                current = current.next
            representation += "\n| "
            current = self.front
            while current:
                representation += f"Next: {current.next}  | "
                current = current.next
            return representation

    def enqueue(self, node):
        """
        Push/ enqueue nodes to the back of a queue.

        Args:
            value (any): A node's value
        """
        node.next = None
        if not self.front:
            self.front = node
            self.rear = node
            return
        self.rear.next = node
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
        self.front = temp.next
        temp.next = None
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


def fizz_buzz_tree(kary_tree):
    new_tree = KTree(3)
    q = Queue()
    q.enqueue(kary_tree.root)
    while not q.is_empty():
        front = q.dequeue()
        value = front.value
        if not value % 15:
            new_tree.add(Node("FizzBuzz"))
        elif not value % 3:
            new_tree.add(Node("Fizz"))
        elif not value % 5: 
            new_tree.add(Node("Buzz"))
        else:
            new_tree.add(Node(str(value)))

        for child in front.children:
            q.enqueue(child)
    return new_tree

if __name__ == "__main__":
    bt = KTree(4, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
    print(fizz_buzz_tree(bt))

