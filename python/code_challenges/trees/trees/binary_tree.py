class BinaryTree:

    def __init__(self):
        self.nodes = []
        self.root = None

    def pre_order(self, root):
        if not self.root:
            raise EmptyTree("Tree is empty. Operation is invalid.")

        print(root.value)

        if root.left:
            self.pre_order(root.left)

        if root.right:
            self.pre_order(root.right)

        self.nodes.append(root.value)
        if root == self.root:
           return self.nodes

    def in_order(self, root):
        if not self.root:
            raise EmptyTree("Tree is empty. Operation is invalid.")

        if root.left:
            self.in_order(root.left)

        print(root.value)

        if root.right:
            self.in_order(root.right)

        self.nodes.append(root.value)
        if root == self.root:
           return self.nodes

    def post_order(self, root):
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
