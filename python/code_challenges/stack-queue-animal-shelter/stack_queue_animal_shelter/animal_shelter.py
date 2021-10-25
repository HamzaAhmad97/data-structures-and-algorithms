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
