# Linked List Insertion

In this challenge I added the append, insert_after, insert_before and the delete_node methods, to append a node to the end of a linked list, insert a node after another node given its value, insert a node before another node given its value, and delete a node given its value respectively.

## Whiteboard Process

* Append()

![](https://drive.google.com/file/d/1FPkbrfEJ6iK-EraJ7KDdGi0bakhm6QIl/view?usp=sharing)

* Insert_after()

![](https://drive.google.com/file/d/1061twwke--JaCeAxdMaW4uuCZvPQsh6C/view?usp=sharing)

* Insert_before()

![](https://drive.google.com/file/d/1KzBYfm-8pRYjR_vAgJUlAmEUjn2eDdzB/view?usp=sharing)

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
