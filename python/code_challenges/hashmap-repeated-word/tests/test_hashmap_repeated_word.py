import pytest
from hashmap_repeated_word import __version__
from hashmap_repeated_word.hashtable_repeated_word import repeated_word, InvalidNumberOfKeysError

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
    """
    Test if repeated_word returns the correct word given that the number of words is valid.
    """
    assert repeated_word(text) == repeated

@pytest.mark.parametrize(
    "text",
    [
        "a",
        "aa",
        "",
    ]
)
def test_repeated_word_raises_an_exception_on_invalid_number_of_words(text):
    """
    Test if repeated_words raises an exception if the number of words is invalid.
    """
    with pytest.raises(InvalidNumberOfKeysError):
        repeated_word(text)

def test_repeated_word_returns_None_if_no_repeated_word_is_found():
    """
    Test if repeated_words returns None if it does not find a word that occurs more than once.
    """
    assert not repeated_word("a b c")