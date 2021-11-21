import pytest
from hashmap_repeated_word import __version__
from hashmap_repeated_word.hashtable_repeated_word import repeated_word

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize(
    "text,repeated",
    [
        ("a a", "a"),
        ("a b c a", "a"),
        ("a b b a", "b"),
        ("A is a is A", "a")
    ]
)
def test_repeated_word(text, repeated):
    assert repeated_word(text) == repeated
