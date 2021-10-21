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

def test_pop_off_stack(send_stack):
    expected = 2
    actual = send_stack.pop()
    assert expected == actual

def test_stack_is_empty_when_popping_all_nodes(send_stack):
    send_stack.pop()
    send_stack.pop()
    actual = send_stack.top
    assert not actual

def test_stack_peak(send_stack):
    expected = 2
    actual = send_stack.peak()
    assert expected == actual
