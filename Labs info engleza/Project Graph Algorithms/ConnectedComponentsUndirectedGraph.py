from Graph import Graph

def ConnectedComponentByBFS(graph, startVertex, visited):
    '''
    Finds all the vertices accesible from startVetex in the graph.
    input:
        - Graph graph
        - int startVertex - the vertex from which the path starts
        - list visited - the list with the vertices which have already been visited
    output:
        - newConnectedComponent - a Graph object representing the current connected component
    '''

    # we found a new connected component, so we initialize a new Graph object
    newConnectedComponent = Graph(0, "undirected")

    # create a queue
    queue = []

    # add the startVertex to the queue, mark it as visited by adding it to visited
    # add the startVertex to the newConnectedComponent
    queue.append(startVertex)
    visited.append(startVertex)
    newConnectedComponent.addVertex(startVertex)

    while len(queue) > 0:
        # take the first vertex in the queue
        startVertex = queue.pop(0)

        for neighbour in graph.parseOutboundEdges(startVertex):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                # add the neighbour to the newConnectedComponent
                newConnectedComponent.addVertex(neighbour)
                # add the edge to the newConnectedComponent (undirected graph)
                newConnectedComponent.addEdge(startVertex, neighbour, 0)

    return newConnectedComponent

def ConnectedComponents(graph):
    '''
    Finds all the connected components in an undirected graph and returns them as Graph objects.
    input:
        - undirected graph
    output:
        - a list (allConnectedComponents) containing all the connected components as Graph objects
    '''
    # create a list which will store all the connected components as Graph objects
    allConnectedComponents = []
    # keep a list of visited vertices in order to visit them only once
    visited = []

    for vertex in graph.parseVertices():
        if vertex not in visited:
            # call ConnectedComponentByBFS and find the newConnectedComponent
            newConnectedComponent = ConnectedComponentByBFS(graph, vertex, visited)

            # if there are edges in the initial graph that were not added in the newConnectedComponent, add them
            for x in newConnectedComponent.parseVertices():
                for y in newConnectedComponent.parseVertices():
                    if x != y and newConnectedComponent.isEdge(x,y) == False and graph.isEdge(x,y) == True:
                        newConnectedComponent.addEdge(x, y, 0)

            # append the newConnectedComponent (Graph object) to the list of allConnectedComponents
            allConnectedComponents.append(newConnectedComponent)

    return allConnectedComponents


