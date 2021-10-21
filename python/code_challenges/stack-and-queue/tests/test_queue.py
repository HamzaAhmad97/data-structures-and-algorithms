import pytest
from stack_and_queue.queue import Queue, EmptyQueueException
from stack_and_queue.node import Node


@pytest.fixture
def empty_queue():
    """
    Make an empty queue available.

    Returns:
        Queue: An empty queue.
    """
    return Queue()


@pytest.fixture
def queue():
    """
    Make a non-empty queue available.

    Returns:
        Queue: a non-empty queue.
    """
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    return queue


def test_queue_enqueue_to_empty_queue(empty_queue):
    """
    Check if enqueue pushes/ adds a node to an empty queue.
    """
    expected = 0
    empty_queue.enqueue(0)
    actual = empty_queue.front.value
    assert actual == expected


def test_queue_enqueue_with_multiple_nodes(empty_queue):
    """
    Check if enqueue pushes/ adds multiple nodes to a queue.
    """
    expected = 2
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    actual = empty_queue.rear.value
    assert actual == expected


def test_queue_dequeue(queue):
    """
    Check if dequeue returns the value of the front node of a non-empty queue.
    """
    expected = 1
    actual = queue.dequeue()
    assert actual == expected


def test_queue_dequeue_raises_exception_when_empty(empty_queue):
    """
    Check if dequeueing from an empty queue raises an exception.
    """
    with pytest.raises(EmptyQueueException, match="Queue is empty, can't dequeue."):
        empty_queue.dequeue()


def test_queue_peek_raises_exception_when_empty(empty_queue):
    """
    Check if peeking an empty queue raises an exception.
    """
    with pytest.raises(EmptyQueueException, match="Queue is empty, can't peek."):
        empty_queue.peek()


def test_queue_peek(queue):
    """
    Check if peek returns the value of the front node in a non-empty queue.
    """
    expected = 1
    actual = queue.peek()
    assert actual == expected


def test_queue_gets_empty_after_multiple_dequeues(queue):
    """
    Check if a non-empty queue becomes empty when dequeueing all of its nodes.
    """
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()


def test_can_instantiate_empty_queue_by_class(empty_queue):
    """
    Check instantiating an empty queue.
    """
    expected = "Queue"
    actual = empty_queue.__class__.__name__
    assert actual == expected


def test_can_instantiate_empty_queue_via_peek(queue):
    """
    Check instantiating an empty queue.
    """
    expected = 1
    actual = queue.peek()
    assert actual == expected
