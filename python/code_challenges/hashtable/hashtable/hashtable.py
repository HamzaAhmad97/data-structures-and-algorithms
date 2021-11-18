class Node:
    def __init__(self, value, _next = None):
        self.value = value
        self._next = _next
    def __str__(self):
        return f"{self.value}"



if __name__ == "__main__":
    ht = Hashtable()
    print(ht.get_hash("something"))