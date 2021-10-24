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



