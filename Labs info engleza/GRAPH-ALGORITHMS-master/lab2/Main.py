import random
from UndirectedGraph import Graph
import Menu
from Exceptions import exceptionGraph
from Exercise4 import get_connected_components,BFS,create_graph

def validate_edge(edge):
    try:
        edge = edge.strip().split(",")
        vertex1 = int(edge[0])
        vertex2 = int(edge[1])
        return vertex1,vertex2
    except exceptionGraph:
        raise exceptionGraph("The input is invalid\n")

def validate_vertex(vertex):
    try:
        vertex = int(vertex)
        return vertex
    except ValueError:
        raise exceptionGraph("Please add an integer\n")

def get_number_of_vertices(graph):
    print("\n The number of vertices in the graph is",graph.get_nr_of_vertices(),'\n')

def get_vertices(graph):
    print("\n The vertices in the graph are:")
    for vertex in graph.parse_vertices():
        print (vertex)

def check_is_edge(graph):
    edge = input("\nInsert the edge(eg. vertex1,vertex2): ")
    vertex1,vertex2 = validate_edge(edge)
    if graph.is_edge(vertex1,vertex2):
        print("Yes, there is an edge from",str(vertex1),"to",str(vertex2))
    else:
        print("No. There is not an edge from",str(vertex1),"to",str(vertex2))
        print("You can try again")

def get_degree_vertex(graph):
    vertex = input("\nInsert the vertex you want to see the degree from: ")
    vertex = validate_vertex(vertex)
    print("Its degree is: ",graph.get_vertex_degree(vertex))

def get_neighbours(graph):
    vertex = input("\nInsert the vertex you want to see the neighbours from: ")
    vertex = validate_vertex(vertex)
    print("Its neighbours are: ")
    for vertices in graph.parse_neighbours(vertex):
        print(vertices, end=' ')

def get_cost(graph):
    print("Input it as <vertex1,vertex2>")
    edge = input("\nInsert the edge you want to see the cost of")
    vertex1,vertex2 = validate_edge(edge)
    print("The cost of this edge is: ",graph.get_cost(vertex1,vertex2))

def modify_cost(graph):
    print("Input it as <vertex1,vertex2>")
    edge = input("\nInsert the edge you want to modify the cost of")
    vertex1,vertex2 = validate_edge(edge)
    cost = input("The new cost is: ")
    cost = validate_vertex(cost)
    graph.set_cost(vertex1,vertex2,cost)

def add_edge(graph):
    edge = input("\nInsert the edge you want to add as <vertex1,vertex2>")
    vertex1,vertex2 = validate_edge(edge)
    cost = input("The cost is: ")
    cost = validate_vertex(cost)
    graph.add_edge(vertex1,vertex2,cost)

def remove_edge(graph):
    edge = input("\nInsert the edge you want to remove as <vertex1,vertex2>")
    vertex1,vertex2 = validate_edge(edge)
    graph.remove_edge(vertex1,vertex2)

def add_vertex(graph):
    vertex = input("\nInsert the vertex you want to add: ")
    vertex = validate_vertex(vertex)
    graph.add_vertex(vertex)

def remove_vertex(graph):
    vertex = input("\nInsert the vertex you want to remove: ")
    vertex = validate_vertex(vertex)
    graph.remove_vertex(vertex)

def copy_the_graph(graph):
    new_graph = graph.copy_graph()
    print(new_graph)

def write_to_file(graph):
    file = input("-> The file you want to write the graph to: ")
    f = open(file,'w')
    number_of_vertices = graph.get_nr_of_vertices()
    number_of_edges = graph.get_nr_of_edges()
    f.write(str(number_of_vertices)+' '+str(number_of_edges)+'\n')

    edges = graph.parse_edges()
    for vertices in edges:
        vertex1 = vertices[0]
        vertex2 = vertices[1]
        cost = graph.get_cost(vertex1,vertex2)
        f.write('Vertex1: '+ str(vertex1) + ' Vertex2: '+str(vertex2)+' Cost: '+str(cost)+'\n')

    for isolatedVertex in graph.parse_vertices():
        if graph.get_vertex_degree(isolatedVertex) == 0:
            f.write(str(isolatedVertex)+' -1 \n')

    f.close()

