import pytest

from graph.graph import  Graph, Vertex

def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

def test_breadth_first_search_a():
    expected = ['a', 'b', 'c', 'e', 'd']
    gph = Graph()
    a = gph.add_node("a")
    b = gph.add_node("b")
    c = gph.add_node("c")
    d = gph.add_node("d")
    e = gph.add_node("e")
    gph.add_edge(a,b,weight=1)
    gph.add_edge(a,c,weight=1)
    gph.add_edge(c,d,weight=1)
    gph.add_edge(a,e,weight=1)
    gph.add_edge(b,e,weight=1)
    assert gph.breadth_first_search == expected

