# from tree_breadth_first.node import Node
# from tree_breadth_first.queue import Queue
# from tree_breadth_first.binary_tree import BinaryTree
# from tree_breadth_first.exceptions import EmptyTree
from node import Node
from queue import Queue
from binary_tree import BinaryTree
from exceptions import EmptyTree
import math


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

    def contains(self, value):
        """
        Check if there exists a node in the tree that has a value equals to the passed value.

        Args:
            value (any): The value to be checked for.

        Returns:
            bool: True if the tree has a node that has a value equals the passed value, False otherwise.
        """
        try:
            for item in self.post_order(self.root):
                if item == value:
                    return True
            return False
        except AttributeError:
            return False

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
            representation += f"[Value > {front.value} | Left > {front.left if front.left else '....None'} | Right > {front.right if front.right else '....None'}]\n"
            if front.left:
                q.enqueue(front.left)
            if front.right:
                q.enqueue(front.right)
        return representation

    def max_value(self):
        """
        Rreturn the maximum value in a tree.

        Raises:
            EmptyTree: If the tree is empty.

        Returns:
            int: The maximum value in the tree.
        """
        if not self.root:
            raise EmptyTree(
                'Tree is empty, cannot perform max_value() on an empty tree.')
        max = -math.inf
        breadth = Queue()
        breadth.enqueue(self.root)
        while not breadth.is_empty():
            front = breadth.dequeue()
            max = front.value if (front.value >= max) else max

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)
        return max

    def check_leaves(self, otherTree):

        def check(root):
            count = 0
            q = Queue()
            q.enqueue(root)
            while not q.is_empty():
                front = q.dequeue()
                if front.left:
                    q.enqueue(front.left)
                if front.right:
                    q.enqueue(front.right)
                if not front.left or not front.right:
                    count += 1
            return count

        return check(self.root) == check(otherTree.root)


if __name__ == "__main__":
    bt = BinarySearchTree(*[1, 2, 3, 4, 5, 6])
    ot = BinarySearchTree(*[])
    print(bt.check_leaves(ot))
