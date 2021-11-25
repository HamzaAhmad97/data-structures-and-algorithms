# Graphs

A graph is a data structure that consists of nodes or vertices that are connected to each other via edges which are just connecting segments. A node can have what is known as a neighbor, which is any node that is adjacent to that node. The degree of a vertex is the number of edges connected to that vertex or node.

## Pull Request

[Latest open pull request](https://github.com/HamzaAhmad97/data-structures-and-algorithms/pull/41)

## Challenge

The current challenge requires implementing a Graph class along with its methods like add_node, add_edge and get_nodes.

## Approach & Efficiency

The adjacency list representation of a graph has been used, we define a dictionary to be the actual adjacency list, so the methods add_node, add_edge, get_nodes and size rely on the process of accessing and modifying key/value pairs which results in O(1) complexity. When it comes to space, it is O(N) in the worst case.

For the breadth first search part, the time complexity is O(N^2) and space complexity is O(N).

## API

```python
graph = Graph()
vertex_a = graph.add_node("a")
vertex_b = graph.add_node("b")
graph.add_edge(vertex_a, vertex_b, weight = 50)
graph.size() # 2
graph.get_nodes() # ["a", "b"]
graph.get_neighbors(graph_b) # [vertex_a]
graph.breadth_first_search(vertex_a) # ["a", "b"]
```
