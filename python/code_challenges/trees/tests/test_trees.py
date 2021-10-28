from trees import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_instantiating_an_empty_tree_instance():
    expected = None
    bt = BinarySearchTree()
    actual = bt.root
    assert actual == expected

def test_instantiating_a_tree_with_a_single_root_node():
    expected = "a"
    bt = BinarySearchTree("a")
    actual = bt.root.value
    assert actual == expected

def test_adding_a_left_child_and_a_right_child():
    expected = ("b","c")
    bt = BinarySearchTree()
    bt.add("b")
    bt.add("c")
    actual = (bt.root.left.value, bt.root.right,value)
    assert actual == expected

def test_returning_a_collection_from_a_preorder_traversal():
    expected = "abdecf"
    bt = BinarySearchTree("a","b","c","d","e","f")
    actual = "".join(bt.pre_order(bt.root))
    assert actual == expected

