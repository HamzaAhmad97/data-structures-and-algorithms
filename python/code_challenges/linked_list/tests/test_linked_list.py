from linked_list import __version__
from linked_list.linked_list import LinkedList
import pytest


@pytest.mark.skip('to do')
def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.skip('to do')
def test_linked_list_is_empty_when_instantiated():
    """
    Test if the linked list is empty when it is first created
    """
    expected = None

    ll = LinkedList()
    actual = ll.head

    assert actual == expected


@pytest.mark.skip('to do')
def test_insert_to_linked_list():
    """
    Test if the insert method works by inserting a value and then checking for the head of the linked list
    """
    expected = "a"

    ll = LinkedList()
    ll.insert("a")
    actual = ll.head.value

    assert actual == expected


@pytest.mark.skip('to do')
def test_head_points_to_first_node_in_linked_list():
    """
    Test if the head property points to the first node
    """
    expected = "last"

    ll = LinkedList()
    ll.insert("first")
    ll.insert("last")
    actual = ll.head.value

    assert actual == expected


@pytest.mark.skip('to do')
def test_includes_returns_true_if_value_equals_node_value():
    """
    Test if the includes method returns True if the value passed exists in a node inside the linked list
    """
    expected = True

    ll = LinkedList()
    ll.insert(1)
    actual = ll.includes(1)

    assert actual == expected


@pytest.mark.skip('to do')
def test_includes_returns_false_if_value_does_not_equal_node_value():
    """
    Test if the includes method returns False if the value passed does not exist in a node in the linked list
    """
    expected = False

    ll = LinkedList()
    ll.insert(2)
    actual = ll.includes(3)

    assert actual == expected


@pytest.mark.skip('to do')
def test_insert_multiple_nodes_to_linked_list():
    """
    Test if inserting more than value to the linked list works correctly
    """
    expected = True

    ll = LinkedList()
    ll.insert(0)
    ll.insert(1)
    first = ll.includes(0)
    second = ll.includes(1)
    actual = first and second

    assert actual == expected


@pytest.mark.skip('to do')
def test_to_string_returns_a_good_representation_of_list():
    """
    Test the to_string method whether it returns the correct representation for the linked list
    """
    expected = "{c} -> {b} -> Null"

    ll = LinkedList()
    ll.insert("b")
    ll.insert("c")
    actual = ll.to_string()

    assert actual == expected
