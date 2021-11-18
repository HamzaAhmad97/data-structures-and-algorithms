# Hashtable

Hashing is the process of taking a string and converting it into another type of value that can be used to for other purposes like determining the index of an array in the case of a hashtable. When we refer to what is stored or contained in each index of the array, it is called a bucket, and it could contain multiple key/ value pairs in a linked list if a collision occurs, and collisions themselves is what happens when more than one key gets hashed to the same location of the hashtable.

## Pull Request

[Latest open pull request](https://github.com/HamzaAhmad97/data-structures-and-algorithms/pull/37).

## Challenge

This challenge requires implementing a Hashtable class along with its methods like add, get, contains, and hash. Thsi also requires defining other classes that hashtables depend on like LinkedList and Node classes.

## Approach & Efficiency

Time complexity is brought to minumum here since adding to a hashtable only requires doing some simple calculations in order to convert or get a hashcode from a key string then it uses fast list indexing to store values, and if multiple keys share the same index in the array under the hood, it will use linked list insertion which also happens within constant time, so our Big O for time is O(1).

When it comes to space complexity, we will have to create a list of a particular size, so it is O(n). Bear in mind that methods like get and contains have time complexity of O(n) since they might need to traverses a linked list to find a key/ value pair.

## API

```python
ht = Hashtable(size = 1024)
ht.add(key = "color", value = "gray") # adds the color: gray key/value pair to the hashtable ht.
ht.get(key = "color") # "gray" -> returns the latest value corresponding to the provided key.
ht.contains("color") # True -> True if key exists in the hashtable, False otherwise.
```
