from testGraph import testGraph

class adjacencyList:
    def __init__(self):
        self.nodes = {}
        
    def addNode(self, node):
        self.nodes[node] = []

    def addEdge(self, startNode, endNode):
        self.nodes[startNode].append(endNode)

    def checkEdge(self, startNode, endNode):
        return endNode in self.nodes[startNode]

    def getEdges(self):
        edges = []
        for key, values in self.nodes.items():
            for value in values:
                edges.append((key, value))
        return edges

    def getSuccesors(self, node):
        return self.nodes[node]

if __name__ == "__main__":
    testGraph(adjacencyList)