class Digraph:
    def __init__(self):
        pass
    def addNode(self, node):
        pass
    def addEdge(self, startNode, endNode):
        pass
    def checkEdge(self, startNode, endNode) -> bool:
        # return true if enge exists, false otherwise
        pass
    def getNodes(self):
        # return list of all nodes
        pass
    def getEdges(self) -> list:
        # return list of all edges
        pass
    def getSuccesors(self, node) -> list:
        # return list of all successors of given node
        pass
    def getNumPredecessorDict(self) -> dict:
        # return dict of all nodes with coresonding number of predecessors
        pass

if __name__ == "__main__":
    from testGraph import testGraph
    testGraph(Digraph)