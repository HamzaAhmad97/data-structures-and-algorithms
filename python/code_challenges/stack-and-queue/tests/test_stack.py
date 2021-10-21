import pytest
from stack_and_queue.stack import Stack, EmptyStackException


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    return stack


def test_push_onto_stack_when_stack_is_empty():
    expected = 1
    stack = Stack()
    stack.push(1)
    actual = stack.top.value
    assert actual == expected


def test_push_onto_stack_multiple_values(stack):
    expected = 2
    actual = stack.top.value
    assert actual == expected


def test_pop_off_stack(stack):
    expected = 2
    actual = stack.pop()
    assert expected == actual


def test_stack_is_empty_when_popping_all_nodes(stack):
    stack.pop()
    stack.pop()
    actual = stack.top
    assert not actual


def test_stack_peek(stack):
    expected = 2
    actual = stack.peek()
    assert expected == actual


def test_can_instantiate_empty_stack_by_class(empty_stack):
    expected = "Stack"
    actual = empty_stack.__class__.__name__
    assert actual == expected


def test_can_instantiate_empty_stack_via_peek(stack):
    expected = 2
    actual = stack.peek()
    assert actual == expected


def test_peek_raises_exception_when_called_on_empty_stack(empty_stack):
    with pytest.raises(EmptyStackException, match="Stack is empty, can't peek."):
        empty_stack.peek()


def test_pop_raises_exception_when_called_on_empty_stack(empty_stack):
    with pytest.raises(EmptyStackException, match="Stack is empty, can't pop."):
        empty_stack.pop()
