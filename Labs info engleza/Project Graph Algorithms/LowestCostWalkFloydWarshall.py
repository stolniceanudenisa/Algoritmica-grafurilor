from Graph import Graph
from texttable import Texttable

INF = 99999

def LowestCostWalkByFloydWarshall(graph, startVertex, endVertex):
    '''
    Finds the lowest cost walk and the minimum cost between startVertex and endVertex, while also displaying
    the intermediate matrices for costs and previous vertices.
    input:
        - Graph graph
        - int startVertex
        - int endVertex
    output:
        - list reconstructedPath
        - int minimum cost
    raises:
        - ValueError if the vertices do not exist or they are equal
        - ValueError if there is no path between the vertices
    '''
    if startVertex not in graph.parseVertices() or endVertex not in graph.parseVertices():
        raise ValueError("A vertex does not exist. \n")
    if startVertex == endVertex:
        raise ValueError("The startVertex and endVertex are equal")

    # initialize the distances matrix
    distance = []
    for vertex1 in graph.parseVertices():
        newLineDistance = []
        for vertex2 in graph.parseVertices():
            if graph.isEdge(vertex1, vertex2):
                newLineDistance.append(graph.getCostEdge(vertex1, vertex2))
            elif vertex1 == vertex2:
                newLineDistance.append(0)
            else:
                newLineDistance.append(INF)
        distance.append(newLineDistance)

    # initialize the previous matrix
    previous = []
    for vertex1 in graph.parseVertices():
        newLinePrevious = []
        for vertex2 in graph.parseVertices():
            if graph.isEdge(vertex1, vertex2):
                # for previous matrix
                newLinePrevious.append(vertex1)
            else:
                newLinePrevious.append(-1) # fill in with -1 if there is no predecessor
        previous.append(newLinePrevious)

    for intermediateVertex in graph.parseVertices():
        # consider each vertex as an intermidiate vertex
        for vertex1 in graph.parseVertices():
            # consider each vertex as source vertex
            for vertex2 in graph.parseVertices():
                # consider each vertex as destination vertex

                # if the intermediateVertex is on the lowest cost path from vertex1 to vertex2, update the value
                # distance[vertex1][vertex2]
                if distance[vertex1][intermediateVertex] + distance[intermediateVertex][vertex2] < distance[vertex1][vertex2]:
                    distance[vertex1][vertex2] = distance[vertex1][intermediateVertex] + distance[intermediateVertex][vertex2]
                    previous[vertex1][vertex2] = previous[intermediateVertex][vertex2]

        # print the intermediate matrices
        print("IntermediateVertex = ", intermediateVertex)
        # f = open("resultsLowestCostWalk.txt", "a")
        # message = "IntermediateVertex = " + str(intermediateVertex)
        # f.write(message)
        # f.write("\n")
        # f.close()

    printDistancesMatrix(distance)
    printPreviousMatrix(previous)

    lowestCostWalk = distance[startVertex][endVertex]
    if lowestCostWalk == INF:
        raise ValueError("There is no path between the vertices.")

    reconstructedPath = reconstructPath(previous, distance, startVertex, endVertex)

    return reconstructedPath, lowestCostWalk

def printDistancesMatrix(distance):
    '''
    Prints the intermediate matrix of distances.
    input:
        - matrix distances
    output:
        - the matrix is printed
    '''
    matrix = Texttable()

    for line in distance:
        printLine = []
        for element in line:
            if element == INF:
                printLine.append("INF")
            else:
                printLine.append(element)
        matrix.add_row(printLine)

    print(matrix.draw())
    # f = open("resultsGraph1kfrom0to100.txt", "w")
    # f.write(matrix.draw())
    # f.write("\n")
    # f.close()

def printPreviousMatrix(previous):
    '''
    Prints the intermediate matrix of previous vertices.
    input:
        - matrix previous
    output:
        - the matrix is printed
    '''
    matrix = Texttable()

    for line in previous:
        printLine = []
        for element in line:
            printLine.append(element)
        matrix.add_row(printLine)

    print(matrix.draw())
    # f = open("resultsGraph1kfrom0to100.txt", "a")
    # f.write(matrix.draw())
    # f.write("\n")
    # f.close()

def reconstructPath(previous, distance, startVertex, endVertex):
    '''
    Reconstructs the path with costs backwards using the previous matrix.
    input:
        - matrix previous
        - matrix distance
        - int startVertex
        - int endVertex
    output:
        - a list containing the edges from the lowest cost walk and its costs
    '''
    path = [endVertex]

    while endVertex != startVertex:
        endVertex = previous[startVertex][endVertex]
        path.append(endVertex)
    
    path.reverse()
    pathWithCosts = []
    for indexVertex in range(len(path)-1):
        pathWithCosts.append(((path[indexVertex], path[indexVertex + 1]), distance[path[indexVertex]][path[indexVertex + 1]]))

    return pathWithCosts




def printDistancesMatrix2(distance):
    f = open("resultsGraph1kfrom0to100matrix.txt", "w")
    for line in distance:
        newLine = ""
        for element in line:
            if element == INF:
                newLine += "INF "
            else:
                newLine += str(element) + " "
        newLine += "\n"
        print(newLine)
        f.write(newLine)
    f.close()

def printPreviousMatrix2(previous):
    f = open("resultsGraph1kfrom0to100matrix.txt", "a")
    for line in previous:
        newLine = ""
        for element in line:
            newLine += str(element) + " "
        newLine += "\n"
        print(newLine)
        f.write(newLine)
    f.close()

# ----------------------------------------------- Tests -----------------------------------------------------

def testLowestCostPath():
    graph = Graph(4, "directed")
    graph.addEdge(0, 1, 5)
    graph.addEdge(0, 3, 10)
    graph.addEdge(1, 2, 3)
    graph.addEdge(2, 3, 1)

    path, lowestCost = LowestCostWalkByFloydWarshall(graph, 0, 3)

    print(path)
    print(lowestCost)

def testLowestCostPath2():
    graph = Graph(5, "directed")
    graph.addEdge(1, 2, 5)
    graph.addEdge(1, 3, 20)
    graph.addEdge(2, 4, 30)
    graph.addEdge(2, 3, 10)
    graph.addEdge(3, 4, 5)

    path, lowestCost = LowestCostWalkByFloydWarshall(graph, 1, 4)

    print(path)
    print(lowestCost)

def testLowestCostPath3():
    graph = Graph(5, "directed")
    graph.addEdge(0, 1, 5)
    graph.addEdge(0, 3, 10)
    graph.addEdge(1, 2, 3)
    graph.addEdge(1, 4, 10)
    graph.addEdge(2, 3, 1)
    graph.addEdge(2, 4, 2)
    graph.addEdge(3, 0, 1)
    graph.addEdge(3, 1, 6)
    graph.addEdge(3, 2, 20)
    graph.addEdge(4, 0, 15)

    path, lowestCost = LowestCostWalkByFloydWarshall(graph, 0, 4)

    print(path)
    print(lowestCost)

# testLowestCostPath3()