class Node():
    def __init__(self, key):
        self.key = key
        self.less = None
        self.greater = None
        self.height = 1

    def __str__(self):
        return f"{self.key}"
    
class AVLTree():
    def __init__(self):
        self.head = None

    def search(self, key):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.key == key:
                return True
            elif key > currentNode.key:
                currentNode = currentNode.greater
            else:
                currentNode = currentNode.less
        return False
    
    def getValues(self):
        nodes = []
        def _get_values_subtree(currentNode, nodes:list):
            if currentNode is None:
                return
            _get_values_subtree(currentNode.less, nodes)
            nodes.append(currentNode.key)
            _get_values_subtree(currentNode.greater, nodes)

        _get_values_subtree(self.head, nodes)
        return nodes
    
    def insert(self, key, currentNode = -1):
        if currentNode == -1:
            self.head = self.insert(key, self.head)
            return
        if currentNode is None:
            return Node(key)
        if key < currentNode.key:
            currentNode.less = self.insert(key, currentNode.less)
        else:
            currentNode.greater = self.insert(key, currentNode.greater)
        currentNode.height = 1 + max(self.getHeight(currentNode.less), self.getHeight(currentNode.greater))

        balanceFactor = self.getBalancedFactor(currentNode)

        if balanceFactor > 1:
            if key < currentNode.less.key:
                return self.rightRotate(currentNode)
            else:
                currentNode.less = self.leftRotate(currentNode.less)
                return self.rightRotate(currentNode)
        
        if balanceFactor < -1:
            if key > currentNode.greater.key:
                return self.leftRotate(currentNode)
            else:
                currentNode.greater = self.rightRotate(currentNode.greater)
                return self.leftRotate(currentNode)
 
        return currentNode

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalancedFactor(self, node):
        if not node:
            return 0
        return self.getHeight(node.less) - self.getHeight(node.greater)
    
    def leftRotate(self, b):
        a = b.greater
        T2 = a.less
        a.less = b
        b.greater = T2
        b.height = 1 + max(self.getHeight(b.less),
                           self.getHeight(b.greater))
        a.height = 1 + max(self.getHeight(a.less),
                           self.getHeight(a.greater))
        return a

    def rightRotate(self, b):
        a = b.less
        T3 = a.greater
        a.greater = b
        b.less = T3
        b.height = 1 + max(self.getHeight(b.less),
                           self.getHeight(b.greater))
        a.height = 1 + max(self.getHeight(a.less),
                           self.getHeight(a.greater))
        return a
    
    def remove(self, key, currentNode = -1):
        if currentNode == -1:
            self.head = self.remove(key, self.head)
            return
        if not currentNode:
            return currentNode
        elif key < currentNode.key:
            currentNode.less = self.remove(key, currentNode.less)
        elif key > currentNode.key:
            currentNode.greater = self.remove(key, currentNode.greater)
        else:
            if currentNode.less is None:
                temp = currentNode.less
                currentNode = None
                return temp
            elif currentNode.greater is None:
                temp = currentNode.less
                currentNode = None
                return temp
            temp = self.getMaxKey(currentNode.less)
            currentNode.key = temp.key
            currentNode.less = self.remove(temp.key, currentNode.less)
        if currentNode is None:
            return currentNode
        
        currentNode.height = 1 + max(self.getHeight(currentNode.less), self.getHeight(currentNode.greater))
        balanceFactor = self.getBalancedFactor(currentNode)

        if balanceFactor > 1:
            if self.getBalancedFactor(currentNode.less) >= 0:
                return self.rightRotate(currentNode)
            else:
                currentNode.less = self.leftRotate(currentNode.less)
                return self.rightRotate(currentNode)
        if balanceFactor < -1:
            if self.getBalancedFactor(currentNode.greater) <= 0:
                return self.leftRotate(currentNode)
            else:
                currentNode.greater = self.rightRotate(currentNode.greater)
                return self.leftRotate(currentNode)
        return currentNode
    
    def getMaxKey(self, currentNode):
        if currentNode is None or currentNode.greater is None:
            return currentNode
        return self.getMaxKey(currentNode.greater)
    

class ForwardStar:
    def __init__(self):
        self.nodes = {}
        
    def addNode(self, node):
        self.nodes[node] = AVLTree()

    def addEdge(self, startNode, endNode):
        self.nodes[startNode].insert(endNode)

    def checkEdge(self, startNode, endNode):
        return self.nodes[startNode].search(endNode)

    def getNodes(self):
        return set(self.nodes.keys())

    def getEdges(self):
        edges = []
        for key, tree in self.nodes.items():
            for value in tree.getValues():
                edges.append((key, value))
        return edges

    def getSuccesors(self, node):
        return self.nodes[node].getValues()
    
    def getNumPredecessorDict(self):
        predecessor_num = {node : 0 for node in self.nodes.keys()}
        for node in self.nodes.values():
            for value in node.getValues():
                predecessor_num[value] += 1
        return predecessor_num


if __name__ == "__main__":
    from testGraph import testGraph
    testGraph(ForwardStar)