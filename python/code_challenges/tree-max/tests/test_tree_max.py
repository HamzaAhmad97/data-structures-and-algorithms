import pytest
from tree_max import __version__
from tree_max.binary_search_tree import BinarySearchTree

def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize(
    "values, max",
    [
        ([1,2,3,4,5,6], 6),
        ([1,1,4,8,6,-1,20], 20),
        ([5,1,1,1,1],5),
        ([-5,-2,-1,0,0],0),
        ([2,2,1,1,2,2],2),
        ([2],2),
    ],
)
def test_max_value(values, max):
    """
    Test if the method max_value returns the correct max value when passing a number of integers as a list.

    Args:
        values (list): A list of values to be added to the tree.
        max (int): The maximum value in the tree.
    """
    bt = BinarySearchTree(*values)
    assert bt.max_value() == max
