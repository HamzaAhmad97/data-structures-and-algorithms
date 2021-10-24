import pytest
from stack_queue_pseudo import __version__
from stack_queue_pseudo.pseudo_queue import PseudoQueue, EmptyPseudoQueueException

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def empty_pseudo_queue():
    """
    Represents an empty pseudo queue.

    Returns:
        PseudoQueue: An empty PseudoQueue instance.
    """
    return PseudoQueue()

def test_enqueue_one_node_to_empty_pseudo_queue(empty_pseudo_queue):
    """
    Test enqueueing a node to an empty pseudo queue.

    Args:
        empty_pseudo_queue (PseudoQueue): An empty PseudoQueue instance.
    """
    empty_pseudo_queue.enqueue(1)
    expected = 1
    actual = empty_pseudo_queue.dequeue()
    assert actual == expected

def test_enqueue_multiple_nodes_to_pseudo_queue(empty_pseudo_queue):
    """
    Test enqueueing more than one node to an empty pseudo queue.

    Args:
        empty_pseudo_queue (PseudoQueue): An empty PseudoQueue instance.
    """
    empty_pseudo_queue.enqueue(1)
    empty_pseudo_queue.enqueue(2)
    expected = 1
    actual = empty_pseudo_queue.dequeue()
    assert actual == expected

def test_dequeue_raises_exception_when_pseudo_queue_is_empty(empty_pseudo_queue):
    """
    Test if dequeueing from an empty pseudo queue raises an exception.

    Args:
        empty_pseudo_queue (PseudoQueue): An empty PseudoQueue instance.
    """
    with pytest.raises(EmptyPseudoQueueException, match="Pseudo queue is empty, can't dequeue."):
        empty_pseudo_queue.dequeue()

