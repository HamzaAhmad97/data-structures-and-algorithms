# Linked List Insertion

[Latest open pull request](https://github.com/HamzaAhmad97/data-structures-and-algorithms/pull/24)

In this challenge I added the append, insert_after, insert_before and the delete_node methods, to append a node to the end of a linked list, insert a node after another node given its value, insert a node before another node given its value, and delete a node given its value respectively.

## Whiteboard Process

* Append()

![](https://www.notion.so/mock-c71027349a444331b62b41e0f1a47e1e#06886de6675b4f9b9b869870111802f6)

* Insert_after()

![](https://drive.google.com/file/d/1061twwke--JaCeAxdMaW4uuCZvPQsh6C/view?usp=sharing)

* Insert_before()

![](https://lh3.googleusercontent.com/WX1z0GOVke-6DsAdcy1LS1JOY56XILvnBf6JtgJ3hWELaUdPLKN8wHhLufa-96ojuQwgsYRV31GCjbirP3z8Z93uhvXkmy1oTfM23ELwWlgsIwrjB1t4oyXRjOa8u66nnR0yoBUAMCPNpv9JatNT1NnOvBT_4xUyFBFp_v9WkGmfhnqhoEIAbQMslYgwXLqnWy-c7WTjnvHHp8S3PdffvbSUYrE3ptOGcMB8OszO_0WQmmIQl9DWBSEMZdsCtk9FKHWNx9fVJnrakUgKOofUhHq521avINEESyWK8PSGnPZIH1oykEubYO1ZUAj9NjSCF-wBLRk9B7gXojGKg4KZe8aoZT-56hHofz5rVgwM1hDxsLopgCTRj5CSyacFAV-BBwDRL2-wpZlrJuRLLoVYVBzP_xfo7mZWle4u4UnYGlsBE6RSiS8xtSM4WEBUHkzHytzldOKf_8x5nr2wbact3oRu9C8QhUdM_UaANGm7OuSF4CQEgX2djTDj2UySKKC2kWjv-YyvJc2UqDTMKcHnbjQ060gZ7uFVEyz7vX65fdGcONlWnCA8h1UoATI5P2EzReQ6kqUI1zAY8Kq--yz8-jpBiOM7uAvcSO3qb8veSNH43k6Qdyv-Cgi9Qo-Fq4jG_esep75MCV3alTjsyd8etqXyIlW_QPwXYYpbB9UhpD5kQz9PVrsy1HwSO-3Nc6RNl_MAg6B7nCR-1ajqxXzlJCdp=w1275-h803-no?authuser=0)

* Delete_node()

![](https://drive.google.com/file/d/1c0dqH3a9pWJnOEjTAerLccCbEOX5VEMp/view?usp=sharing)

## Approach & Efficiency

I followed the simplest approach with maximum effeciency for all of the new methods.

| Method    | Summary                                                                                 | Big O Time | Big O Space | Example             |
| :-------- | :-------------------------------------------------------------------------------------- | :--------: | :---------: | :------------------ |
| append    | add a new node to the end of a linked list                                                 |    O(N)    |    O(1)     | myList.append(99)   |
| insert_after  | insert a node after another node given its value                                    |    O(n)    |    O(1)     | myList.insert_after(80,99) |
| insert_before | insert a node before another node given its value                                   |    O(n)    |    O(1)     | myList.insert_before(80,99)  |
| delete_node | delete a node given its value                                                |    O(n)    |    O(1)     | myList.delete_node(99)  |

## Solution

```python
ll = LinkedList()
ll.insert('a')
ll.append('x')
ll.insert_before('x', 'b')
ll.insert_after('b','c')
ll.delete_node('x')
print(ll.to_string())
```
