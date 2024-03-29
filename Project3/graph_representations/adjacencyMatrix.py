class AdjacencyMatrix:
    def __init__(self):
        self.matrix = []
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)
        if len(self.matrix) == 0:
            self.matrix.append([0])
        else:
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * len(self.nodes))

    def addEdge(self, startNode, endNode):
        startNodeIndex = self.nodes.index(startNode)
        endNodeIndex = self.nodes.index(endNode)
        self.matrix[startNodeIndex][endNodeIndex] = 1

    def checkEdge(self, startNode, endNode):
        return self.matrix[startNode][endNode] == 1
    
    def getNodes(self):
        return set(self.nodes)

    def getEdges(self):
        edges = []
        for startIndex in range(len(self.nodes)):
            for endIndex in range(len(self.nodes)):
                if self.matrix[startIndex][endIndex] == 1:
                    edges.append((startIndex, endIndex))
        return edges
    
    def getSuccesors(self, node):
        startIndex = self.nodes.index(node)
        succesors = []
        for endIndex in range(len(self.nodes)):
            if self.matrix[startIndex][endIndex] == 1:
                succesors.append(endIndex)
        return succesors
    
    def getNumPredecessorDict(self):
        predecessor_num = {node : 0 for node in self.nodes}
        for row in self.matrix:
            for value, node in zip(row, self.nodes):
                if value:
                    predecessor_num[node] += 1
        return predecessor_num

if __name__ == "__main__":
    from testGraph import testGraph
    testGraph(AdjacencyMatrix)