
from UndirectedGraph import Graph

class Utils(object):
    def colorGraph(self,graph):
        vertices=graph.get_nr_of_vertices()
        # the color list
        colorList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", \
                     "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
                     "v", "w", "x", "y", "z"]
        bannedColors =[]
        # we parse every vertex
        for x in range(vertices):

            # we get the list of banned colors for the vertex x
            bannedColors=graph.getBannedColors(x)

            # we parse the color list
            for color in colorList :

                # if the color is not banned
                if color not in bannedColors :
                    # we set to the vertex x the color
                    graph.set_color(x, color)
                    # then, with the adjacency list we get
                    # all his neighbours and ban the color it used
                    for y in graph.get_adj_v(x):

                        graph.add_banned_color(y, color)
                    break
        # we return the colors used
        return graph.get_color()
