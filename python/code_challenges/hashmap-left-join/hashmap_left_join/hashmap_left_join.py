
from hashmap_left_join.dependency_classes import Hashtable
#from dependency_classes import Hashtable

def left_join(ht1, ht2):
    """
    A function that accepts two hashtables and performs left join and adds the result to a list.

    Args:
        ht1 (Hashtable): The left hashtbale instance.
        ht2 (Hashtable): The right hashtable instance.

    Returns:
        list: The values after left join.
    """
    container = []

    for node in ht1.get_nodes():
        ctr = 0
        for item in ht2.get_nodes():
            if item.value[0] == node.value[0]:
                container.append((node.value[0], (node.value[1], item.value[1])))
                ctr += 1
        if not ctr:
            container.append((node.value[0], (node.value[1], None)))
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
