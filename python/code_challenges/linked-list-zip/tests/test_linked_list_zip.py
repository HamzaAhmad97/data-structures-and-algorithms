from linked_list_zip import __version__
from linked_list_zip.linked_list_zip import LinkedList, EmptyLinkedListException, zip_lists
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_zip_lists_returns_correct_result_when_both_lists_are_of_the_same_length():
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


