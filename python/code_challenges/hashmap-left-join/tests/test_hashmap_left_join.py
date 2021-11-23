
import pytest
from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import left_join
from hashmap_left_join.dependency_classes import Hashtable

def test_version():
    assert __version__ == '0.1.0'


def test_left_join_1():
    """
    Test left join scenario 1
    """
    expected = [('a', ('a', '2')), ('a', ('a', '1')), ('b', ('b', '1')), ('c', ('c', None))]
    ht_left = Hashtable()
    ht_right = Hashtable()
    val_left = [("a", "a"), ("b", "b"),("c","c"),]
    val_right = [("a","1"),("a","2"),("b", "1"),]
    for key, value in val_left:
        ht_left.add(key, value)
    for key, value in val_right:
        ht_right.add(key, value)
    assert left_join(ht_left, ht_right) == expected

def test_left_join_2():
    """
    Test left join scenario 2
    """
    expected = [('a', ('a', '3')), ('a', ('a', '2')), ('a', ('a', '1')), ('b', ('b', None)) ,('c', ('c', None))]
    ht_left = Hashtable()
    ht_right = Hashtable()
    val_left = [("a", "a"), ("b", "b"),("c","c"),]
    val_right = [("a","1"),("a","2"),("a", "3"),]
    for key, value in val_left:
        ht_left.add(key, value)
    for key, value in val_right:
        ht_right.add(key, value)
    assert left_join(ht_left, ht_right) == expected

def test_left_join_with_empty_left_hashtable():
    """
    Test left join scenario 3 with an empty left hashtable.
    """
    expected = []
    ht_left = Hashtable()
    ht_right = Hashtable()
    val_left = []
    val_right = [("i","1"),("j","2"),("k", "1"),]
    for key, value in val_left:
        ht_left.add(key, value)
    for key, value in val_right:
        ht_right.add(key, value)
    assert left_join(ht_left, ht_right) == expected

def test_left_join_4():
    """
    Test left join scenario 4
    """
    expected = [('a', ('a', None)), ('b', ('b', None)) ,('c', ('c', None))]
    ht_left = Hashtable()
    ht_right = Hashtable()
    val_left = [("a", "a"), ("b", "b"),("c","c"),]
    val_right = [("i","1"),("j","2"),("k", "1"),]
    for key, value in val_left:
        ht_left.add(key, value)
    for key, value in val_right:
        ht_right.add(key, value)
    assert left_join(ht_left, ht_right) == expected





# @pytest.fixture(scope="function")
# def hashtable_left(vals):
#     ht = Hashtable()
#     for key, val in vals:
#         ht.add(key, val)
#     return ht

# @pytest.fixture(scope="function")
# def hashtable_right(vals):
#     ht = Hashtable()
#     for key, val in vals:
#         ht.add(key, val)
#     return ht

# @pytest.mark.parametrize(
#     "hashtable_left,hashtable_right,expected", 
#     [
#         (
#             [("a", "a"), ("b", "b"),("c","c"),],
#             [("a","1"),("a","2"),("b", "1"),], 
#             [('a', ('a', '1')), ('a', ('a', '2')), ('b', ('b', '1')), ('c', ('c', None))]
#         ), 
#         (
#             [("a", "a"), ("b", "b"),("c","c"),],
#             [("a","1"),("a","2"),("a", "3"),], 
#             [('a', ('a', '1')), ('a', ('a', '2')), ('a', ('a', '3')), ('b', ('b', None)) ,('c', ('c', None))]
#         ), 
#         (
#             [("a", "a"), ("b", "b"),("c","c"),],
#             [("i","1"),("j","2"),("k", "1"),], 
#             [('a', ('a', None)), ('b', ('b', None)) ,('c', ('c', None))]
#         ), 
#         (
#             [],
#             [("i","1"),("j","2"),("k", "1"),], 
#             []
#         ), 
#     ],
#     indirect=['hashtable_left','hashtable_right']
# )
# def test_left_join(hashtable_left, hashtable_right, expected):
#     assert left_join(hashtable_left, hashtable_right) == expected
