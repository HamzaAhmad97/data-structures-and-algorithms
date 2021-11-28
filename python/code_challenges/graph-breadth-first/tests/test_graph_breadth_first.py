from graph_breadth_first import __version__
from graph_breadth_first.graph_breadth_first import Graph

def test_version():
    assert __version__ == '0.1.0'

def test_breadth_first_search_a():
    expected = ['a', 'b', 'c', 'e', 'd']
    gph = Graph()
    a = gph.add_node("a")
    b = gph.add_node("b")
    c = gph.add_node("c")
    d = gph.add_node("d")
    e = gph.add_node("e")
    # directed graph
    gph.add_edge(a,b,weight=1)
    gph.add_edge(a,c,weight=1)
    gph.add_edge(c,d,weight=1)
    gph.add_edge(a,e,weight=1)
    gph.add_edge(b,e,weight=1)
    assert gph.breadth_first_search(a) == expected

def test_breadth_first_search_b():
    expected = ['d', 'c', 'a', 'b', 'e']
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
    # now it becomes an undirected graph
    gph.add_edge(b,a,weight=1)
    gph.add_edge(c,a,weight=1)
    gph.add_edge(d,c,weight=1)
    gph.add_edge(e,a,weight=1)
    gph.add_edge(e,b,weight=1)
    assert gph.breadth_first_search(d) == expected

def test_breadth_first_search_method_c():
    expected = ['a']
    gph = Graph()
    a = gph.add_node("a")
    assert gph.breadth_first_search(a) == expected