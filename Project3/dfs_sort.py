from graph_representations.digraphRepresentation import Digraph

from collections import deque

def __dfs(graph: Digraph, node, visited, output):
    visited.add(node)
    neighbors = graph.getSuccesors(node)
    for neighbor in neighbors:
        if neighbor not in visited:
            __dfs(graph, neighbor, visited, output)
    output.appendleft(node)

def dfs_sort(digraph: Digraph):
    visited = set()
    output = deque()
    for node in digraph.getNodes():
        if node not in visited:
            __dfs(graph, node, visited, output)
    return list(output)

if __name__ == "__main__":
    from graph_representations.arcList import arcList
    graph = arcList()
    edges = [ (1, 2), (1, 3), (1, 4), (1, 0), (2, 4), (2, 3), (2, 0), (0, 3), (0, 4) ]
    for edge in edges:
        graph.addEdge(*edge)
    print(dfs_sort(graph))