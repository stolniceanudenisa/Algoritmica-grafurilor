from Exceptions import exceptionGraph
import copy
from queue import PriorityQueue
import sys


def inf() :
    return 10000000000


class Graph(object) :
    def __init__(self, vertices) :
        self.__vertices = vertices
        self.__dictionaryCosts = {}
        self.__neighbours = {}
        self.__edges = {}
        self.__colorList = [None] * vertices
        # initialize the dictionary of banned colors
        # same as we initialize the neighbours dictionary
        self.__bannedColors = {}
        for i in range(vertices):
            self.__bannedColors[i]=[]
        for i in range(vertices) :
            self.__neighbours[i] = []

    # returns an iterable containing all the vertices
    # in the graph

    def parse_vertices(self) :
        return self.__neighbours.keys()

    # returns the number of vertices in the graph
    def get_nr_of_vertices(self) :
        return self.__vertices

    # returns the number of edges in the graph
    def get_nr_of_edges(self) :
        return len(self.__dictionaryCosts.keys())

    # returns an interable containing
    # all the edges in the graph
    def parse_edges(self) :
        return self.__dictionaryCosts.keys()

    # sets the color of a vertex
    def set_color(self, vertex, color) :
        self.__colorList[vertex] = color

    # gets the color of a vertex
    def get_color(self) :
        return self.__colorList

    # adds to the banned color list of a vertex a color
    def add_banned_color(self, vertex, color) :
        self.__bannedColors[vertex].append(color)

    # gets the banned colors for a vertex
    def getBannedColors(self, vertex) :
        return self.__bannedColors[vertex]


    def get_vertices2(self, vertex) :
        return self.__neighbours[vertex]

    def get_adj_v(self, vertex) :
        return self.__neighbours[vertex]



    # checks if there is an edge from 'vertex1'
    # to 'vertex2'
    # the vertices must be valid
    # otherwise it raises an exception
    # returns true if the edge exists, false otherwise
    def is_edge(self, vertex1, vertex2) :
        if vertex1 not in self.__neighbours.keys() or vertex2 not in self.__neighbours.keys() :
            raise exceptionGraph("Vertices are not valid")
        return vertex2 in self.__neighbours[vertex1]

    # returns the degree of a vertex
    # it raises an exception if the vertex is not valid
    def get_vertex_degree(self, vertex) :
        if vertex not in self.__neighbours.keys() :
            raise exceptionGraph("Vertex does not exist")
        return len(self.__neighbours[vertex])

    # returns an iterable containing all vertices
    # neighbour to a given vertex
    # raises an exception if the vertex is not valid
    def parse_neighbours(self, vertex) :
        if vertex not in self.__neighbours.keys() :
            raise exceptionGraph("Vertex does not exist")
        return self.__neighbours[vertex]

    # adds an edge(vertex1,vertex2,cost) to the graph
    # raises an exception if the vertices do not exist
    # or if the edge already exists
    def add_edge(self, vertex1, vertex2, cost) :
        if vertex1 not in self.__neighbours.keys() or vertex2 not in self.__neighbours.keys() :
            raise exceptionGraph("Vertices do not exist")
        if self.is_edge(vertex1, vertex2) :
            raise exceptionGraph("The edge already exists")
        if vertex1 == vertex2 :
            raise exceptionGraph("There can't be an edge from a vertex to itself")
        self.__neighbours[vertex2].append(vertex1)
        self.__neighbours[vertex1].append(vertex2)
        self.__dictionaryCosts[(vertex1, vertex2)] = cost

    # removes an edge(vertex1,vertex2) from the graph
    # raises an exception if the vertices do not exist
    # or if there is not edge between them
    def remove_edge(self, vertex1, vertex2) :
        if vertex1 not in self.__neighbours.keys() or vertex2 not in self.__neighbours.keys() :
            raise exceptionGraph("Vertices do not exist")

        if not self.is_edge(vertex1, vertex2) :
            raise exceptionGraph("The edge doesn't exist")

        self.__neighbours[vertex2].remove(vertex1)
        self.__neighbours[vertex1].remove(vertex2)

        if (vertex1, vertex2) in self.__dictionaryCosts.keys() :
            self.__dictionaryCosts.pop((vertex1, vertex2))
        else :
            self.__dictionaryCosts.pop((vertex2, vertex1))

    # adds a new vertex to the graph
    # x must not already exist
    # otherwise it raises an exception
    def add_vertex(self, vertex) :
        if vertex in self.__neighbours.keys() :
            raise exceptionGraph("Vertex already exists")
        self.__neighbours[vertex] = []
        self.__vertices += 1

    def is_vertex(self, vertex) :
        return vertex in self.__neighbours.keys()

    # removes a vertex from the graph
    # x must be existent
    # otherwise it raises an exception
    def remove_vertex(self, vertex) :
        if vertex not in self.__neighbours.keys() :
            raise exceptionGraph("Vertex doesn't exist")
        self.__vertices -= 1
        for neighbours in self.__neighbours[vertex] :
            self.__neighbours[neighbours].remove(vertex)
            if (neighbours, vertex) in self.__dictionaryCosts.keys() :
                self.__dictionaryCosts.pop((neighbours, vertex))
            else :
                self.__dictionaryCosts.pop((vertex, neighbours))
        self.__neighbours.pop(vertex)

    # makes a copy of the graph
    def copy_graph(self) :
        copy_graph = Graph(self.__vertices)
        copy_graph.__neighbours = {}
        for vertex in self.__neighbours.keys() :
            copy_graph.__neighbours[vertex] = self.__neighbours[vertex].copy()
        copy_graph.__dictionaryCosts = self.__dictionaryCosts.copy()
        return copy_graph

    # returns the cost from an edge (vertex1, vertex2)
    # raises exceptions if the vertices do not exist
    # or if the edge doesn't exist
    def get_cost(self, vertex1, vertex2) :
        if vertex1 not in self.__neighbours or vertex2 not in self.__neighbours :
            raise exceptionGraph("The vertices are invalid")
        if vertex2 not in self.__neighbours[vertex1] :
            raise exceptionGraph("The edge doesn't exist")
        if (vertex1, vertex2) in self.__dictionaryCosts.keys() :
            return self.__dictionaryCosts[(vertex1, vertex2)]
        else :
            return self.__dictionaryCosts[(vertex2, vertex1)]

    def get_edge_cost(self, vertex1, vertex2) :
        if (vertex1, vertex2) in self.__dictionaryCosts.keys() :
            return self.__dictionaryCosts[(vertex1, vertex2)]
        if (vertex2, vertex1) in self.__dictionaryCosts.keys() :
            return self.__dictionaryCosts[(vertex2, vertex1)]
        return 100000000000

    # changes the cost of an edge
    # raises an exception if the vertices do not exist
    # or if the edge doesn't exist
    def set_cost(self, vertex1, vertex2, cost) :
        if vertex1 not in self.__neighbours or vertex2 not in self.__neighbours :
            raise exceptionGraph("The vertices are invalid")
        if vertex2 not in self.__neighbours[vertex1] :
            raise exceptionGraph("The edge doesn't exist")
        if (vertex1, vertex2) in self.__dictionaryCosts.keys() :
            self.__dictionaryCosts[(vertex1, vertex2)] = cost
        else :
            self.__dictionaryCosts[(vertex2, vertex1)] = cost

    # def get_edge(self, vertex1, vertex2) :
    #   if vertex1 not in self.__neighbours.keys() or vertex2 not in self.__neighbours.keys() :
    #      raise exceptionGraph("Vertices are not valid")
    # if vertex2 not in self.__neighbours[vertex1]:
    #   raise exceptionGraph("The edge doesn't exist")
    # if (vertex1,vertex2) in self.__dictionaryCosts.keys():
    #    return vertex1,vertex2
    # else:
    #   return vertex2,vertex1
    # return 100000000000

    # it is a utility function to find the vertex
    # with the minimum distance value, from the
    # set of vertices
    # not yet included in the shortest path tree
    def get_min_key(self, keyValue, isInMST) :
        minim = inf()
        minIndex = -1
        for i in range(self.get_nr_of_vertices()) :
            if keyValue[i] < minim and isInMST[i] == 0 :
                minim = keyValue[i]
                minIndex = i
        return minIndex

    # function to construct and print MST for a graph
    # using PRIM's algorithm

    def MSTprim(self, startVertex) :
        totalCost = 0
        edges = []
        inMST = []
        parent = []
        valueOfVertex = []
        for it in range(self.get_nr_of_vertices()) :
            # the value of all vertices is infinity
            valueOfVertex.append(inf())

            inMST.append(0)

            parent.append(0)

        parent[startVertex] = -1  # first node is the root of the tree

        inMST[startVertex] = 1  # visited

        valueOfVertex[startVertex] = 0
        nr_of_vertices = self.get_nr_of_vertices()
        currentVertex = startVertex
        for neighbour in self.__neighbours[currentVertex] :
            # print(self.get_edge_cost(neighbour,currentVertex))

            # gets the edge cost between neighbour and currentVertex
            edgeCost = self.get_edge_cost(neighbour, currentVertex)

            # if the value of vertex [ neighbour ] > edge cost
            # and the neighbour isn't already in the MST
            # then it it added
            if valueOfVertex[neighbour] > edgeCost and inMST[neighbour] == 0 :
                valueOfVertex[neighbour] = edgeCost
                parent[neighbour] = currentVertex
        # print("current vertice",currentVertex)
        # print("valueOfVertice",valueOfVertex)
        # print("edge cost",edgeCost)
        # print("len edges", len(edges))
        # print("nr of vertices",nr_of_vertices)

        while len(edges) < nr_of_vertices - 1 :
            currentVertex = self.get_min_key(valueOfVertex, inMST)
            inMST[currentVertex] = 1
            edges.append(
                [currentVertex, parent[currentVertex], self.get_edge_cost(currentVertex, parent[currentVertex])])
            for neighbour in self.__neighbours[currentVertex] :
                edgeCost = self.get_edge_cost(neighbour, currentVertex)
                if valueOfVertex[neighbour] > edgeCost and inMST[neighbour] == 0 :
                    valueOfVertex[neighbour] = edgeCost
                    parent[neighbour] = currentVertex

        print("Parent", parent)
        print("Edges", edges)
        # printing the MST
        edge = 0
        while edge < len(edges) :
            print("edge: " + str(edges[edge][0]) + " - " + str(edges[edge][1]) + " | cost: " + str(edges[edge][2]))
            totalCost += edges[edge][2]
            edge += 1
        print("Total cost: ", totalCost)
        print("That's the minimum spanning tree.")

