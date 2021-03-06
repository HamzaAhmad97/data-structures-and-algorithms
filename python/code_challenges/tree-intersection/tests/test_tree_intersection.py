import pytest
from tree_intersection import __version__
from tree_intersection.depenancy_classes import BinarySearchTree
from tree_intersection.tree_intersection import tree_intersection

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize(
    "tree_a,tree_b,intersections",
    [
        ([1,2,3], [1,2,3], [1,2,3]),
        ([2], [1,3],None ),
        ([1,2], [1,2], [1,2]),
        ([1],[2],None),
        ([],[], None),
        ([], [1], None),
        ([1,1,1], [1,1,1], [1])
    ]
)
def test_tree_intersection(tree_a, tree_b, intersections):
    a = BinarySearchTree(*tree_a)
    b = BinarySearchTree(*tree_b)
    assert tree_intersection(a,b) == intersections

