class Dog:
    TYPE = 'Dog'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Type: {Dog.TYPE} | Next: {self.next}"


class Cat:
    TYPE = 'Cat'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Type: {Cat.TYPE} | Next: {self.next}"


class NoSuchTypeEexception(Exception):
    pass


class Queue():

    def __init__(self):
        """
        The constructor method for the class Queue. Initialize front and rear.
        """
        self.dog_front = None
        self.dog_rear = None
        self.cat_front = None
        self.cat_rear = None

    def enqueue(self, animal):

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
        except:
            raise NoSuchTypeEexception
