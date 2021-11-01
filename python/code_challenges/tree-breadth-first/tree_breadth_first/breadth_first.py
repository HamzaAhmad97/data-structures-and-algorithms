from tree_breadth_first.binary_search_tree import BinarySearchTree
from tree_breadth_first.exceptions import EmptyTree
from tree_breadth_first.queue import Queue
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

