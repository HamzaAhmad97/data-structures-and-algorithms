import pytest
from stack_queue_brackets import __version__

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
    assert validate_brackets(sequence) == is_valid