def read_file(file):
    try:
        f = open(file,'r')
    except exceptionGraph:
        raise exceptionGraph("The file is not available")
    firstLine = f.readline().strip().split()
    graph = Graph(0)
    number_of_vertices = int(firstLine[0])

    line = f.readline()
    while line!="":
        edge = line.strip().split()
        vertex1 = int(edge[0])
        vertex2 = int(edge[1])
        if vertex1 not in graph.parse_vertices():
            graph.add_vertex(vertex1)
        if vertex2 not in graph.parse_vertices() and vertex2!=-1:
            graph.add_vertex(vertex2)
        if len(edge)==3 and vertex1!=vertex2 and not graph.is_edge(vertex1,vertex2):
            graph.add_edge(vertex1,vertex2,int(edge[2]))
        line = f.readline()

    if number_of_vertices != graph.get_nr_of_vertices():
        for vertex in range(number_of_vertices):
            if vertex not in graph.parse_vertices():
                graph.add_vertex(vertex)

    f.close()
    return graph

def random_graph(number_of_vertices,number_of_edges):
    minimum = input("Minimum cost: ")
    minimum = validate_vertex(minimum)
    maximum = input("Maximum cost: ")
    maximum = validate_vertex(maximum)

    if number_of_edges > number_of_vertices*number_of_vertices:
        raise exceptionGraph("The nr of edges must be < than nrVertices^2")

    graph = Graph(number_of_vertices)
    for vertex in range(number_of_edges):
        cost = random.randint(minimum,maximum)
        vertex1 = random.randrange(0,number_of_vertices)
        vertex2 = random.randrange(0,number_of_vertices)
        while graph.is_edge(vertex1,vertex2) or vertex1==vertex2:
            vertex1 = random.randrange(0,number_of_vertices)
            vertex2 = random.randrange(0,number_of_vertices)
        graph.add_edge(vertex1,vertex2,cost)

    return graph

def run():
    while True:
        Menu.menu()
        command = input(">")
        try:
            if command == "file":
                file = input("The file name is: ")
                graph = read_file(file)
                graph_options(graph)
            elif command == "random":
                number_vertices = int(input("Number of vertices: "))
                number_edges = int(input("Number of edges: "))
                graph = random_graph(number_vertices,number_edges)
                graph_options(graph)
            elif command == "exit":
                return
            else:
                print("Inexistent command")
        except Exception as e:
            print("Error: "+str(e))

def graph_options(graph):
    options = {
                "1":get_number_of_vertices,
                "2":get_vertices,
                "3":check_is_edge,
                "4":get_degree_vertex,
                "5":get_neighbours,
                "6":get_cost,
                "7":modify_cost,
                "8":add_edge,
                "9":remove_edge,
                "10":add_vertex,
                "11":remove_vertex,
                "12":copy_the_graph,
                "w":write_to_file,
                "p":print_graph,
                "ex4":connected_components
            }

    while True:
        print("\n->lab1 for LAB1 menu")
        print("->lab2 for LAB2 menu")
        option = input(">")
        if option =='lab1':
            Menu.print_menuLAB1()
        elif option =='lab2':
            Menu.print_menuLAB2()
        elif option in options:
            try:
                options[option](graph)
            except Exception as e:
                print("Error: "+str(e))
        elif option =='exit':
            return
        else:
            print("Invalid choice")

def print_graph(graph):
    number_of_vertices = graph.get_nr_of_vertices()
    number_of_edges = graph.get_nr_of_edges()
    print("Number of vertices: " + str(number_of_vertices) +'\n'+"Number of edges: "+str(number_of_edges))
    edges = graph.parse_edges()
    for vertices in edges:
        vertex1 = vertices[0]
        vertex2 = vertices[1]
        cost = graph.get_cost(vertex1,vertex2)
        print("Vertex1: "+str(vertex1)+" Vertex2: "+str(vertex2)+" Cost: "+str(cost))


def connected_components(graph):
    components = get_connected_components(graph)
    for component in components:
        print("The number of connected components is: "+str(components.index(component)+1))
        print_component(component)
        print("")
    print("\n Number of components are: "+str(len(components)))

def print_component(graph):
    print("The vertices are: ",end=" ")
    for vertex in graph.parse_vertices():
        print(vertex,end=" ")
    print("\nThe edges are: ")
    edges = graph.parse_edges()
    for i in edges:
        vertex1 = i[0]
        vertex2 = i[1]
        cost = graph.get_cost(vertex1,vertex2)
        print("Vertex1: "+str(vertex1)+" Vertex2: "+str(vertex2)+" Cost: "+str(cost))

run()