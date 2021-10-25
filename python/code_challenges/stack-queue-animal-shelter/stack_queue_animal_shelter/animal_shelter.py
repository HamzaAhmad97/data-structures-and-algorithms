class Dog:
    """
    A class representing a dog.
    """
    TYPE = 'Dog'

    def __init__(self, name, age):
        """
        The constructor method, initialize the name, age, and the next properties.

        Args:
            name (str): Dog's name.
            age (int): Dog's age.
        """
        self.name = name
        self.age = age
        self.next = None

    def __str__(self):
        """
        Construct a string representation of the dog.

        Returns:
            str: Dog representation as a string.
        """
        return f"Name: {self.name} | Age: {self.age} | Type: {Dog.TYPE} | Next: {self.next}"


class Cat:
    """
    A class representing a cat.
    """
    TYPE = 'Cat'

    def __init__(self, name, age):
        """
        The constructor method, initialize the name, age, and the next properties.

        Args:
            name (str): Cat's name.
            age (int): Cat's age.
        """
        self.name = name
        self.age = age
        self.next = None

    def __str__(self):
        """
        Construct a string representation of the cat.

        Returns:
            str: Cat representation as a string.
        """
        return f"Name: {self.name} | Age: {self.age} | Type: {Cat.TYPE} | Next: {self.next}"


class NoSuchTypeEexception(Exception):
    """
    An exception that will get raised whne passing a type that is not supported or when dequeueing from an empty queue.

    Args:
        Exception (class): The Exception class.
    """
    pass


class AnimalShelter():
    """
    Animal shelter class.
    """

    def __init__(self):
        """
        The constructor method, define the front and the rear for the dog and cat queues.
        """
        self.dog_front = None
        self.dog_rear = None
        self.cat_front = None
        self.cat_rear = None

    def enqueue(self, animal):
        """
        Add or push a cat or dog object to the queue.

        Args:
            animal (Dog/Cat): The animal object to be enqueued.
        """
        if animal.TYPE == 'Dog':

            if not self.dog_front:
                self.dog_front = animal
                self.dog_rear = animal
                return
            self.dog_rear.next = animal
            self.dog_rear = animal

        elif animal.TYPE == 'Cat':
            if not self.cat_front:
                self.cat_front = animal
                self.cat_rear = animal
                return
            self.cat_rear.next = animal
            self.cat_rear = animal

    def dequeue(self, pref):
        """
        Get and remove the animal object only if it is a cat or a dog, and thier respective stacks are not empty.

        Args:
            pref (str): The type of the animal to be returned.

        Raises:
            NoSuchTypeEexception: If type or queue is empty.

        Returns:
            Cat/Dog : A cat or a dog object if exists.
        """

        try:
            if pref.title() == 'Dog':
                temp = self.dog_front
                self.dog_front = temp.next
                temp.next = None
                return temp
            elif pref.title() == 'Cat':
                temp = self.cat_front
                self.cat_front = temp.next
                temp.next = None
                return temp
            else:
                raise NoSuchTypeEexception
        except:
            raise NoSuchTypeEexception
