from tree_fizz_buzz import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_fizz_buzz_tree_k_1():
    expected = "1"
    kt = KTree(1,1)
    actual = fizz_buzz_tree(kt).front.value
    assert actual == expected

