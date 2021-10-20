from linked_list_kth import __version__
from linked_list_kth.linked_list_kth import LinkedList, OutOfRangeException
import pytest

def test_version():
    assert __version__ == '0.1.0'
@pytest.mark.xfail()
def test_kth_from_end_returns_correct_value_if_number_is_smaller_than_list_length():
    """
    Test if value returned when k is smaller than list length
    """
    expected = 'b'
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.kth_from_end(1)
    assert actual == expected

@pytest.mark.xfail()
def test_kth_from_end_returns_correct_value_when_k_equals_length_of_list():
    """
    Test if value gets returned when k is equal to the number of items in list
    """
    expected = 'c'
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    actual = ll.kth_from_end(2) # since the list is zero indexed
    assert actual == expected

@pytest.mark.xfail()
def test_kth_from_end_raises_an_exception_if_k_is_negative():
    """
    Test if kth_from_end raises an exception if k is negative
    """
    ll = LinkedList()
    ll.insert('a')
    with pytest.raises(OutOfRangeException, match="Distance cannot be negative or exceeding the number of nodes in the list."):
        ll.kth_from_end(-1)

@pytest.mark.xfail()
def test_kth_from_end_raises_an_exception_if_k_is_greater_than_the_length_of_linked_list():
    """
    Test if kth_from_end rases an exception when k is greater than the length of the list
    """
    ll = LinkedList()
    ll.insert('a')
    with pytest.raises(OutOfRangeException, match="Distance cannot be negative or exceeding the number of nodes in the list."):
        ll.kth_from_end(2)


def test_kth_from_end_returns_correct_value_when_linked_list_contains_one_node():
    """
    Test if kth_from_end returns the correct value when the list contains one item
    """
    expected = 'a'
    ll = LinkedList()
    ll.insert('a')
    actual = ll.kth_from_end(0)
    assert actual == expected
