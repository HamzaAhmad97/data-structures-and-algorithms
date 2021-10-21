from stack_and_queue.queue import Queue
from stack_and_queue.node import Node
import pytest

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    return queue

