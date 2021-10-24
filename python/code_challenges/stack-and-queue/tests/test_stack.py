import pytest
from stack_and_queue.stack import Stack, EmptyStackException


@pytest.fixture
def empty_stack():
    """
    Make an empty stack available.

    Returns:
        Stack: An empty stack.
    """
    return Stack()


@pytest.fixture
def stack():
    """
    Make a non-empty stack available.

    Returns:
        Stack: a non-empty stack.
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    return stack


def test_push_onto_stack_when_stack_is_empty():
    """
    Check if push pushes nodes to an empty stack.
    """
    expected = 1
    stack = Stack()
    stack.push(1)
    actual = stack.top.value
    assert actual == expected


def test_push_onto_stack_multiple_values(stack):
    """
    Check if push pushes multiple nodes to a stack.
    """
    expected = 2
    actual = stack.top.value
    assert actual == expected


def test_pop_off_stack(stack):
    """
    Check if pop returns the value of the top node of a non-empty stack.
    """
    expected = 2
    actual = stack.pop()
    assert expected == actual


def test_stack_is_empty_when_popping_all_nodes(stack):
    """
    Check if a non-empty stack becomes empty when popping all of its nodes.
    """
    stack.pop()
    stack.pop()
    actual = stack.top
    assert not actual


def test_stack_peek(stack):
    """
    Check if peek returns the value of the top node in a non-empty stack.
    """
    expected = 2
    actual = stack.peek()
    assert expected == actual


def test_can_instantiate_empty_stack_by_class(empty_stack):
    """
    Check instantiating an empty stack.
    """
    expected = "Stack"
    actual = empty_stack.__class__.__name__
    assert actual == expected


def test_can_instantiate_empty_stack_via_peek(stack):
    """
    Check instantiating an empty stack.
    """
    expected = 2
    actual = stack.peek()
    assert actual == expected


def test_peek_raises_exception_when_called_on_empty_stack(empty_stack):
    """
    Check if peeking an empty stack raises an exception.
    """
    with pytest.raises(EmptyStackException, match="Stack is empty, can't peek."):
        empty_stack.peek()


def test_pop_raises_exception_when_called_on_empty_stack(empty_stack):
    """
    Check if popping from an empty stack raises an exception.
    """
    with pytest.raises(EmptyStackException, match="Stack is empty, can't pop."):
        empty_stack.pop()
