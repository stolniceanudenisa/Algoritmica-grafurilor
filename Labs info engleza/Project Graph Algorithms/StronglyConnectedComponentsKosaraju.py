from Graph import Graph

def createStackProcessedByDFS(graph, startVertex, visited, stackProcessed):
    '''
    Creates the stackProcessed by adding each vertex when it has no more outbound neighbours left.
    In order to do that, it performs a deep-first search on a graph with a given startVertex.
    input:
        - Graph graph
        - int startVertex
        - list visited
        - list stackProcessed
    output: -
    '''
    # mark the current node as visited
    visited.append(startVertex)
    for neighbour in graph.parseOutboundEdges(startVertex):
        if neighbour not in visited:
            createStackProcessedByDFS(graph, neighbour, visited, stackProcessed)
    # after all neighbours have been visited, add the vertex to the stack
    stackProcessed.append(startVertex)

def getTransposedGraph(graph):
    '''
    Returns the transposed graph of a given graph.
    input: Graph graph
    output: Graph transposedGraph
    '''
    # create a new graph with the same number of vertices
    transposedGraph = Graph(graph.getNumberVertices(), "directed")

    for vertex in graph.parseVertices():
        for neighbour in graph.parseOutboundEdges(vertex):
            transposedGraph.addEdge(neighbour, vertex, 0)

    return transposedGraph

def createStronglyConnectedComponentByDFS(transposedGraph, newSCC, startVertex, visited):
    '''
    Creates a SCC as Graph object.
    In order to do that, it performs a deep-first search on a graph with a given startVertex.
    input:
        - Graph transposedGraph
        - Graph newSCC
        - int startVertex
        - list visited
    output: -
    '''
    # newSCC = Graph(0)
    visited.append(startVertex)
    for neighbour in transposedGraph.parseOutboundEdges(startVertex):
        if neighbour not in visited:
            # add the neighbour vertex to newSCC
            newSCC.addVertex(neighbour)
            # add the edge neighbour, startVertex) (because it is the transposed Graph) to newSCC
            newSCC.addEdge(neighbour, startVertex, 0)
            createStronglyConnectedComponentByDFS(transposedGraph, newSCC, neighbour, visited)

def findStronglyConnectedComponents(graph):
    '''
    Finds the strongly-connected components of a directed graph and returns the result as a list of Graph
    objects.
    input:
        - a directed graph
    output:
        - a list containing all strongly-connected components of the graph
    '''
    allStronglyConnectedComponents = []
    visited = []
    stackProcessed = []

    # create the stack processed, the first DFS performed
    for vertex in graph.parseVertices():
        if vertex not in visited:
            createStackProcessedByDFS(graph, vertex, visited, stackProcessed)
    
    # create the transposed graph
    transposedGraph = getTransposedGraph(graph)

    visited = []
    # find the strongly-connected components
    while len(stackProcessed) > 0:
        vertex = stackProcessed.pop()
        if vertex not in visited:
            # create a new SCC
            newSCC = Graph(0, "directed")
            # add the first vertex to it
            newSCC.addVertex(vertex)
            createStronglyConnectedComponentByDFS(transposedGraph, newSCC, vertex, visited)

            # if there are edges in the initial graph that were not added in the newConnectedComponent, add them
            for x in newSCC.parseVertices():
                for y in newSCC.parseVertices():
                    if newSCC.isEdge(x,y) == False and graph.isEdge(x,y) == True:
                        newSCC.addEdge(x, y, 0)

            # after the newSCC was created, add it to the list of all strongly-connected components
            allStronglyConnectedComponents.append(newSCC)

    return allStronglyConnectedComponents

# --------------------------------------------------- Tests ---------------------------------------------------

def printCCs(g):
    allCCs = findStronglyConnectedComponents(g)

    numberComponent = 0

    for cc in allCCs:
        numberComponent += 1
        message = ""
        message += "Component " + str(numberComponent) + ": "
        print(message)
        print(cc.componentAsString())
        print("\n")

def testFindCCs2():
    g1 = Graph(5, "directed") 
    g1.addEdge(1, 0, 9) 
    g1.addEdge(0, 2, 0) 
    g1.addEdge(2, 1, 0) 
    g1.addEdge(0, 3, 0) 
    g1.addEdge(3, 4, 0) 
    print ("SSC in first graph ")
    printCCs(g1)
    
    g2 = Graph(4, "directed") 
    g2.addEdge(0, 1) 
    g2.addEdge(1, 2) 
    g2.addEdge(2, 3) 
    print ("nSSC in second graph ")
    printCCs(g2) 
    
    
    g3 = Graph(7, "directed") 
    g3.addEdge(0, 1) 
    g3.addEdge(1, 2) 
    g3.addEdge(2, 0) 
    g3.addEdge(1, 3) 
    g3.addEdge(1, 4) 
    g3.addEdge(1, 6) 
    g3.addEdge(3, 5) 
    g3.addEdge(4, 5) 
    print ("nSSC in third graph ")
    printCCs(g3)
    
    g4 = Graph(11, "directed") 
    g4.addEdge(0, 1) 
    g4.addEdge(0, 3) 
    g4.addEdge(1, 2) 
    g4.addEdge(1, 4) 
    g4.addEdge(2, 0) 
    g4.addEdge(2, 6) 
    g4.addEdge(3, 2) 
    g4.addEdge(4, 5) 
    g4.addEdge(4, 6) 
    g4.addEdge(5, 6) 
    g4.addEdge(5, 7) 
    g4.addEdge(5, 8) 
    g4.addEdge(5, 9) 
    g4.addEdge(6, 4) 
    g4.addEdge(7, 9) 
    g4.addEdge(8, 9) 
    g4.addEdge(9, 8) 
    print ("nSSC in fourth graph ")
    printCCs(g4)
    
    
    g5 = Graph (5, "directed") 
    g5.addEdge(0, 1) 
    g5.addEdge(1, 2) 
    g5.addEdge(2, 3) 
    g5.addEdge(2, 4) 
    g5.addEdge(3, 0) 
    g5.addEdge(4, 2) 
    print ("nSSC in fifth graph ")
    printCCs(g5) 

# testFindCCs2()