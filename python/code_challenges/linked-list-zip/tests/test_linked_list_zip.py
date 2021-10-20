from linked_list_zip import __version__
from linked_list_zip.linked_list_zip import LinkedList, EmptyLinkedListException, zip_lists
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_zip_lists_returns_correct_result_when_both_lists_are_of_the_same_length():
    """
    Check if zipping two lists with the same length returns the correct result
    """
    expected = "{c} -> {3} -> {b} -> {2} -> {a} -> {1} -> Null"
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")
    kk = LinkedList()
    kk.insert("1")
    kk.insert("2")
    kk.insert("3")
    actual = zip_lists(ll,kk).to_string()
    assert actual == expected

def test_zip_lists_returns_correct_result_when_lists_are_not_of_the_same_length():
    """
    Check if zipping two lists of different length returns the correct result.
    """
    expected = '{b} -> {3} -> {a} -> {2} -> {1} -> Null'
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    kk = LinkedList()
    kk.insert("1")
    kk.insert("2")
    kk.insert("3")
    actual = zip_lists(ll,kk).to_string()

def test_zip_lists_raises_an_exception_when_either_of_lists_is_empty():
    """
    Check if passing one or two empty linked lists raises an exception.
    """
    ll = LinkedList()
    ll.insert('a')
    kk = LinkedList()
    with pytest.raises(EmptyLinkedListException, match="One or both arguments are empty linked lists."):
        zip_lists(ll,kk)
