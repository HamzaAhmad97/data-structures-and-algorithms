import pytest
from hashtable import __version__
from hashtable.hashtable import Hashtable

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def hashtable():
    return Hashtable()

def test_hashtable_contains_bare_value(hashtable):
    hashtable.add("name","Hamza")
    assert hashtable.contains("name")
    
def test_hashable_contains_pair_in_a_linked_list(hashtable):
    hashtable.add("name", "Hamza")
    hashtable.add("name", "Alan")
    assert hashtable.contains("name")

def test_hashtable_add(hashtable):
    hashtable.add("name", "Einstein")
    assert hashtable.contains('name')

def test_hashable_add_same_key(hashtable):
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
    assert hashtable._Hashtable__hash(key) == hashcode
