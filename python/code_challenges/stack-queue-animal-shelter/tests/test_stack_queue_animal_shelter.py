from stack_queue_animal_shelter import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def animal_shelter():
    return AnimalShelter()

@pytest.fixture
def dog():
    return Dog("Coco", 3)

@pytest.fixture
def cat():
    return Cat("Meme", 2)

def test_enqueue_one_a_dog(animal_shelter,dog):
    expected = "Coco"
    animal_shelter.enqueue(dog)
    actual = animal_shelter.dequeue('dog').name
    assert actual == expected

def test_enqueue_one_a_cat(animal_shelter,cat):
    expected = "Meme"
    animal_shelter.enqueue(cat)
    actual = animal_shelter.dequeue('cat').name
    assert actual == expected

def test_dequeue_raises_an_exception_if_type_is_empty(animal_shelter):
    with pytest.raises(NoSuchTypeEexception, match='Type specified does not exist.'):
        animal_shelter.dequeue('dog')

def test_dequeue_raises_an_exception_if_type_is_other_than_a_dog_or_cat(animal_shelter,cat):
    animal_shelter.enqueue(cat)
    with pytest.raises(NoSuchTypeEexception, match='Typr specified is not a cat nor a dog.'):
        animal_shelter.dequeue('horse')
