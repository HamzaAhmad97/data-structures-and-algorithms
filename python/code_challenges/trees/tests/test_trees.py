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



