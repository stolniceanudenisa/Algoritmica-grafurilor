from Exceptions import exceptionGraph
import copy


class Graph(object):
    def __init__(self, vertices):
        self.__vertices = vertices
        self.__dictionaryCosts = {}
        self.__neighbours = {}

        for i in range(vertices):
            self.__neighbours[i] = []


    # returns an iterable containing all the vertices
    # in the graph

    def parse_vertices(self):
        return self.__neighbours.keys()

    # returns the number of vertices in the graph
    def get_nr_of_vertices(self):
        return self.__vertices

    # returns the number of edges in the graph
    def get_nr_of_edges(self):
        return len(self.__dictionaryCosts.keys())

    # returns an interable containing
    # all the edges in the graph
    def parse_edges(self):
        return self.__dictionaryCosts.keys()


    # checks if there is an edge from 'vertex1'
    # to 'vertex2'
    # the vertices must be valid
    # otherwise it raises an exception
    # returns true if the edge exists, false otherwise
    def is_edge(self,vertex1,vertex2):
        if vertex1 not in self.__neighbours.keys() or vertex2 not in self.__neighbours.keys():
            raise exceptionGraph("Vertices are not valid")
        return vertex2 in self.__neighbours[vertex1]


    # returns the degree of a vertex
    # it raises an exception if the vertex is not valid
    def get_vertex_degree(self,vertex):
        if vertex not in self.__neighbours.keys():
            raise exceptionGraph("Vertex does not exist")
        return len(self.__neighbours[vertex])


    # returns an iterable containing all vertices
    # neighbour to a given vertex
    # raises an exception if the vertex is not valid
    def parse_neighbours(self,vertex):
        if vertex not in self.__neighbours.keys():
            raise exceptionGraph("Vertex does not exist")
        return self.__neighbours[vertex]

    # adds an edge(vertex1,vertex2,cost) to the graph
    # raises an exception if the vertices do not exist
    # or if the edge already exists
    def add_edge(self,vertex1,vertex2,cost):
        if vertex1 not in self.__neighbours.keys() or vertex2 not in self.__neighbours.keys():
            raise exceptionGraph("Vertices do not exist")
        if self.is_edge(vertex1,vertex2):
            raise exceptionGraph("The edge already exists")
        if vertex1 == vertex2:
            raise exceptionGraph("There can't be an edge from a vertex to itself")
        self.__neighbours[vertex2].append(vertex1)
        self.__neighbours[vertex1].append(vertex2)
        self.__dictionaryCosts[(vertex1,vertex2)] = cost

    # removes an edge(vertex1,vertex2) from the graph
    # raises an exception if the vertices do not exist
    # or if there is not edge between them
    def remove_edge(self,vertex1,vertex2):
        if vertex1 not in self.__neighbours.keys() or vertex2 not in self.__neighbours.keys():
            raise exceptionGraph("Vertices do not exist")

        if not self.is_edge(vertex1,vertex2):
            raise exceptionGraph("The edge doesn't exist")

        self.__neighbours[vertex2].remove(vertex1)
        self.__neighbours[vertex1].remove(vertex2)

        if (vertex1,vertex2) in self.__dictionaryCosts.keys():
            self.__dictionaryCosts.pop((vertex1,vertex2))
        else:
            self.__dictionaryCosts.pop((vertex2,vertex1))

    # adds a new vertex to the graph
    # x must not already exist
    # otherwise it raises an exception
    def add_vertex(self,vertex):
        if vertex in self.__neighbours.keys():
            raise exceptionGraph("Vertex already exists")
        self.__neighbours[vertex] = []
        self.__vertices += 1

    # removes a vertex from the graph
    # x must be existent
    # otherwise it raises an exception
    def remove_vertex(self,vertex):
        if vertex not in self.__neighbours.keys():
            raise exceptionGraph("Vertex doesn't exist")
        self.__vertices -= 1
        for neighbours in self.__neighbours[vertex]:
            self.__neighbours[neighbours].remove(vertex)
            if (neighbours,vertex) in self.__dictionaryCosts.keys():
                self.__dictionaryCosts.pop((neighbours,vertex))
            else:
                self.__dictionaryCosts.pop((vertex,neighbours))
        self.__neighbours.pop(vertex)

    # makes a copy of the graph
    def copy_graph(self):
        copy_graph = Graph(self.__vertices)
        copy_graph.__neighbours = {}
        for vertex in self.__neighbours.keys():
            copy_graph.__neighbours[vertex] = self.__neighbours[vertex].copy()
        copy_graph.__dictionaryCosts = self.__dictionaryCosts.copy()
        return copy_graph

    # returns the cost from an edge (vertex1, vertex2)
    # raises exceptions if the vertices do not exist
    # or if the edge doesn't exist
    def get_cost(self,vertex1,vertex2):
        if vertex1 not in self.__neighbours or vertex2 not in self.__neighbours:
            raise exceptionGraph("The vertices are invalid")
        if vertex2 not in self.__neighbours[vertex1]:
            raise exceptionGraph("The edge doesn't exist")
        if (vertex1, vertex2) in self.__dictionaryCosts.keys():
            return self.__dictionaryCosts[(vertex1,vertex2)]
        else:
            return self.__dictionaryCosts[(vertex2,vertex1)]

    # changes the cost of an edge
    # raises an exception if the vertices do not exist
    # or if the edge doesn't exist
    def set_cost(self,vertex1,vertex2,cost):
        if vertex1 not in self.__neighbours or vertex2 not in self.__neighbours :
            raise exceptionGraph("The vertices are invalid")
        if vertex2 not in self.__neighbours[vertex1] :
            raise exceptionGraph("The edge doesn't exist")
        if (vertex1,vertex2) in self.__dictionaryCosts.keys():
            self.__dictionaryCosts[(vertex1,vertex2)] = cost
        else:
            self.__dictionaryCosts[(vertex2,vertex1)] = cost

