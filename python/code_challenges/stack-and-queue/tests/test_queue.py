import pytest
from stack_and_queue.queue import Queue, EmptyQueueException
from stack_and_queue.node import Node


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    return queue


def test_queue_enqueue_to_empty_queue(empty_queue):
    expected = 0
    empty_queue.enqueue(0)
    actual = empty_queue.front.value
    assert actual == expected


def test_queue_enqueue_with_multiple_nodes(empty_queue):
    expected = 2
    empty_queue.enqueue(1)
    empty_queue.enqueue(2)
    actual = empty_queue.front.value
    assert actual == expected


def test_queue_dequeue(queue):
    expected = 1
    actual = queue.dequeue().value
    assert actual == expected


def test_queue_dequeue_raises_exception_when_empty(empty_queue):
    with pytest.raises(EmptyQueueException, match="Queue is empty, can't dequeue.")
    empty_queue.dequeue()


def test_queue_peek_raises_exception_when_empty(empty_queue):
    with pytest.raises(EmptyQueueException, match="Queue is empty, can't peek.")
    empty_queue.peek()


def test_queue_peek(queue):
    expected = 1
    actual = queue.peek()
    assert actual == expected


