from stack_queue_brackets.stack import Stack


def validate_brackets(sequence):
    """
    Check if the brackets in the passed string are balanced.

    Args:
        sequence (str): A string containing anything, may contain various types of brackets.

    Returns:
        bool: Whether or not the brackets in the string are balanced.
    """
    brackets = Stack()
    for ch in sequence:
        if ch in '[]{}()':
            brackets.push(ch)
    return brackets.is_empty()
