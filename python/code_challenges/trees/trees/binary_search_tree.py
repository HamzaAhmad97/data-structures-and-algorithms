from trees.node import Node
from trees.queue import Queue
from trees.binary_tree import BinaryTree


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

    def contains(self, value):
        try:
            for item in self.post_order(self.root):
                if item == value:
                    return True
            return False
        except AttributeError:
            return False

    def __str__(self):
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
