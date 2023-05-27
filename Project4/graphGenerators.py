import random
from adjacencyList import AdjacencyList
from robertsFlores import robertsFlores

def generateGraphWithHC(n = 100, density = 0.5):
    graph = AdjacencyList()
    for i in range(1, n+1):
        graph.addNode(i)
    cycle = [x for x in range(1, n+1)]
    random.shuffle(cycle)
    if cycle[1] == cycle[-1]:
        cycle[1], cycle[2] = cycle[2], cycle[1]
    for i in range(len(cycle) - 1, -1, -1):
        graph.addEdge(cycle[i], cycle[i-1])
    for startNode in range(1, n):
        for endNode in range(startNode+1, n):
            if random.random() <= density:
                graph.addEdge(startNode, endNode)
        random.shuffle(graph.nodes[startNode])
    return graph

if __name__ == "__main__":
    for i in range(20):
        graph = generateGraphWithHC(15)
        print(f"{i}: {robertsFlores(graph)}")