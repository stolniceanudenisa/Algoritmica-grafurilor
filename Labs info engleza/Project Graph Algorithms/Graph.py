from copy import deepcopy
import random

class Graph:
    def __init__(self, n, graphType):
        self._dictIn = {}
        self._dictOut = {}
        self._dictCost = {}
        self._n = n
        self._graphType = graphType

        for i in range(n):
            self._dictIn[i] = []
            self._dictOut[i] = []

        self._isolatedVertices = []
        self._inexistentVertices = []

    def getNumberVertices(self):
        '''
        Gets the number of vertices.
        '''
        return len(self._dictIn)
    
    def parseVertices(self):
        '''
        Returns an iterator for all the vertices.
        '''
        return self._dictIn.keys()

    # added function
    def getNumberEdges(self):
        '''
        Gets the number of edges.
        '''
        return len(self._dictCost)
    
    def parseEdges(self):
        '''
        Returns an iterator for all the edges.
        '''
        return self._dictCost.keys()

    def addEdge(self, x, y, cost = 0):
        '''
        Adds an edge from x to y with the cost 'cost'.
        Precondition: the edge (x,y) does not already exist.
        Raises: ValueError if the edge already exists or if the target vertices does not exist.
        '''
        if self._graphType == "undirected":
            if (x,y) in self._dictCost.keys() or (y,x) in self._dictCost.keys():
                raise ValueError("The edge already exists.")
            if x not in self._dictIn or y not in self._dictIn:
                raise ValueError("The target vertices do not exist.")

            self._dictIn[x].append(y)
            self._dictIn[y].append(x)
            self._dictOut[x].append(y)
            self._dictOut[y].append(x)
            self._dictCost[(x,y)] = cost

        else:
            if (x,y) in self._dictCost.keys():
                raise ValueError("The edge already exists.")
            if x not in self._dictIn or y not in self._dictIn:
                raise ValueError("The target vertices does not exist.")

            self._dictIn[y].append(x)
            self._dictOut[x].append(y)
            self._dictCost[(x,y)] = cost
    
    def removeEdge(self, x, y):
        '''
        Deletes the edge from x to y.
        Precondition: the edge (x,y) exists in the graph.
        Raises: ValueError if the edge does nor exist.
        '''
        if self._graphType == "undirected":
            if (x,y) not in self._dictCost.keys() and (y,x) not in self._dictCost.keys():
                raise ValueError("The edge does not exist.")
            # remove the edge from self._dictCost
            if (x,y) in self._dictCost.keys():
                self._dictCost.pop((x,y))
            elif (x,y) in self._dictCost.keys():
                self._dictCost.pop((y,x))

            # remove x from self._dictOut[y]
            index = self._dictOut[y].index(x)
            self._dictOut[y].pop(index)
            # remove y from self._dictOut[x]
            index = self._dictOut[x].index(y)
            self._dictOut[x].pop(index)
            # remove x from self._dictIn[y]
            index = self._dictIn[y].index(x)
            self._dictIn[y].pop(index)
            # remove y from self._dictIn[x]
            index = self._dictIn[x].index(y)
            self._dictIn[x].pop(index)
        else:
            if (x,y) not in self._dictCost.keys():
                raise ValueError("The edge does not exist.")
            # remove the edge from self._dictCost
            self._dictCost.pop((x,y))
            # remove y from self._dictOut[x]
            index = self._dictOut[x].index(y)
            self._dictOut[x].pop(index)
            # remove x from self._dictIn[y]
            index = self._dictIn[y].index(x)
            self._dictIn[y].pop(index)

    def addVertex(self, x):
        '''
        Adds a vertex x.
        Precondition: the vertex does not already exist.
        Raises: ValueError if the vertex already exists.
        '''
        if x in self._dictOut.keys():
            raise ValueError("Vertex already exists.")

        self._dictIn[x] = []
        self._dictOut[x] = []

        if x >= self._n:
            self._isolatedVertices.append(x)

    def removeVertex(self, x):
        '''
        Deletes a vertex x.
        Precondition: the vertex exists in the graph.
        Raises: ValueError if the vertex does not exist.
        '''
        if x not in self._dictOut.keys():
            raise ValueError("Vertex does not exist.")
        
        if x >= self._n:
            index = self._isolatedVertices.index(x)
            if index >= 0 and index < len(self._isolatedVertices):
                self._isolatedVertices.remove(x)

        for vertex in self._dictOut[x]:
            try:
                self._dictCost.pop((x,vertex))
            except Exception:
                pass
            self._dictIn[vertex].remove(x)

        for vertex in self._dictIn[x]:
            try:
                self._dictCost.pop((vertex, x))
            except Exception:
                pass
            self._dictOut[vertex].remove(x)
            
        self._dictOut.pop(x)
        self._dictIn.pop(x)

        if x < self._n:
            self._inexistentVertices.append(x)

    def isEdge(self, x, y):
        '''
        Checks if the edge determined by the vertices x, y exists in the graph.
        Returns:
            True - if there exists an edge from x to y
            False - otherwise
        '''
        if self._graphType == "undirected":
            if (x,y) in self._dictCost.keys() or (y,x) in self._dictCost.keys():
                return True
            return False
        else:
            if (x,y) in self._dictCost.keys():
                return True
            return False

    def isVertex(self, x):
        '''
        Checks if the vertex x exists in the graph.
        Returns:
            True - if the vertex exists
            False - otherwise
        '''
        if x in self._dictIn.keys():
            return True
        return False

    def getInDegree(self, x):
        '''
        Returns the InDegree of vertex x.
        Precondition: the vertex x exists.
        Raises: ValueError if the vertex does not exist.
        '''
        if x not in self._dictIn.keys():
            raise ValueError("The vertex does not exist.")
        return len(self._dictIn[x])
    
    def getOutDegree(self, x):
        '''
        Returns the OutDegree of vertex x.
        Precondition: the vertex x exists.
        Raises: ValueError if the vertex does not exist.
        '''
        if x not in self._dictOut.keys():
            raise ValueError("The vertex does not exist.")
        return len(self._dictOut[x])

    def parseOutboundEdges(self, x):
        '''
        Parse (iterate) the set of outbound edges of a specified vertex
        (the target vertices).
        Precondition: the vertex x exists.
        Raises: ValueError if the vertex does not exist.
        '''
        if x not in self._dictOut.keys():
            raise ValueError("The vertex does not exist.")
        return self._dictOut[x]

    def parseInboundEdges(self, x):
        '''
        Parse (iterate) the set of outbound edges of a specified vertex
        (the target vertices).
        Precondition: the vertex x exists.
        Raises: ValueError if the vertex does not exist.
        '''
        if x not in self._dictIn.keys():
            raise ValueError("The vertex does not exist.")
        return self._dictIn[x]

    def getCostEdge(self, x, y):
        '''
        Returns the cost of the edge (x,y)
        Precondition: the edge (x,y) exists.
        Raises: ValueError if the edge does not exist.
        '''
        if self._graphType == "undirected":
            if (x,y) not in self._dictCost.keys() and (y,x) not in self._dictCost.keys():
                raise ValueError("The edge does not exist.")
            if (x,y) in self._dictCost.keys():
                return self._dictCost[(x,y)]
            else:
                return self._dictCost[(y,x)]
        else:
            if (x,y) not in self._dictCost.keys():
                raise ValueError("The edge does not exist.")
            return self._dictCost[(x,y)]

    def updateCostEdge(self, x, y, newCost):
        '''
        Updates the cost of the edge (x,y)
        Precondition: the edge (x,y) exists.
        Raises: ValueError if the edge does not exist.
        '''
        if self._graphType == "undirected":
            if (x,y) in self._dictCost.keys():
                self._dictCost[(x,y)] = newCost
            elif (y,x) in self._dictCost.keys():
                self._dictCost[(x,y)] = newCost
            else:
                raise ValueError("The edge does not exist.")
        else:  
            if (x,y) not in self._dictCost.keys():
                raise ValueError("The edge does not exist.")
            self._dictCost[(x,y)] = newCost

    def copyGraph(self):
        '''
        Returns a copy of the graph.
        '''
        return deepcopy(self)

    def graphAsString(self):
        '''
        Returns the graph as a string, so that in can be written to a textfile.
        '''
        result = ""
        result += str(len(self._dictIn)) + " " + str(len(self._dictCost)) + "\n"
        for edge, value in self._dictCost.items():
            result += str(edge[0]) + " " + str(edge[1]) + " " + str(value) + "\n"

        # if there are isolated vertices or a vertex from 0 to n-1 is missing, we will write them here:
        # if x is isolated it will appear as x 1, if x is missing from 0 to n-1 it will appear as x -1
        for vertex in self._inexistentVertices:
                result += str(vertex) + " " + str(-1) + "\n"

        for vertex in self._isolatedVertices:
                result += str(vertex) + " " + str(1) + "\n"

        return result

    def componentAsString(self):
        result = ""
        result += "Vertices: "
        for vertex in self.parseVertices():
            result += str(vertex) + " "
        result += "\n"

        result += "Edges: "
        for edge in self.parseEdges():
            result += str(edge) + " "
        
        return result

def createRandomGraph(n, m):
    '''
    Creates and returns a directed graph with n vertices and m edges.
    '''
    newGraph = Graph(n, "directed")

    while m > 0:
        newX = random.randint(0, n-1)
        newY = random.randint(0, n-1)
        newCost = random.randint(0, 100)

        while newGraph.isEdge(newX, newY):
            newX = random.randint(0, n-1)
            newY = random.randint(0, n-1)
        newGraph.addEdge(newX, newY, newCost)
        m -= 1
    return newGraph