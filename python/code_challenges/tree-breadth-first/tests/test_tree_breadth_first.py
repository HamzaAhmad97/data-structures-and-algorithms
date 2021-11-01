import pytest
from tree_breadth_first import __version__
from tree_breadth_first.breadth_first import breadth_first
from tree_breadth_first.binary_search_tree import BinarySearchTree

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize(
    "values, result",
    [
        ([1,2,3,4,5,6], [1,2,3,4,5,6]),
        ([1,1,4,8,6,-1,20], [1,1,4,8,6,-1,20]),
        ([5,1,1,1,1],[5,1,1,1,1]),
        ([-5,-2,-1,0,0],[-5,-2,-1,0,0]),
        ([2,2,1,1,2,2],[2,2,1,1,2,2]),
        ([2],[2]),
    ],
)
def test_breadth_first(values, result):
    bt = BinarySearchTree(*values)
    assert breadth_first(bt) == result
