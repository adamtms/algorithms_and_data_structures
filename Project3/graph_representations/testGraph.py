def addNodes(graph, nodes):
    for node in nodes:
        graph.addNode(node)

def addEdges(graph, edges):
    for startNode, endNode in edges:
        graph.addEdge(startNode, endNode)

def testGraph(Graph):
    graph = Graph()
    nodes1 = [i for i in range(5)]
    edges1 = [ (1, 2), (1, 3), (1, 4), (1, 0), (2, 4), (2, 3), (2, 0), (0, 3), (0, 4) ]
    nodes2 = [i for i in range(5, 10)]
    edges2 = [ (1, 9), (1, 6), (4, 5), (3, 7) ]
    addNodes(graph, nodes1)
    addEdges(graph, edges1)
    print(graph.getNodes())
    print(f"Should be {nodes1}")
    print(graph.getSuccesors(1))
    print(f"Should be {edges1}")
    print(graph.getSuccesors(1))
    print("Should be [2, 3, 4, 0]")
    print(graph.getSuccesors(4))
    print("Should be []")
    print(f"{graph.checkEdge(4, 3)} == False")
    print(f"{graph.checkEdge(1, 2)} == True")
    print(f"{graph.checkEdge(0, 1)} == False")
    print(graph.getNumPredecessorDict())
    print("Should be {0: 2, 1: 0, 2: 1, 3: 3, 4: 3}")
    addNodes(graph, nodes2)
    addEdges(graph, edges2)
    print(graph.getNodes())
    print(f"Should be {nodes1+nodes2}")
    print(graph.getEdges())
    print(f"Should be {edges1 + edges2}")
    print(graph.getSuccesors(1))
    print("Should be [2, 3, 4, 0, 9, 6]")
    print(graph.getSuccesors(4))
    print("Should be [5]")
    print(f"{graph.checkEdge(4, 5)} == True")
    print(f"{graph.checkEdge(1, 2)} == True")
    print(f"{graph.checkEdge(0, 1)} == False")
    print(graph.getNumPredecessorDict())
    print("Should be {0: 2, 1: 0, 2: 1, 3: 3, 4: 3, 5: 1, 6: 1, 7: 1, 8: 0, 9: 1}")
