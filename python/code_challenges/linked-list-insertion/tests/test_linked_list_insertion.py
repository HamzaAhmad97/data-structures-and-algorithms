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
