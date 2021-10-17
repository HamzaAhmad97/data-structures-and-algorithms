from linked_list_insertion import __version__
from linked_list_insertion.linked_list_insertions import LinkedList
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.skip('to do')
def test_append():
    expected = "{a} -> {x} -> Null"
    ll = LinkedList()
    ll.insert("a")
    ll.append('x')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_append_multiple_nodes_to_linked_list():
    expected = "{a} -> {x} -> {y} -> Null"
    ll = LinkedList()
    ll.insert("a")
    ll.append('x')
    ll.append('y')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_insert_node_before_a_node_in_the_middle():
    expected = "{a} -> {x} -> {b} -> Null"
    ll = LinkedList()
    ll.insert("b")
    ll.insert("a")
    ll.insert_before('b', 'x')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_insert_node_before_first_node():
    expected = "{x} -> {a} -> Null"
    ll = LinkedList()
    ll.insert('a')
    ll.insert_before('a','x')
    actual = ll.to_string()
    assert actual == expected

@pytest.mark.skip('to do')
def test_insert_after_a_node_in_the_middle():
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
    expected = "{a} -> {x} -> Null"
    ll = LinkedList()
    ll.insert('a')
    ll.insert_after('a','x')
    actual = ll.to_string()
    assert actual == expected
