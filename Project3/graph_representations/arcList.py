from testGraph import testGraph

class arcList:
    def __init__(self):
        self.edges = []
        
    def addNode(self, node):
        pass

    def addEdge(self, startNode, endNode):
        self.edges.append((startNode, endNode))

    def checkEdge(self, startNode, endNode):
        return (startNode, endNode) in self.edges

    def getEdges(self):
        return self.edges

    def getSuccesors(self, node):
        succesors = []
        for startNode, endNode in self.edges:
            if startNode == node:
                succesors.append(endNode)
        return succesors

if __name__ == "__main__":
    testGraph(arcList)