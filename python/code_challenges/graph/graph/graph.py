from collections import deque


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
        self.dq.appendLeft(value)

    def dequeue(self):
        """
        Get or pop the front or the very first element in a queue.
        """
        self.dq.pop()

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
        self.dq.pop()


class Edge:
    """
    A class representing a connection between two enteties or vertices.
    """
    def __init__(self, vertex, weight):
        """
        The constructor method of edge class. Initializes the vertex and the weight properties.

        Args:
            vertex (Vertex): [description]
            weight ([type]): [description]
        """
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
    Initalization for a hashmap to hold the vertices
    """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ """
        return self.__adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)

            neighbors = self.get_neigbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)