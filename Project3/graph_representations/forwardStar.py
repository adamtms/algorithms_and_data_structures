class ForwardStar:
    def __init__(self):
        self.nodes = {}
        
    def addNode(self, node):
        self.nodes[node] = set()

    def addEdge(self, startNode, endNode):
        self.nodes[startNode].add(endNode)

    def checkEdge(self, startNode, endNode):
        return endNode in self.nodes[startNode]

    def getNodes(self):
        return set(self.nodes.keys())

    def getEdges(self):
        edges = []
        for key, s in self.nodes.items():
            for value in s:
                edges.append((key, value))
        return edges

    def getSuccesors(self, node):
        return list(self.nodes[node])
    
    def getNumPredecessorDict(self):
        predecessor_num = {node : 0 for node in self.nodes.keys()}
        for node in self.nodes.values():
            for value in node:
                predecessor_num[value] += 1
        return predecessor_num


if __name__ == "__main__":
    from testGraph import testGraph
    testGraph(ForwardStar)