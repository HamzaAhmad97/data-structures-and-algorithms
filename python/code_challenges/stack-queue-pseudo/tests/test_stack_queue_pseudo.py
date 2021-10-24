import pytest
from stack_queue_pseudo import __version__


def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def empty_pseudo_queue():
    return PseudoQueue()

def test_enqueue_one_node_to_empty_pseudo_queue(empty_pseudo_queue):
    empty_pseudo_queue.push(1)
    expected = 1
    actual = empty_pseudo_queue.dequeue()
    assert actual == expected

def test_enqueue_multiple_nodes_to_pseudo_queue(empty_pseudo_queue):
    empty_pseudo_queue.push(1)
    empty_pseudo_queue.push(2)
    expected = 1
    actual = empty_pseudo_queue.dequeue()
    assert actual == expected


