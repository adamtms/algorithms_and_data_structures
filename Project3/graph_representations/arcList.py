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
    
    def getNumPredecessorDict(self):
        # if a node is not connected to any other it will not be returned
        predecessor_num = {}
        for tail, head in self.edges:
            if tail not in predecessor_num:
                predecessor_num[tail] = 0

            if head not in predecessor_num:
                predecessor_num[head] = 1
                continue
            predecessor_num[head] += 1
        return predecessor_num

if __name__ == "__main__":
    from testGraph import testGraph
    testGraph(arcList)