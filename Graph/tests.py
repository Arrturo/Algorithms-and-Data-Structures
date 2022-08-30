from graph import Graph, EdgeType, GraphPath


#           0     1      2     3    4      5    6      7
vertexs = ["VI", "RU", "PA", "CO", "CH", "SU", "KE", "RA"]
graph = Graph()
for vertex in vertexs:
    graph.create_vertex(vertex)
keys = [key for key in graph.adjacencies.keys()]
graph.add(EdgeType.undirected, keys[0], keys[4])
graph.add(EdgeType.undirected, keys[0], keys[1])
graph.add(EdgeType.undirected, keys[0], keys[2])

graph.add(EdgeType.undirected, keys[1], keys[7])
graph.add(EdgeType.undirected, keys[1], keys[5])
# graph.add(EdgeType.undirected, keys[1], keys[0])

graph.add(EdgeType.undirected, keys[2], keys[3])
graph.add(EdgeType.undirected, keys[2], keys[6])

graph.add(EdgeType.undirected, keys[3], keys[1])
graph.add(EdgeType.undirected, keys[3], keys[0])


print(graph)
# CH - SU, CH - VI - RU - SU

print("Breadth First Traversal")
graph.traverse_breadth_first(print)

print("Deep First Traversal")
graph.traverse_depth_first(print)

print()
GraphPath.display(keys[4], keys[5], graph)

print()
GraphPath.display(keys[5], keys[4], graph)

print()
GraphPath.display(keys[3], keys[4], graph)

print()
GraphPath.display(keys[4], keys[3], graph)
graph.show()


print("-------GRAPH2-----------")

#           0     1   2    3    4
vertexs = ["A", "M", "L", "O", "N"]
graph = Graph()
for vertex in vertexs:
    graph.create_vertex(vertex)
keys = [key for key in graph.adjacencies.keys()]
print(keys)
graph.add(EdgeType.undirected, keys[0], keys[1])
graph.add(EdgeType.undirected, keys[0], keys[2])

graph.add(EdgeType.undirected, keys[2], keys[3])

graph.add(EdgeType.undirected, keys[1], keys[3])
graph.add(EdgeType.undirected, keys[1], keys[4])

graph.add(EdgeType.undirected, keys[3], keys[4])
print(graph)
print()
GraphPath.display(keys[3], keys[0], graph)

print()
GraphPath.display(keys[1], keys[2], graph)
graph.show()


print("-------GRAPH3-----------")

#           0    1    2    3    4    5    6
vertexs = ["S", "R", "Q", "P", "U", "V", "T"]
graph = Graph()
for vertex in vertexs:
    graph.create_vertex(vertex)
keys = [key for key in graph.adjacencies.keys()]
print(keys)
graph.add(EdgeType.undirected, keys[0], keys[1])

graph.add(EdgeType.undirected, keys[1], keys[2])
graph.add(EdgeType.undirected, keys[1], keys[3])
graph.add(EdgeType.undirected, keys[1], keys[4])

graph.add(EdgeType.undirected, keys[3], keys[4])

graph.add(EdgeType.undirected, keys[4], keys[5])
graph.add(EdgeType.undirected, keys[5], keys[6])
print(graph)
print()
GraphPath.display(keys[0], keys[6], graph)
GraphPath.display(keys[6], keys[0], graph)

print()
GraphPath.display(keys[3], keys[2], graph)
graph.show()
