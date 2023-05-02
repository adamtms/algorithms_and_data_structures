from testGraph import testGraph

class Digraph:
    def __init__(self):
        pass
    def addNode(self, node):
        pass
    def addEdge(self, startNode, endNode):
        pass
    def checkEdge(self, startNode, endNode):
        # return true if enge exists, false otherwise
        pass
    def getEdges(self):
        # return list of all edges
        pass
    def getSuccesors(self, node):
        # return list of all successors of given node
        pass
    def getNumPredecessorDict(self):
        # return dict of all nodes with coresonding number of predecessors
        pass

if __name__ == "__main__":
    testGraph(Digraph)