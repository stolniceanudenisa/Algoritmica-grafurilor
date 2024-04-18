from Graph import Graph, createRandomGraph
from ConnectedComponentsUndirectedGraph import ConnectedComponents
from StronglyConnectedComponentsKosaraju import findStronglyConnectedComponents
from BiconnectedComponentsUndirectedTarjan import findBiconnectedComponents
from LowestCostWalkFloydWarshall import LowestCostWalkByFloydWarshall
from TopologicalSorting import ActivitiesScheduling
from MaximumCliqueBronKebosch import maximumClique

class UI:

    def _printMainMenu(self):
        result = ""
        result += "0. Exit \n"
        result += "1. Read a directed graph from a textfile. \n"
        result += "2. Create a directed random graph. \n"
        result += "3. Read an undirected graph from a textfile and find its connected components. \n"
        result += "4. Read a directed graph from a textfile and find its strongly-connected components. \n"
        result += "5. Read an undirected graph from a textfile and find its biconnected components. \n"
        result += "6. Read a directed graph from a textfile and two vertices and find the lowest cost walk. \n"
        result += "7. Read n activities, their duration and dependencies and print their detalis, total time of the project and the critical activities. \n"
        result += "8. Read an undirected graph from a textfile and find a clique of maximum size. \n"

        print(50 * "-")
        print(result)
        print(50 * "-")

    def _printMenu(self):
        result = ""
        result += "0. Exit. \n"
        result += "1. Get the number of vertices. \n"
        result += "2. Parse the set of vertices. \n"
        result += "3. Give vertices x, y and find if there is and edge (x,y). \n"
        result += "4. Get the In Degree of x. \n"
        result += "5. Get the Out Degree of x. \n"
        result += "6. Parse (iterate) the set of outbound edges(target vertex) of a vertex x. \n"
        result += "7. Parse (iterate) the set of inbound edges(target vertex) of a vertex x. \n"
        result += "8. Get cost of edge (x, y). \n"
        result += "9. Modify cost of edge (x, y). \n"
        result += "10. Add Vertex. \n"
        result += "11. Remove Vertex. \n"
        result += "12. Add Edge. \n"
        result += "13. Remove Edge. \n"
        result += "14. Get a copy of the Graph. \n"
        result += "15. Write a Graph to a textfile. \n"
        result += "16. Print Graph. \n"
        result += "17. Find the connected components in an undirected graph. \n"

        print(50 * "-")
        print(result)
        print(50 * "-")

    def _createRandomGraphUI(self):
    
        n = int(input("Give number of vertices: "))
        m = int(input("Give number of edges: "))

        if(m > n*n):
            errorMessage = ""
            errorMessage += "The graph can have maximum " +  str(n*n) + " edges."
            raise ValueError(errorMessage)

        newGraph = createRandomGraph(n, m)
        return(newGraph)

    def _readDirectedGraphFromTextfileUI(self, fileName):
        '''
        Reads a graph from a textfile and creates the graph.
        '''
        f = open(fileName, 'r')

        line = f.readline().strip()
        line = line.split(" ")

        # the first line contains the nr of vertices(n) and the nr of edges
        n = int(line[0])
        nrEdges = int(line[1])

        # create a new graph with n vertices
        newGraph = Graph(n, "directed")

        # add each edge from the textfile to the graph
        for edge in range(nrEdges):
            line = f.readline().strip()
            line = line.split(' ')

            # a line has the format x, y, cost
            newGraph.addEdge(int(line[0]), int(line[1]), int(line[2]))

        f.close()

        return newGraph

    def _readUndirectedGraphFromTextfileUI(self, fileName):
        '''
        Reads an undirected graph from a textfile and creates the graph.
        '''
        f = open(fileName, 'r')

        line = f.readline().strip()
        line = line.split(" ")

        # the first line contains the nr of vertices(n) and the nr of edges
        n = int(line[0])
        nrEdges = int(line[1])

        # create a new graph with n vertices
        newGraph = Graph(n, "undirected")

        # add each edge from the textfile to the graph
        for edge in range(nrEdges):
            line = f.readline().strip()
            line = line.split(' ')

            # a line has the format x, y, cost
            x = int(line[0])
            y = int(line[1])
            cost = int(line[2])

            if newGraph.isEdge(x,y) == False and x != y:
                # as the file contains a directed graph, we have to check if the edge
                # does not already exist
                newGraph.addEdge(x, y, cost)

        f.close()

        return newGraph

    def _getNumberVerticesUI(self, graph):
        message = "The number of vertices is " + str(graph.getNumberVertices()) + '\n'
        print(message)

        # besides printing the results of the operations on the screen, we will display the results of the operations
        # in results.txt file
        f = open("results.txt", "a")
        f.write(message)
        f.close()
    
    def _parseVerticesUI(self, graph):
        message = "The vertices are: "
        for vertex in graph.parseVertices():
            message += str(vertex) + " "
        message += '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _isEdgeUI(self, graph):
        x = int(input("Give x: "))
        y = int(input("Give y: "))

        f = open("results.txt", "a")

        if graph.isEdge(x, y):
            message = "There is an edge (" + str(x) + ", " + str(y) + "). \n"
            print(message)
            f.write(message)
        else:
            message = "There is no edge (" + str(x) + ", " + str(y) + "). \n"
            print(message)
            f.write(message)

        f.close()

    def _getInDegreeUI(self, graph):
        x = int(input("Give vertex: "))
        message = "The in degree of " +  str(x) + " is: " + str(graph.getInDegree(x)) + '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _getOutDegreeUI(self, graph):
        x = int(input("Give vertex: "))
        message = "The out degree of " + str(x) + " is: " + str(graph.getOutDegree(x)) + '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _parseOutboundEdgesUI(self, graph):
        x = int(input("Give vertex: "))
        message = "The target vertices of the outbound edges are: "
        for vertex in graph.parseOutboundEdges(x):
            message += str(vertex) + " "
        message += '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _parseInboundEdgesUI(self, graph):
        x = int(input("Give vertex: "))
        message = "The target vertices of the inbound edges are: "
        for vertex in graph.parseInboundEdges(x):
            message += str(vertex) + " "
        message += '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _getCostOfEdgeUI(self, graph):
        x = int(input("Give x: "))
        y = int(input("Give y: "))
        message = "The cost of the edge (" + str(x) + ", " + str(y) + ") is: " + str(graph.getCostEdge(x,y)) + '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _modifyCostEdgeUI(self, graph):
        x = int(input("Give x: "))
        y = int(input("Give y: "))
        newCost = int(input("Give new cost: "))
        graph.updateCostEdge(x,y, newCost)
        message = "The cost of the edge (" + str(x) + ", " + str(y) + ") is now: " + str(graph.getCostEdge(x,y)) + '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _addVertexUI(self, graph):
        x = int(input("Give x: "))
        graph.addVertex(x)
        message = "The vertex " + str(x) + " was added." +'\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _removeVertexUI(self, graph):
        x = int(input("Give x: "))
        graph.removeVertex(x)
        message = "The vertex " + str(x) + " was removed." + '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _addEdgeUI(self, graph):
        x = int(input("Give x: "))
        y = int(input("Give y: "))
        cost = int(input("Give cost: "))
        graph.addEdge(x, y, cost)
        message = "The edge (" + str(x) + ", " + str(y) + ") having the cost " + str(cost) + " was added." + '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _removeEdgeUI(self, graph):
        x = int(input("Give x: "))
        y = int(input("Give y: "))
        graph.removeEdge(x, y)
        message = "The edge (" + str(x) + ", " + str(y) + ") was removed." + '\n'
        print(message)

        f = open("results.txt", "a")
        f.write(message)
        f.close()

    def _getCopyOfGraphUI(self, graph):
        copyGraph = graph.copyGraph()
        print("This is a copy of the graph:")
        print(copyGraph.graphAsString())

        f = open("results.txt", "a")
        f.write("This is a copy of the graph: \n")
        f.write(copyGraph.graphAsString())
        f.write("\n")
        f.close()

    def _printGraph(self, graph):
        print("The graph is: ")
        print(graph.graphAsString())

    def _writeGraphToTextfileUI(self, graph):
        '''
        Writes the graph 'graph' to a textfile.
        '''
        fileName = input("Enter the name of the textfile: ")
        f = open(fileName, "w")

        result = graph.graphAsString()
        f.write(result)

        f.close()

    def _printConnectedComponents(self, graph):
        allConnectedComponents = ConnectedComponents(graph)

        if len(allConnectedComponents) == 0:
            print("There are no connectedComponents(vertices).")
            return

        numberConnectedComponent = 0
        message = ""

        for component in allConnectedComponents:
            numberConnectedComponent += 1
            message = ""
            message += "Connected component " + str(numberConnectedComponent) + ": "
            print(message)
            print(component.componentAsString())
            print("\n")

    def _printStronglyConnectedComponents(self, graph):
        allStronglyConnectedComponents = findStronglyConnectedComponents(graph)

        if len(allStronglyConnectedComponents) == 0:
            print("There are no strongly-connectedComponents(vertices).")
            return

        numberStronglyConnectedComponent = 0
        message = ""

        for component in allStronglyConnectedComponents:
            numberStronglyConnectedComponent += 1
            message = ""
            message += "Strongly-connected component " + str(numberStronglyConnectedComponent) + ": "
            print(message)
            print(component.componentAsString())
            print("\n")

    def _printBiconnectedComponents(self, graph):
        allBiConnectedComponents = findBiconnectedComponents(graph)

        if len(allBiConnectedComponents) == 0:
            print("There are no strongly-connectedComponents(vertices).")
            return

        numberBiConnectedComponent = 0
        message = ""

        for component in allBiConnectedComponents:
            numberBiConnectedComponent += 1
            message = ""
            message += "Biconnected component " + str(numberBiConnectedComponent) + ": "
            print(message)
            print(component.componentAsString())
            print("\n")

    def _printLowestCostWalk(self, newGraph, startVertex, endVertex):
        try:
            path, cost = LowestCostWalkByFloydWarshall(newGraph, startVertex, endVertex)
            message = "Lowest cost walk: "
            for vertex in path:
                message += str(vertex) + " "
            message += "\n"
            message += "Cost: " + str(cost) + "\n"
            print(message)

            f = open("resultsGraph1kfrom0to100matrix.txt", "a")
            f.write(message)
            f.close()
        except ValueError as message:
            print(message)

    def _readActivitiesGraph(self, fileName):
        '''
        Reads a graph from a textfile and creates the graph and the activityDuration dictionary.
        '''
        f = open(fileName, 'r')

        line = f.readline().strip()
        #line = line.split(" ")

        # the first line contains the nr of vertices(n)
        n = int(line[0])

        # create a new graph with n vertices ( from 1 to n)
        newGraph = Graph(n+1, "directed")
        newGraph.removeVertex(0)
        activityDuration = {}

        # read the activity durations
        line = f.readline().strip()
        line = line.split(" ")

        for index in range(1, n+1):
            activityDuration[index] = int(line[index-1])

        # add for each vertex the dependencies
        for activity in range(1, n+1):
            line = f.readline().strip()
            if line != "-1":
                line = line.split(' ')
                for previousActivity in line:
                    newGraph.addEdge(int(previousActivity), activity)

        f.close()

        return newGraph, activityDuration

    def _printActivities(self, newGraph, activityDuration):
        earliestStartTime, latestStartTime, sortedList, criticalActivities = ActivitiesScheduling(newGraph, activityDuration)
        
        # print a topological order
        message = ""
        message += "A topological order is: "
        for vertex in sortedList:
            message += str(vertex) + " "
        print(message)
        
        # print the earliest and latest start time for each activity
        message = ""
        for activity in newGraph.parseVertices():
            message = str(activity) + ": "
            message += "Earliest start time: " + str(earliestStartTime[activity]) + " "
            message += "Latest start time: " + str(latestStartTime[activity]) + " "
            print(message)

        # print the total time of the project
        message = ""
        message += "Total time of the project: " + str(earliestStartTime[len(sortedList) + 1])
        print(message)

        # print the critical activities
        message = "The critical activities are: "
        for activity in criticalActivities:
            message += str(activity) + " "
        print(message)
        print("\n")

        # print the graph in graph form
        print(newGraph.componentAsString())
    
    def _printCliqueOfMaximumSize(self, newGraph):
        cliqueOfMaximumSize, subgraph = maximumClique(newGraph)

        message = "The vertices from a clique of maxmimum size are: "
        for vertex in cliqueOfMaximumSize:
            message += str(vertex) + " "
        print(message)
        print("\n")
        print(subgraph.componentAsString())
        print("\n")

    def start(self):

        commands = {1: self._getNumberVerticesUI, 2: self._parseVerticesUI, 3: self._isEdgeUI,
        4: self._getInDegreeUI, 5: self._getOutDegreeUI, 6: self._parseOutboundEdgesUI, 7: self._parseInboundEdgesUI, 
        8: self._getCostOfEdgeUI, 9: self._modifyCostEdgeUI, 10: self._addVertexUI, 11: self._removeVertexUI, 
        12: self._addEdgeUI, 13: self._removeEdgeUI, 14: self._getCopyOfGraphUI, 15: self._writeGraphToTextfileUI,
        16: self._printGraph, 17: self._printConnectedComponents}

        while(True):
            try:
                self._printMainMenu()
                mainCommand = int(input("Enter command: "))

                if mainCommand == 0:
                    # exit
                    return
                elif mainCommand == 1:
                    # read a graph from a textfile and continue with other commands
                    fileName = input("Enter the name of the textfile: ")
                    newGraph = self._readDirectedGraphFromTextfileUI(fileName)

                    while(True):
                        self._printMenu()
                        command = int(input("Enter command: "))
                        if command == 0:
                            break
                        try:
                            commands[command](newGraph)
                        except Exception as ex:
                            print(ex)

                elif mainCommand == 2:
                    # create a random graph and save it in a textfile
                    fileName = input("Enter the name of the textfile where you want the graph to be saved: ")
                    f = open(fileName, "w")
                    try:
                        newGraph = self._createRandomGraphUI()
                        f.write(newGraph.graphAsString())
                    except Exception as ex:
                        f.write(str(ex))
                        print(ex)
                    f.close()

                elif mainCommand == 3:
                    # read an undirected graph from a textfile and find its connected components
                    fileName = input("Enter the name of the textfile: ")
                    newGraph = self._readUndirectedGraphFromTextfileUI(fileName)
                    try:
                        self._printConnectedComponents(newGraph)
                    except Exception as ex:
                        print(ex)

                elif mainCommand == 4:
                    # read a directed graph from a textfile and find its strongly-connected components
                    fileName = input("Enter the name of the textfile: ")
                    newGraph = self._readDirectedGraphFromTextfileUI(fileName)
                    try:
                        self._printStronglyConnectedComponents(newGraph)
                    except Exception as ex:
                        print(ex)
                
                elif mainCommand == 5:
                    # read an undirected graph from a textfile and find its biconnected components
                    fileName = input("Enter the name of the textfile: ")
                    newGraph = self._readUndirectedGraphFromTextfileUI(fileName)
                    try:
                        self._printBiconnectedComponents(newGraph)
                    except Exception as ex:
                        print(ex)

                elif mainCommand == 6:
                    # read a directed graph and two vertices from a textfile and find the lowest cost walk
                    fileName = input("Enter the name of the textfile: ")
                    newGraph = self._readDirectedGraphFromTextfileUI(fileName)

                    startVertex = int(input("Enter startVertex: "))
                    endVertex = int(input("Enter endVertex: "))

                    try:
                        self._printLowestCostWalk(newGraph, startVertex, endVertex)
                    except Exception as ex:
                        print(ex)
                elif mainCommand == 7:
                    fileName = input("Enter the name of the textfile: ")
                    newGraph, activityDuration = self._readActivitiesGraph(fileName)

                    self._printActivities(newGraph, activityDuration)
                elif mainCommand == 8:
                    # read an undirected graph from a textfile and find a clique of maximum size
                    fileName = input("Enter the name of the textfile: ")
                    newGraph = self._readUndirectedGraphFromTextfileUI(fileName)

                    self._printCliqueOfMaximumSize(newGraph)

                else:
                    print("Bad command.")

            except Exception as ex:
                print(ex)