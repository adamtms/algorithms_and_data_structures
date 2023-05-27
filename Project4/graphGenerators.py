import random
from adjacencyList import AdjacencyList
from robertsFlores import robertsFlores
from hierholzer import hierholzer

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

def generateGraphWithEC(n = 100, density = 0.5):
    graph = AdjacencyList()
    for i in range(1, n+1):
        graph.addNode(i)

    for startNode in range(1, n + 1):
        for endNode in range(startNode+1, n):
            if random.random() <= density:
                graph.addEdge(startNode, endNode)
        random.shuffle(graph.nodes[startNode])

    for i in range(1, n):
        if len(graph.nodes[i]) % 2:
            graph.addEdge(i, n)
    
    # for key, nodes in graph.nodes.items():
    #     print(f"{key}: {nodes}")
    
    return graph

def generateGraphWithoutECandHC(n = 100, density = 0.5):
    graph = AdjacencyList()
    for i in range(1, n+1):
        graph.addNode(i)
    
    for startNode in range(1, n + 1):
        for endNode in range(startNode+1, n):
            if random.random() <= density:
                graph.addEdge(startNode, endNode)
        random.shuffle(graph.nodes[startNode])
    
    graph.addEdge(n, 1)
    return graph

if __name__ == "__main__":
    # for i in range(20):
    #     graph = generateGraphWithHC(15)
    #     print(f"{i}: {robertsFlores(graph)}")
    for i in range(20):
        graph = generateGraphWithEC(100, 0.3)
        print(f"{i}: {hierholzer(graph)}")