from linked_list import __version__
from linked_list.linked_list import Node, LinkedList


def test_version():
    assert __version__ == '0.1.0'

def test_linked_list_is_empty_when_instantiated():
    expected = None

    ll = LinkedList()
    actual = ll.__head

    assert actual == expected


def test_insertion_to_linked_list():
    expected = "a"

    ll = LinkedList()
    ll.insert("a")
    actual = ll.__head.value

    assert actual == expected
