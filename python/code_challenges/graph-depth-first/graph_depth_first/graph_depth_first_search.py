from collections import deque
import os


class Vertex:
    """
    A class representing a container.
    """

    def __init__(self, value):
        """
        The constructor method for the vertex class. Initializes the property value.
        Args:
            value (any): The value to be stored in a vertex.
        """
        self.value = value


class Queue:
    """
    A class representing a queue which is a data structure that utilizes the first in first out access method.
    """

    def __init__(self):
        """
        The constructor method of the queue class. Initializes the dq property to a deque instance.
        """
        self.dq = deque()

    def enqueue(self, value):
        """
        Push or add a value after storing it in a vertex to a queue.
        Args:
            value (any): The value to be pushed to the queue in a vertex instance.
        """
        self.dq.appendleft(value)

    def dequeue(self):
        """
        Get or pop the front or the very first element in a queue.
        """
        return self.dq.pop()

    def __len__(self):
        """
        Overwrite the len method so that the queue has a length property.
        Returns:
            int: A representation of the length of a queue.
        """
        return len(self.dq)


class Stack:
    """
    A data structure that utilitzes the first in last out access method.
    """

    def __init__(self):
        """
                The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
                """
        self.dq = deque()

    def push(self, value):
        """
        Push a value in a node on top of a stack.
        Args:
            value (any): The value to be pushed on top of the stack.
        """
        self.dq.append(value)

    def pop(self):
        """
        Pop or get the very last item in a stack.
        """
        return self.dq.pop()

    def peek(self):
        return self.dq[-1]

    def is_empty(self):
        return True if not len(self.dq) else False


class Edge:
    """
    A class representing a connection between two enteties or vertices.
    """

    def __init__(self, vertex, weight):
        """
        The constructor method of edge class. Initializes the vertex and the weight properties.
        Args:
            vertex (Vertex): A vertex instance.
            weight (int): The weight given to a connection.
        """
        self.vertex = vertex
        self.weight = weight


class Graph:
    """
    A class representing a data structure that consists of a set of vertices that are connected to each other.
    """

    def __init__(self):
        """
        A constructor method of the class Graph. Initialize the adjacency_list property.
        """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
        Add a node to a graph.
        Args:
            value (any): The value to be stored in a vertex to be added to a graph.
        Returns:
            vertex: The newly added vertex instance.
        """
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        """
        Get the number of vertices in a graph.
        Returns:
            int: The number of nodes or vertices in a graph.
        """
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """
        Create a connection between two vertices in a graph with a weight.
        Args:
            start_vertex (vertex): The starting vertex.
            end_vertex (vertex):  The ending vertex.
            weight (int, optional): The weight or strenght of connection. Defaults to 0.
        Raises:
            KeyError: If either the start or the end vertex do not exist in the graph.
        """
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Return all the nodes in a graph.
        Returns:
            list: A list of all the vertices in a graph.
        """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Get all the neighbors of the vertex vertex.
        Args:
            vertex (vertex): The vertex to get its neighbors.
        Returns:
            list: A list of all the adjacent vertices to a given vertex instance.
        """
        return self.__adjacency_list.get(vertex, [])

    def depth_first_search(self, start_node):
        visited = []

        def traverse(start_node):
            if start_node in visited:
                return
            visited.append(start_node)
            neighbors = [edge.vertex for edge in self.get_neighbors(
                start_node) if edge.vertex not in visited]
            for neighbor in neighbors:
                traverse(neighbor)
        traverse(start_node)
        return [v.value for v in visited]


if __name__ == "__main__":
    os.system('clear')
    route = Graph()
    x = route.add_node("A")
    a = route.add_node("a")
    b = route.add_node("b")
    c = route.add_node("c")
    d = route.add_node("d")
    e = route.add_node("e")
    f = route.add_node("f")
    g = route.add_node("g")
    h = route.add_node("h")

    route.add_edge(a, b)
    route.add_edge(a, d)

    route.add_edge(b, a)
    route.add_edge(b, d)
    route.add_edge(b, c)

    route.add_edge(c, b)
    route.add_edge(c, g)

    route.add_edge(d, a)
    route.add_edge(d, b)
    route.add_edge(d, f)
    route.add_edge(d, h)
    route.add_edge(d, e)

    route.add_edge(e, d)

    route.add_edge(f, d)
    route.add_edge(f, h)

    route.add_edge(g, c)

    route.add_edge(h, d)
    route.add_edge(h, f)

    print(route.depth_first_search(b))