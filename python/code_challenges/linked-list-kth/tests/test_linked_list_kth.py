from linked_list_kth import __version__
from linked_list_kth.linked_list_kth import LinkedList
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_kth_from_end_returns_correct_value_if_number_is_smaller_than_list_length():
    expected = 'b'
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.kth_from_end(1)
    assert actual == expected


