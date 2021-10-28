# Trees

Trees are a common data structure that also relies on the idea of having nodes that hold values and that are also connected to each other via references stored in them. From their names, trees consist of nodes that when connected will look like a tree because the root branches to other nodes, and the branches keep branching and so on. Tress also share a set of terminologies, like a node, which is the basic unit in a tree, and it holds a value, and a reference to other nodes. The root is the node at the beginning of the tree. We also have K, which is a number that specifies the maximum number of children a node can have in a k-ary tree, so for example, if we are having a binary tree, this means that each node is allowed to reference or connect to other two nodes tops. Also, in a binary tree, since we have two nodes connected to each node, we give them the names right and left. Since nodes connect to each other, they connect via what is called an edge, which is simply a link between a parent and a child node. A leaf is a node that does not have any children but is connected of course to its parent node. Considering the height, it refers to the depth of the tree, or in other words, it means how many edges we have until we walk directly from the root towards the last child or the leaf node.

## [Latest Open Pull Request](https://github.com/HamzaAhmad97/data-structures-and-algorithms/pull/31)

## Challenge

This challenge requires defining BinaryTree, BinarySearchTree, and Node classes. Each node instance should have value, left, and right properties, and each binary tree instance should represent the base for a binary search tree, and should define three method for traversing a binary tree. Each method should return a correct collection representing the retreival of values from nodes. Binary search tree instances should define an add method to `add` nodes to a tree using breadth first traversal, and a `contains` method to check if a given value exists in a node in a binary tree. As an addition, I added the `__str__` method for both the node and the binary search tree classes. 

## Approach & Efficiency

The three methods of traversing a tree in a depth first manner, pre-order, in-order, and post-order use recursion to do their jobs, which results in space complexity of O(1) and time complexity of O(log(N)). 

`add` method follows the breadth first approach. Inside it a queue gets created, and the actual work takes place in a while loop, so the time complexity is expected to be O(N), and the space complexity O(w) where w is the largest width of the tree. `contains` method relies on the returned collection from the pre-order method so its time compexity is expected to be O(log(N)) and the space complexity O(1). The `__str__` in the binary search tree follows the same approach as the `add` method.

## API

* `pre_order(root)`: Traverse in a depth first manner following pre-order method.
* `in_order(root)`: Traverse in a depth first manner following in-order method.
* `post_order(root)`: Traverse in a depth first manner following post-order method.
* `add(value)`: Traverse in a breadth first manner and add a node to the tree storing the value.
* `contains(value)`: Check if a tree has a node that has a value equals the passed value.

