from dependancy_classes import Graph, Stack
import os

def business_trip(graph, cities):


    start_city = cities[0]
    visited = []
    stack = Stack()
    stack.push(start_city)
    c = 0
    while not stack.is_empty():
        # visited : monstroplis -> naboo -> metroville ->
        # stack : monstroplis -> arendelle -> metroville -> naboo -> narnia -> metroville ->
        unvisited_neighbors = []
        last_visited = stack.peek()
        visited.append(last_visited)
        print(last_visited.value)
        neighbors = [edge.vertex for edge in graph.get_neighbors(last_visited)]
        for neighbor in neighbors:
            if neighbor not in visited:
                unvisited_neighbors.append(neighbor)
        print("unvisited:  ",[v.value for v in unvisited_neighbors])
        if unvisited_neighbors:
            for unvisited in unvisited_neighbors:
                stack.push(unvisited)
        else:
            stack.pop()
        print("stack:  ",[v.value for v in stack.dq])
        print("visited:  ",[v.value for v in visited])
        print("*******************")
        c += 1

    return [v.value for v in visited]

def trip(route, city):
    def depth_first_search(city):
        unvisited_neighbors = []
        if not stack.is_empty():
            return
        last = stack.peek()
        visited.append(last)

        neighbors = [edge.vertex for edge in route.get_neighbors(last)]
        for neighbor in neighbors:
            if neighbor not in visited:
                unvisited_neighbors.append(neighbor)
        if unvisited_neighbors:
            for unvisited in unvisited_neighbors:
                stack.push(unvisited)
        else:
            stack.pop()
        return depth_first_search(last)
    stack = Stack()
    visited = []
    stack.push(city)
    depth_first_search(city)
    return visited

visited = set()
def depth_first_search(graph, start):
    unvisted_neighbors = []
    visited.add(start)
    print(start.value)
    neighbors = [edge.vertex for edge in route.get_neighbors(start)]
    for neighbor in neighbors:
        if neighbor not in visited:
            unvisted_neighbors.append(neighbor)
    for neighbor in unvisted_neighbors:
        depth_first_search(graph, neighbor)
    print([v.value for v in visited])

if __name__ == "__main__":
    os.system('clear')
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

    route.add_edge(naboo, narnia, weight=250)
    route.add_edge(naboo, metroville, weight=26)
    route.add_edge(naboo, monstropolis, weight=73)
    
    #print(business_trip(route, [monstropolis, arendelle]))
    ##print(trip(route, pandora ))
    # s = Stack()
    # s.push(arendelle)
    # print(route.get_neighbors(pandora)[0].vertex in s.dq)
    print(depth_first_search(pandora, arendelle))
