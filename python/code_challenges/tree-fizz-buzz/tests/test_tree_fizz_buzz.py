from tree_fizz_buzz import __version__
from tree_fizz_buzz.fizz_buzz_tree import fizz_buzz_tree, KTree

def test_version():
    assert __version__ == '0.1.0'

def test_fizz_buzz_tree_k_1():
    """
    Test fizz_buzz_tree function with a tree of k = 1
    """
    expected = 1
    kt = KTree(1,1)
    actual = kt.root.value
    assert actual == expected

def test_fizz_buzz_tree_k_2():
    """
    Test fizz_buzz_tree function with a tree of k = 2
    """
    expected = " 1 | 2 | Fizz | 4 |"
    kt = KTree(2,1,2,3,4)
    actual = str(fizz_buzz_tree(kt))
    assert expected == actual

def test_fizz_buzz_tree_k_4():
    """
    Test fizz_buzz_tree function with a tree of k = 4
    """
    expected = " 1 | 2 | Fizz | 4 | Buzz | Fizz | 7 | 8 | Fizz | Buzz | 11 | Fizz | 13 | 14 | FizzBuzz | 16 |"
    kt = KTree(2, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
    actual = str(fizz_buzz_tree(kt))
    assert actual == expected