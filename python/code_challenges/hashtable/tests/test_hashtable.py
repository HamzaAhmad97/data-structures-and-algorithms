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
    
