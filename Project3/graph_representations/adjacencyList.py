class AdjacencyList:
    def __init__(self):
        self.nodes = {}
        
    def addNode(self, node):
        self.nodes[node] = []

    def addEdge(self, startNode, endNode):
        self.nodes[startNode].append(endNode)

    def checkEdge(self, startNode, endNode):
        return endNode in self.nodes[startNode]

    def getNodes(self):
        return set(self.nodes.keys())

    def getEdges(self):
        edges = []
        for key, values in self.nodes.items():
            for value in values:
                edges.append((key, value))
        return edges

    def getSuccesors(self, node):
        return self.nodes[node]
    
    def getNumPredecessorDict(self):
        predecessor_num = {node : 0 for node in self.nodes.keys()}
        for values in self.nodes.values():
            for value in values:
                predecessor_num[value] += 1
        return predecessor_num

if __name__ == "__main__":
    from testGraph import testGraph
    testGraph(AdjacencyList)