from tree_breadth_first.binary_search_tree import BinarySearchTree
from tree_breadth_first.exceptions import EmptyTree
from tree_breadth_first.queue import Queue
def breadth_first(tree):
    """
    Return the values of nodes in a binary tree following breadth first search.

    Args:
        tree (BinarySearchTree): A binary search tree instance.

    Raises:
        EmptyTree: If the tree is empty the function will raise the exception.

    Returns:
        list: A list containing the values retreived from the nodes of the trees.
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

