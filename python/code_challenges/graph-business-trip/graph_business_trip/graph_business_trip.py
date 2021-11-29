from dependancy_classes import Graph, Stack

def business_trip(graph, cities):
    start_city = cities[0]
    stack = Stack()
    stack.push(start_city)
    while len(stack.dq):
        last_visited = stack.pop()
        print(last_visited)
        neighbors = graph.get_neighbors(last_visited)
        for neighbor in neighbors:
            if neighbor.vertex not in stack.dq:
                stack.push(neighbor.vertex)





if __name__ == "__main__":
    route = Graph()
    pandora = route.add_node("Pandora")
    metroville = route.add_node("Metroville")
    arendelle = route.add_node("Arendelle")
    monstropolis = route.add_node("Monstropolis")
    naboo = route.add_node("Naboo")
    narnia = route.add_node("Narnia")

    route.add_edge(pandora, arendelle, weight=150)
    route.add_edge(pandora, metroville, weight=82)

    route.add_edge(arendelle, pandora, weight=150)
    route.add_edge(arendelle, metroville, weight=99)
    route.add_edge(arendelle, monstropolis, weight=42)

    route.add_edge(metroville, pandora, weight=82)
    route.add_edge(metroville, arendelle, weight=99)
    route.add_edge(metroville, monstropolis, weight=105)
    route.add_edge(metroville, narnia, weight=37)
    route.add_edge(metroville, naboo, weight=26)

    route.add_edge(monstropolis, arendelle, weight=42)
    route.add_edge(monstropolis, metroville, weight=105)
    route.add_edge(monstropolis, naboo, weight=73)

    route.add_edge(narnia, metroville, weight=37)
    route.add_edge(narnia, naboo, weight=250)

    #business_trip(route, [pandora, arendelle])
    # s = Stack()
    # s.push(arendelle)
    # print(route.get_neighbors(pandora)[0].vertex in s.dq)
    