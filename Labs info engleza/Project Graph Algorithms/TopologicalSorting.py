from Graph import Graph

def TopologicalSorting(graph):
    '''
    Verifies if the graph is a Directed Acyclic Graph and if it does, performs a topological sorting.
    input:
        - directed Graph
    output:
        - list sortedList, if the graph is a DAG
        - empty list, if not
    '''
    sortedList = []
    # the queue will be used to store the vertices with no predecessors
    queue = []
    predecessorsCount = {}
    # initialize predecessorsCount
    for vertex in graph.parseVertices():
        predecessorsCount[vertex] = graph.getInDegree(vertex)
        if predecessorsCount[vertex] == 0:
            # if the vertex has no predecessors, add it to the queue
            queue.append(vertex)
    
    while len(queue) > 0:
        vertex = queue.pop(0)
        sortedList.append(vertex)
        # for every vertex, parse the outbound edges and decrease their predecessorsCount
        for neighbour in graph.parseOutboundEdges(vertex):
            predecessorsCount[neighbour] -= 1
            # if the neighbour has no predecessors, add it to the queue
            if predecessorsCount[neighbour] == 0:
                queue.append(neighbour)

    # if vertices from the graph miss from the sortedList, that means they form a cycle,
    # therefore the graph is not a DAG
    if len(sortedList) < graph.getNumberVertices():
        sortedList = []

    return sortedList

def TimesComputing(graph, sortedList, activityDuration):
    '''
    Computes the earliest and latest starting time, the earliest and latest ending time for each activity.
    Computes the total time of the project.
    input:
        - directed Graph
        - sortedList - a list containing the topological sorting
        - activityDuration - a dictionary containing the duration for each activity
    output:
        - list sortedList, if the graph is a DAG
        - empty list, if not
    '''
    FIRST = 0
    LAST = len(sortedList) + 1
    INF = 10000

    # add the fictive nodes: first and last
    graph.addVertex(FIRST)
    graph.addVertex(LAST)

    # insert the fictive first activity
    sortedList.insert(0, FIRST)
    activityDuration[FIRST] = 0

    # add the edges between the FIRST and the vertices with no predecessor
    for vertex in graph.parseVertices():
        if graph.getInDegree(vertex) == 0 and vertex != LAST and vertex != FIRST:
            graph.addEdge(FIRST, vertex)

    # insert the fictive last activity
    sortedList.append(LAST)
    activityDuration[LAST] = 0

    # add the edges between the vertices with no successor and the LAST
    for vertex in graph.parseVertices():
        if graph.getOutDegree(vertex) == 0 and vertex != LAST and vertex != FIRST:
            graph.addEdge(vertex, LAST)

    # initialize the dictionaries for earliestStartTime and earliestEndTime
    earliestStartTime = {}
    earliestStartTime[FIRST] = 0
    for vertex in graph.parseVertices():
        earliestStartTime[vertex] = 0
    earliestEndTime = {}
    earliestEndTime[FIRST] = 0
    for vertex in graph.parseVertices():
        earliestEndTime[vertex] = 0

    # initialize the dictionaries for latestStartTime and lastestEndTime
    latestStartTime = {}
    latestStartTime[FIRST] = 0
    for vertex in graph.parseVertices():
        latestStartTime[vertex] = INF
    latestEndTime = {}
    latestEndTime[FIRST] = 0
    for vertex in graph.parseVertices():
        latestEndTime[vertex] = INF

    # compute the earliest start and end time for each activity
    for index in range(1, len(sortedList)):
        # take as earliestStartTime the maximum earliestEndTime of the predecessors
        for predecessor in graph.parseInboundEdges(sortedList[index]):
            earliestStartTime[sortedList[index]] = max(earliestStartTime[sortedList[index]], earliestEndTime[predecessor])
        # the earliestEndTime will be the earliestStartTime + activityDuration
        earliestEndTime[sortedList[index]] = earliestStartTime[sortedList[index]] + activityDuration[sortedList[index]]

    # compute the latest start and end time for each activity
    latestEndTime[LAST] = earliestEndTime[LAST]
    latestStartTime[LAST] = latestEndTime[LAST] - activityDuration[LAST]
    latestStartTime[FIRST] = 0
    latestEndTime[FIRST] = 0

    for index in range(len(sortedList)-1, 0, -1):
        # take as latestEndTime the minimum latestStartTime of the successors
        for successor in graph.parseOutboundEdges(sortedList[index]):
            latestEndTime[sortedList[index]] = min(latestEndTime[sortedList[index]], latestStartTime[successor])
        # the latestStartTime will be the latestEndTime - activityDuration
        latestStartTime[sortedList[index]] = latestEndTime[sortedList[index]] - activityDuration[sortedList[index]]

    # remove the fictive nodes
    sortedList.pop(0)
    sortedList.pop()

    # determine the critical activities
    criticalActivities = []
    for activity in sortedList:
        if earliestStartTime[activity] == latestStartTime[activity]:
            criticalActivities.append(activity)
    criticalActivities.insert(0,0)
    criticalActivities.append(len(sortedList)+1)

    return earliestStartTime, earliestEndTime, latestStartTime, latestEndTime, criticalActivities

def ActivitiesScheduling(graph, activityDuration):
    sortedList = TopologicalSorting(graph)

    if len(sortedList) == 0:
        raise ValueError("The graph is not a Directed Acyclic Graph.")

    earliestStartTime, earliestEndTime, latestStartTime, latestEndTime, criticalActivities = TimesComputing(graph, sortedList, activityDuration)

    return earliestStartTime, latestStartTime, sortedList, criticalActivities




def test():
    g = Graph(0, "directed")
    activityDuration = {}
    g.addVertex(1)
    g.addVertex(2)
    activityDuration[1] = 2
    activityDuration[2] = 3

    g.addVertex(3)
    g.addEdge(2,3,0)
    activityDuration[3] = 5

    g.addVertex(4)
    g.addEdge(1,4,0)
    activityDuration[4] = 3

    g.addVertex(5)
    g.addEdge(1,5,0)
    activityDuration[5] = 3

    g.addVertex(6)
    g.addEdge(3,6,0)
    g.addEdge(4,6,0)
    g.addEdge(5,6,0)
    activityDuration[6] = 3

    g.addVertex(7)
    g.addEdge(3,7,0)
    activityDuration[7] = 2
    print(activityDuration)
    sortedList = TopologicalSorting(g)
    for vertex in sortedList:
        print(vertex)
    ActivitiesScheduling(g, activityDuration)
    # est, eet, lst, let = TimesComputing(g, sortedList, activityDuration)
    # print(est)
    # print(eet)
    # print(lst)
    # print(let)

