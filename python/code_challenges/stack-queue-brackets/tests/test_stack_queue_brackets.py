import pytest
from stack_queue_brackets import __version__
from stack_queue_brackets.validate_brackets import validate_brackets


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize(
    "sequence, is_valid",
    [
        ('{}', True),
        ('{}(){}', True),
        ('()[[Extra Characters]]', True),
        ('(){}[[]]', True),
        ('{}{Code}[Fellows](())', True),
        ('[({}]', False),
        ('(](', False),
        ('{(})', False),
        ('{', False),
        (')', False),
        ('[}', False),
    ],
)
def test_validate_brackets(sequence, is_valid):
    """
    Test the validate_brackets function for 11 different sequences containing characters including brackets.

    Args:
        sequence (str): A string containing a set of characters, may include brackets.
        is_valid (bool): Whether or not the brackets in the string are balanced.
    """
    assert validate_brackets(sequence) == is_valid
