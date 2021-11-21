import re
import os

class Node:
    def __init__(self, value, _next = None):

        self.value = value
        self._next = _next
    def __str__(self):

        return f"{self.value}"

class LinkedList:

    def __init__(self):

        self.head = None
    def insert(self,value):

        self.head = Node(value, self.head)
    def __str__(self):

        current = self.head
        representation = ""
        while current != None:
            representation += f"{{{current}}} -> "
            if current._next == None:
                representation += f"Null"
            current = current._next
        return representation

class Hashtable:

    def __init__(self, size = 1024):

        self.__size = size
        self.__buckets = [None for _ in range(size)]

    def __hash(self, key):

        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):

        index = self.__hash(key)

        if not self.__buckets[index]:
            self.__buckets[index] = LinkedList()
        val = [key, value]
        self.__buckets[index].insert(val)

    def get(self, key):
        index = self.__hash(key)
        value = self.__buckets[index]
        if value:
            if isinstance(value, LinkedList):
                current = value.head
                while current:
                    if current.value[0] == key:
                        return current.value[1]
                    current = current._next
            return value
        return None
                
    def contains(self, key):

        index = self.__hash(key)
        value = self.__buckets[index]
        if value:
            if isinstance(value, LinkedList):
                current = value.head
                while current:
                    if current.value[0] == key:
                        return True
                    current = current._next
            return True
        return False

class InvalidNumberOfKeysError(Exception):
    pass

def repeated_word(text):
    ht = Hashtable()
    words = list(map(lambda word : word.lower(), re.findall(r"\w+", text)))
    if len(list(words)) <= 1:
        raise InvalidNumberOfKeysError("String provided contains an invalid number of keys.")
    for word in words:
        if ht.contains(word):
            return word
        ht.add(word, None)


if __name__ == "__main__":
    os.system('clear')
    text = "a a"
    ht = Hashtable()
    print(repeated_word(text))
    print("-------------")
   
    