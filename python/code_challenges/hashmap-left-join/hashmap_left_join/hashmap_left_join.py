from hashmap_left_join.dependency_classes import Hashtable
#from dependency_classes import Hashtable

def left_join(ht1, ht2):

    container = []
    for itm in ht1._Hashtable__buckets:
        if itm:
            current = itm.head
            while current:
                hashcode = ht1._Hashtable__hash(current.value[0])
                cur = ht2._Hashtable__buckets[hashcode]
                if not cur:
                    container.append((current.value[0], (current.value[1], None)))
                    current = current._next
                    continue
                cur = cur.head
                while cur:
                    if cur.value[0] == current.value[0]:

                        container.append((current.value[0], (current.value[1], cur.value[1])))
                    cur = cur._next
                current = current._next
    return container


if __name__ == "__main__":
    ht1 = Hashtable(100)
    ht2 = Hashtable(100)
    ht1.add("a", "a")
    ht1.add("b", "b")
    ht1.add("c", "c")

    ht2.add("a", "1")
    ht2.add("a", "2")
    ht2.add("b", "1")
    print(left_join(ht1,ht2))
