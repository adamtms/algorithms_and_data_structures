from collections import defaultdict
from adjacencyList import AdjacencyList

def robertsFlores(graph):
    path = []
    nodes = graph.getNodes()
    startNode = nodes[0]
    path.append(startNode)
    numberOfVisitedChilds = defaultdict(lambda: 0)

    while(path):
        actualNode = path[-1]
        if numberOfVisitedChilds[actualNode] == len(graph.nodes[actualNode]):
            path.pop(-1)
            numberOfVisitedChilds[actualNode] = 0
            continue
        if len(path) == len(nodes):
            if graph.checkEdge(path[-1], path[0]) and path[1] != path[-1]:
                # print(f"Path: {path}")
                # print("HC found")
                return True
        if graph.nodes[actualNode][numberOfVisitedChilds[actualNode]] not in path:
            path.append(graph.nodes[actualNode][numberOfVisitedChilds[actualNode]])
        numberOfVisitedChilds[actualNode] += 1
    return False
        
def test(nodes, edges):
    graph = AdjacencyList()
    for node in nodes:
        graph.addNode(node)

    for startNode, endNode in edges:
        graph.addEdge(startNode, endNode)

    robertsFlores(graph)
    print()

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6]
    edges = [(6, 1), (1, 2), (2, 3), (3, 5),(3, 4), (4, 5), (5, 6)]
    test(nodes, edges)