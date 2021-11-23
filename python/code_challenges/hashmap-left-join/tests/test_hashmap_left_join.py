import pytest
from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import left_join

def test_version():
    assert __version__ == '0.1.0'



@pytest.mark.parametrize(
    "left_hashtable,right_hashtable, expected", 
    [
        (
            [("a", "a"), ("b", "b"),("c","c"),],
            [("a","1"),("a","2"),("b", "1"),], 
            [('a', ('a', '1')), ('a', ('a', '2')), ('b', ('b', '1')), ('c', ('c', None))]
        ), 
        (
            [("a", "a"), ("b", "b"),("c","c"),],
            [("a","1"),("a","2"),("a", "3"),], 
            [('a', ('a', '1')), ('a', ('a', '2')), ('a', ('a', '3')), ('b', ('b', None)) ,('c', ('c', None))]
        ), 
        (
            [("a", "a"), ("b", "b"),("c","c"),],
            [("i","1"),("j","2"),("k", "1"),], 
            [('a', ('a', None)), ('b', ('b', None)) ,('c', ('c', None))]
        ), 
        (
            [],
            [("i","1"),("j","2"),("k", "1"),], 
            []
        ), 
    ]
)

# [('a', ('11', 'dddd')), ('a', ('11', 'dd')), ('a', ('11', '4')), ('b', ('22', '2')), ('c', ('33', '3'))]