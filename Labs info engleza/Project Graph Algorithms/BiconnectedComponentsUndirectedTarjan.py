from Graph import Graph

def createBiconnectedComponentByDFS(graph, currentTime, startVertex, discoveryTime, lowlink, parent, stackProcessed, allBiconnectedComponents):
    '''
    Finds the biconnected components from startVertex and adds them to the list allBiconnectedComponents as Graph objects.
    In order to do that, it performs a deep-first search on a graph with a given startVertex.
    input:
        - directed Graph graph
        - int currentTime
        - int startVertex
        - list discoveryTime, lowlink
        - list parent
        - list stackProcessed
        - list allBiconnectedComponents
    output: -
    '''
    # initialize discoveryTime, lowlink, push the vertex on the stackProcessed
    discoveryTime[startVertex] = currentTime
    lowlink[startVertex] = currentTime
    currentTime += 1

    # count the children in the current node
    children = 0

    # visit all its neighbours
    for neighbour in graph.parseOutboundEdges(startVertex):
        # if the neighbour is not visited yet, continue the DFS (make it a child of startVertex)
        if discoveryTime[neighbour] == -1:
            children += 1
            parent[neighbour] = startVertex
            # add the edge on the stack
            stackProcessed.append((startVertex, neighbour))

            createBiconnectedComponentByDFS(graph, currentTime, neighbour, discoveryTime, lowlink, parent, stackProcessed, allBiconnectedComponents)

            # Check if the subtree rooted with startVertex has a connection to one of the ancestors of neighbour
            lowlink[startVertex] = min(lowlink[startVertex], lowlink[neighbour])

            # If startVertex is an articulation point, pop all edges from stack until (startVertex, neighbour)
            # and add them to the newBCC
            # a vertex is an articulation point in 2 cases:
            # 1. it is the root and has at leats 2 direct children
            # 2. its discoveryTime <= than the lowlink of one of its neighbours
            if parent[startVertex] == -1 and children > 1 or parent[startVertex] != -1 and lowlink[neighbour] >= discoveryTime[startVertex]: 
                # create a newBCC (Graph object)
                newBCC = Graph(0, "undirected")
                currentEdge = -1
                #currentEdge = stackProcessed.pop()
                while currentEdge != (startVertex, neighbour): 
                    currentEdge = stackProcessed.pop()
                    if newBCC.isVertex(currentEdge[0]) == False:
                        newBCC.addVertex(currentEdge[0])
                    if newBCC.isVertex(currentEdge[1]) == False:
                        newBCC.addVertex(currentEdge[1])
                    newBCC.addEdge(currentEdge[0], currentEdge[1])
                    #currentEdge = stackProcessed.pop()
                    
                # add the new component to the list
                allBiconnectedComponents.append(newBCC)

        # if we find a backEdge
        elif neighbour != parent[startVertex] and lowlink[startVertex] > discoveryTime[neighbour]: 
            # Update lowlink value of startVertex only if neighbour has been already processed
            # (it's a back edge, not cross edge)
            lowlink[startVertex] = min(lowlink[neighbour], discoveryTime[startVertex])
            stackProcessed.append((startVertex, neighbour))

def findBiconnectedComponents(graph):
    '''
    Finds the biconnected components of an undirected graph and returns the result as a list of Graph
    objects.
    input:
        - an undirected graph
    output:
        - a list containing all biconnected components of the graph
    '''
    allBiconnectedComponents = []
    discoveryTime = [-1] * graph.getNumberVertices()
    lowlink = [-1] * graph.getNumberVertices()
    parent = [-1] * graph.getNumberVertices()
    stackProcessed = []

    for vertex in graph.parseVertices():
        if discoveryTime[vertex] == -1:
            # it was not visited yet
            currentTime = 1
            createBiconnectedComponentByDFS(graph, currentTime, vertex, discoveryTime, lowlink, parent, stackProcessed, allBiconnectedComponents)

            # If stack is not empty, pop all edges from stack and create a new BCC 
            if len(stackProcessed) > 0: 
                newBCC = Graph(0, "undirected")
                while stackProcessed: 
                    currentEdge = stackProcessed.pop()
                    if newBCC.isVertex(currentEdge[0]) == False:
                        newBCC.addVertex(currentEdge[0])
                    if newBCC.isVertex(currentEdge[1]) == False:
                        newBCC.addVertex(currentEdge[1])
                    newBCC.addEdge(currentEdge[0], currentEdge[1])
                allBiconnectedComponents.append(newBCC)

    return allBiconnectedComponents

# ---------------------------------------------- Tests -------------------------------------------------------

def printCCs(g):
    allCCs = findBiconnectedComponents(g)

    numberComponent = 0

    for cc in allCCs:
        numberComponent += 1
        message = ""
        message += "Component " + str(numberComponent) + ": "
        print(message)
        print(cc.componentAsString())
        print("\n")

def testBCCs():
    g = Graph(12, "undirected") 
    g.addEdge(0, 1) 
    g.addEdge(1, 2) 
    g.addEdge(1, 3) 
    g.addEdge(2, 3) 
    g.addEdge(2, 4) 
    g.addEdge(3, 4) 
    g.addEdge(1, 5) 
    g.addEdge(0, 6) 
    g.addEdge(5, 6) 
    g.addEdge(5, 7) 
    g.addEdge(5, 8) 
    g.addEdge(7, 8) 
    g.addEdge(8, 9) 
    g.addEdge(10, 11)

    printCCs(g)

# testBCCs()

def testBCCs2():
    g = Graph(3, "undirected")
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,0)

    printCCs(g)

# testBCCs2()