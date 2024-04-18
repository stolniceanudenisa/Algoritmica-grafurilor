from Graph import Graph

def BronKebosch(graph, temporaryResult, candidates, excludedSet, maximumClique):
    '''
    Finds the clique of maximum size in the graph.
    input:
        - undirected graph
        - lists temporaryResult, candidates, excludedSet, maximumClique
    output:
        - 
    '''
    if len(candidates) == 0 and len(excludedSet) == 0:
        # a maximal clique was found (temporary Result)
        # compare the size
        print(temporaryResult)
        if len(temporaryResult) > len(maximumClique):
            maximumClique.clear()
            maximumClique.extend(temporaryResult)
    
    for vertex in candidates:
        # add the vertex to the temporary result
        temporaryResult.append(vertex)

        # remove the non-neighbours from the candidates (prepare the new candidates list for the next call)
        remainingVerticesCandidates = []
        for neighbour in graph.parseOutboundEdges(vertex):
            if neighbour in candidates:
                remainingVerticesCandidates.append(neighbour)

        # remove the non-neighbours from the excludedSet (prepare the new excludedSet list for the next call)
        remainingVerticesExcludedSet = []
        for neighbour in graph.parseOutboundEdges(vertex):
            if neighbour in excludedSet:
                remainingVerticesExcludedSet.append(neighbour)

        BronKebosch(graph, temporaryResult, remainingVerticesCandidates, remainingVerticesExcludedSet, maximumClique)

        # after the recursive call, remove the vertex from the candidates and add it to the excludesSet
        candidates.remove(vertex)
        excludedSet.append(vertex)
        temporaryResult.remove(vertex)

def maximumClique(graph):
    '''
    Finds the clique of maximum size in the graph.
    input:
        - undirected graph
    output:
        - the vertices from the maximumClique as list
    '''
    temporaryResult = []
    candidates = []
    excludedSet = []
    maximumClique = []

    for vertex in graph.parseVertices():
        candidates.append(vertex)

    BronKebosch(graph, temporaryResult, candidates, excludedSet, maximumClique)

    subgraph = Graph(0, "undirected")

    for vertex in maximumClique:
        subgraph.addVertex(vertex)

    for edge in graph.parseEdges():
        if subgraph.isVertex(edge[0]) and subgraph.isVertex(edge[1]):
            subgraph.addEdge(edge[0], edge[1])

    return maximumClique, subgraph


def test():
    graph = Graph(6, "undirected")
    graph.addEdge(0, 1, 0)
    graph.addEdge(0, 4, 0)
    graph.addEdge(1, 4, 0)
    graph.addEdge(1, 2, 0)
    graph.addEdge(3, 4, 0)
    graph.addEdge(3, 5, 0)
    graph.addEdge(4, 5, 0)
    graph.addEdge(1, 3, 0)
    graph.addEdge(1, 5, 0)

    print(graph.parseVertices())
    result, subgraph = maximumClique(graph)
    print(result)
    print(subgraph.componentAsString())

