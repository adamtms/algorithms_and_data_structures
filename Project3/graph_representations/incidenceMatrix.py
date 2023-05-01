from testGraph import testGraph

class IncidenceMatrix:
    def __init__(self):
        self.matrix = []
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)
        if len(self.matrix) == 0:
            self.matrix.append([])
        else:
            self.matrix.append([0] * len(self.matrix[0]))

    def addEdge(self, startNode, endNode):
        for index in range(len(self.nodes)):
            if self.nodes[index] == startNode:
                self.matrix[index].append(1)
            elif self.nodes[index] == endNode:
                self.matrix[index].append(-1)
            else:
                self.matrix[index].append(0)

    def getNodeIndex(self, node):
        for index in range(len(self.nodes)):
            if self.nodes[index] == node:
                return index
        return -1

    def checkEdge(self, startNode, endNode):
        startNodeIndex = self.getNodeIndex(startNode)
        endNodeIndex = self.getNodeIndex(endNode)
        for index in range(len(self.matrix[0])):
            if self.matrix[startNodeIndex][index] == 1 and self.matrix[endNodeIndex][index] == -1:
                return True
        return False

    def getEdges(self):
        edges = []
        for edgeIndex in range(len(self.matrix[0])):
            startNodeIndex = -1
            endNodeIndex = -1
            for nodeIndex in range(len(self.nodes)):
                if self.matrix[nodeIndex][edgeIndex] == 1:
                    startNodeIndex = nodeIndex
                elif self.matrix[nodeIndex][edgeIndex] == -1:
                    endNodeIndex = nodeIndex
            edges.append((self.nodes[startNodeIndex], self.nodes[endNodeIndex]))
        return edges

    def getSuccesors(self, node):
        succesors = []
        nodeIndex = self.getNodeIndex(node)
        for edgeIndex in range(len(self.matrix[0])):
            if self.matrix[nodeIndex][edgeIndex] == 1:
                for i in range(len(self.nodes)):
                    if self.matrix[i][edgeIndex] == -1:
                        succesors.append(self.nodes[i])
        return succesors

if __name__ == "__main__":
    testGraph(IncidenceMatrix)