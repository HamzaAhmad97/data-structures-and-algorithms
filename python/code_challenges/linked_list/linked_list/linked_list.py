class Node:

    def __init__(self, value=None):
        self.value = value
        self.next_ = None

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self): 
        self.__head = None

    def insert(self, value):
        new_node = Node()
        new_node.value = value
        new_node.next_ = self.__head
        self.__head = new_node

    def includes(self, value):
        current = self.__head
        while current != None:
            if current.value == value:
                return True
            current = current.next_
        return False

    def to_string(self):
        current = self.__head
        representation = ""
        while current != None:
            representation += f"{{{current.value}}} -> "
            if current.next_ == None:
                representation += f"Null"
            current = current.next_
        return representation
