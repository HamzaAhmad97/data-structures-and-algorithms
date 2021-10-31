import pytest
from trees.exceptions import EmptyTree
from trees import __version__
from trees.binary_search_tree import BinarySearchTree

def test_version():
    assert __version__ == '0.1.0'

def test_instantiating_an_empty_tree_instance():
    """
    Check for correctly instantiating an empty tree instance.
    """
    expected = None
    bt = BinarySearchTree()
    actual = bt.root
    assert actual == expected

def test_instantiating_a_tree_with_a_single_root_node():
    """
    Check for correctly instantiating a tree given a single value as the root.
    """
    expected = "a"
    bt = BinarySearchTree("a")
    actual = bt.root.value
    assert actual == expected

def test_adding_a_left_child_and_a_right_child():
    """
    Check for adding a left and a right node to a tree that only has a root.
    """
    expected = ("b","c")
    bt = BinarySearchTree()
    bt.add("a")
    bt.add("b")
    bt.add("c")
    actual = (bt.root.left.value, bt.root.right.value)
    assert actual == expected

def test_returning_a_collection_from_a_preorder_traversal():
    """
    Check for returning a correct collection of nodes' values using pre-order method.
    """
    expected = "abdecf"
    bt = BinarySearchTree("a","b","c","d","e","f")
    actual = "".join(bt.pre_order(bt.root))
    assert actual == expected

def test_returning_a_collection_from_a_inorder_traversal():
    """
    Check for returning a correct collection of nodes' values using in-order method.
    """
    expected = "dbeafc"
    bt = BinarySearchTree("a","b","c","d","e","f")
    actual = "".join(bt.in_order(bt.root))
    assert actual == expected

def test_returning_a_collection_from_a_postorder_traversal():
    """
    Check for returning a correct collection of nodes' values using post-order method.
    """
    expected = "debfca"
    bt = BinarySearchTree("a","b","c","d","e","f")
    actual = "".join(bt.post_order(bt.root))
    assert actual == expected

def test_traversal_over_an_empty_tree_raises_an_exception():
    """
    Check if operating on an empty tree raises an empty tree exception.
    """
    bt = BinarySearchTree()
    with pytest.raises(EmptyTree):
        bt.pre_order(bt.root)

