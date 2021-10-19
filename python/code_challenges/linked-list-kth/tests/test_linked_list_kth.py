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


def test_kth_from_end_returns_correct_value_when_k_equals_length_of_list():
    expected = 'c'
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.kth_from_end(2) # since the list is zero indexed
    assert actual == expected

def test_kth_from_end_raises_an_exception_if_k_is_negative():
    ll = LinkedList()
    ll.insert('a')
    with pytest.raises(OutOfRangeException, match="Distance cannot be negative or exceeding the number of nodes in the list."):
        ll.kth_from_end(-1)


