from dependency_classes import Hashtable

def left_join(ht1, ht2):
    container = []
    for itm in ht1._Hashtable__buckets:
        if itm:
            current = itm.head
            while current:
                hashcode = ht1._Hashtable__hash(current.value[0])
                cur = ht2._Hashtable__buckets[hashcode].head
                while cur:
                    if cur.value[0] == current.value[0]:

                        container.append((current.value[0], (current.value[1], cur.value[1])))
                    cur = cur._next
                current = current._next
    return container


if __name__ == "__main__":
    ht1 = Hashtable(100)
    ht2 = Hashtable(100)
    ht1.add("a", "11")
    ht1.add("b", "22")
    ht1.add("c", "33")

    ht2.add("b", "2")
    ht2.add("c", "3")
    ht2.add("d", "4")
    ht2.add("a", "4")
    ht2.add("a", "dd")
    ht2.add("a", "dddd")
    left_join(ht1,ht2)
