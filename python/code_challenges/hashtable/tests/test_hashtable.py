import pytest
from hashtable import __version__
from hashtable.hashtable import Hashtable

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def hashtable():
    """
    An empty hashtable instance.

    Returns:
        Hashtable: an empty hashtable instance.
    """
    return Hashtable()

def test_hashtable_contains_bare_value(hashtable):
    """
    Test if contains method return the correct value corresponding to a key if it is the only one stored at that index.

    """
    hashtable.add("name","Hamza")
    assert hashtable.contains("name")
    
def test_hashable_contains_pair_in_a_linked_list(hashtable):
    """
    Test if contains method returns True if a key exists but it is not unique.

    """
    hashtable.add("name", "Hamza")
    hashtable.add("name", "Alan")
    assert hashtable.contains("name")

def test_hashtable_add(hashtable):
    """
    Test the add method with a new key.

    """
    hashtable.add("name", "Einstein")
    assert hashtable.contains('name')

def test_hashable_add_same_key(hashtable):
    """
    Test add method when the key already exists.

    """
    hashtable.add("a", "a")
    hashtable.add("a", "a")
    assert hashtable.contains("a")

@pytest.mark.parametrize(
    "key,hashcode",
    [
       ("a", 679),
       ("ab", 341),
       ("hello", 652),
       ("something000", 658)
    ]
)
def test_hashtable_hash(key,hashcode, hashtable):
    """
    Test hash method returns the correct hashtable.

    """
    assert hashtable._Hashtable__hash(key) == hashcode
def test_hashtable_get_returns_value(hashtable):
    """
    Test get method when the key is unique at its index.

    """
    expected = "Hamza"
    hashtable.add("name", "Hamza")
    assert hashtable.get("name") == expected

def test_hashtable_get_returns_correct_last_value(hashtable):
    """
    Test get method when the key is not unique.

    """
    expected = "Alan"
    hashtable.add("name", "Hamza")
    hashtable.add("name", "Alan")
    assert hashtable.get("name") == expected

def test_hashtable_get_returns_none_if_key_does_not_exist(hashtable):
    """
    Test if get method returns None if the key does not exist.

    """
    assert not hashtable.get("name")

def test_hashtable_contains_returns_false_if_key_does_not_exist(hashtable):
    """
    Test if contains method returns False if the key does not exist in the hashtable.

    """
    assert not hashtable.contains("name")

def test_hashtable_handles_collisions(hashtable):
    """
    Test if the add method handles collisions.

    """
    expected = "grey"
    hashtable.add("color", "red")
    hashtable.add("color", "blue")
    hashtable.add("color", "grey")
    assert hashtable.get("color") == expected