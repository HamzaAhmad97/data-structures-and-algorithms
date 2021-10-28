from trees.exceptions import EmptyTree


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
