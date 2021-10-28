from trees import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_creating_an_empty_tree_instance():
    expected = None
    bt = BinarySearchTree()
    actual = bt.root
    assert actual == expected


