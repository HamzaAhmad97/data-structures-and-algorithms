from stack_and_queue.stack import Stack
from stack_and_queue.node import Node
import pytest

@pytest.fixture
def send_empty_stack():
    stack = Stack()
@pytest.fixture
def send_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)

def test_push_onto_stack_when_stack_is_empty(send_empty_stack):
    expected = 1
    actual = send_empty_stack.top.value
    assert actual == expected

def test_push_onto_stack_multiple_values(send_stack):
    expected = 2
    actual = send_stack.top.value
    assert actual == expected

