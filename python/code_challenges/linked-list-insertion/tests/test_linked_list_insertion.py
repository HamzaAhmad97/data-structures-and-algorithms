from linked_list_insertion import __version__
from linked_list_insertion.linked_list_insertion import LinkedList
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.skip('to do')
def test_append():
    """
    Test the append method of a linked list
    """
    expected = "{a} -> {x} -> Null"
    ll = LinkedList()
    ll.insert("a")
    ll.append('x')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_append_multiple_nodes_to_linked_list():
    """
    Test appending more than one node to a linked list
    """
    expected = "{a} -> {x} -> {y} -> Null"
    ll = LinkedList()
    ll.insert("a")
    ll.append('x')
    ll.append('y')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_insert_node_before_a_node_in_the_middle():
    """
    Test inserting a node before some node in the middle of a linked list
    """
    expected = "{a} -> {x} -> {b} -> Null"
    ll = LinkedList()
    ll.insert("b")
    ll.insert("a")
    ll.insert_before('b', 'x')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_insert_node_before_first_node():
    """
    Test inserting a node before the first node in a linked list
    """
    expected = "{x} -> {a} -> Null"
    ll = LinkedList()
    ll.insert('a')
    ll.insert_before('a','x')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_insert_after_a_node_in_the_middle():
    """
    Test inserting a node after a node in the middle of a linked list
    """
    expected = "{b} -> {c} -> {x} -> {a} -> Null"
    ll = LinkedList()
    ll.insert('a')
    ll.insert('c')
    ll.insert('b')
    ll.insert_after('c','x')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_insert_after_the_last_node():
    """
    Test inserting a node after the last node in a linked list
    """
    expected = "{a} -> {x} -> Null"
    ll = LinkedList()
    ll.insert('a')
    ll.insert_after('a','x')
    actual = ll.to_string()
    assert actual == expected

def test_delete_node():
    expected = "{a} -> Null"
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.delete_node('b')
    actual = ll.to_string()
    assert actual == expected
