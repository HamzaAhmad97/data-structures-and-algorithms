from linked_list_kth import __version__
from linked_list_kth.linked_list_kth import LinkedList, OutOfRangeException
import pytest

def test_version():
    assert __version__ == '0.1.0'
@pytest.mark.xfail()
def test_kth_from_end_returns_correct_value_if_number_is_smaller_than_list_length():
    expected = 'b'
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.kth_from_end(1)
    assert actual == expected

@pytest.mark.xfail()
def test_kth_from_end_returns_correct_value_when_k_equals_length_of_list():
    expected = 'c'
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.kth_from_end(2) # since the list is zero indexed
    assert actual == expected

@pytest.mark.xfail()
def test_kth_from_end_raises_an_exception_if_k_is_negative():
    ll = LinkedList()
    ll.insert('a')
    with pytest.raises(OutOfRangeException, match="Distance cannot be negative or exceeding the number of nodes in the list."):
        ll.kth_from_end(-1)

@pytest.mark.xfail()
def test_kth_from_end_raises_an_exception_if_k_is_greater_than_the_length_of_linked_list():
    ll = LinkedList()
    ll.insert('a')
    with pytest.raises(OutOfRangeException, match="Distance cannot be negative or exceeding the number of nodes in the list."):
        ll.kth_from_end(2)


def test_kth_from_end_returns_correct_value_when_linked_list_contains_one_node():
    expected = 'a'
    ll = LinkedList()
    ll.insert('a')
    actual = ll.kth_from_end(0)
    assert actual == expected
