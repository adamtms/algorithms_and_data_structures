from graph_representations.digraphRepresentation import Digraph


def kahn_sort(digraph: Digraph):
    num_predecessor = digraph.getNumPredecessorDict()
    queue = [x for x, y in num_predecessor.items() if y == 0]
    visited = 0
    output = []

    while queue:
        visited += 1
        node = queue.pop()
        output.append(node)
        for neighbour in digraph.getSuccesors(node):
            num_predecessor[neighbour] -= 1
            if num_predecessor[neighbour] == 0:
                queue.append(neighbour)

    if visited != len(num_predecessor):
        print("Topological search not possible")
        return -1
    return output

if __name__ == "__main__":
    from graph_representations.arcList import arcList
    graph = arcList()
    edges = [ (1, 2), (1, 3), (1, 4), (1, 0), (2, 4), (2, 3), (2, 0), (0, 3), (0, 4) ]
    for edge in edges:
        graph.addEdge(*edge)
    print(kahn_sort(graph))