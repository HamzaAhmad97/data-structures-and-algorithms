from linked_list import __version__
from linked_list.linked_list import Node, LinkedList
from python.code_challenges.linked_list import linked_list


def test_version():
    assert __version__ == '0.1.0'


def test_linked_list_is_empty_when_instantiated():
    expected = None

    ll = LinkedList()
    actual = ll.__head

    assert actual == expected


def test_insert_to_linked_list():
    expected = "a"

    ll = LinkedList()
    ll.insert("a")
    actual = ll.__head.value

    assert actual == expected


def test_head_points_to_first_node_in_linked_list():
    expected = "last"

    ll = LinkedList()
    ll.insert("first")
    ll.insert("last")
    actual = ll.__head.next_.value

    assert actual == expected

def test_includes_returns_true_if_value_equals_node_value():
    expected = True

    ll = LinkedList()
    ll.insert(1)
    actual = ll.includes(1)

    assert actual == expected
