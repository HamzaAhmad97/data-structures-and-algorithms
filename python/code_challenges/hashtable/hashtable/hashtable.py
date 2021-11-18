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



if __name__ == "__main__":
    ht = Hashtable()
    print(ht.get_hash("something"))