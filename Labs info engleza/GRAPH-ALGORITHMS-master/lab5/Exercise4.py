from UndirectedGraph import Graph
import queue

def BFS(graph,start):
    q = queue.Queue()
    accessed = set()
    q.put(start)
    accessed.add(start)
    while not q.empty():
        x = q.get()
        for y in graph.parse_neighbours(x):
            if y not in accessed:
                q.put(y)
                accessed.add(y)
    return accessed


def get_connected_components(graph):
    components = []
    vertices = graph.parse_vertices()
    visited = set()
    for x in vertices:
        if x not in visited:
            accessible = BFS(graph,x)
            visited = visited.union(accessible)
            component = create_graph(graph,accessible)
            components.append(component)
    return components

def create_graph(initialGraph,validVertices):
    result_graph = Graph(0)
    for vertex in validVertices:
        result_graph.add_vertex(vertex)
    for vertex in validVertices:
        for neighbour in initialGraph.parse_neighbours(vertex):
            if not result_graph.is_edge(vertex,neighbour):
                result_graph.add_edge(vertex,neighbour,initialGraph.get_cost(vertex,neighbour))
    return result_graph

