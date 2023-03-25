import sys

sys.setrecursionlimit(int(1e8))

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.less = None
        self.greater = None
        self.height = 1

    def __str__(self):
        return f"key = {self.key} value = {self.value} less = {self.less} greater = {self.greater}"
    
class AVLTree():
    def __init__(self):
        self.head = None

    def search(self, key):
        currentNode = self.head
        while currentNode != None:
            if currentNode.key == key:
                return currentNode
            elif key > currentNode.key:
                currentNode = currentNode.greater
            else:
                currentNode = currentNode.less
        return None

    def __getitem__(self, key):
        item = self.search(key)
        if item == None:
            print("Given key doesn't exists")
        else:
            print(item)
    
    def insert(self, key, value, currentNode = -1):
        if currentNode == -1:
            self.head = self.insert(key, value, self.head)
            return
        if currentNode == None:
            return Node(key, value)
        if key < currentNode.key:
            currentNode.less = self.insert(key, value, currentNode.less)
        else:
            currentNode.greater = self.insert(key, value, currentNode.greater)
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
            if currentNode.less == None:
                temp = currentNode.less
                currentNode = None
                return temp
            elif currentNode.greater == None:
                temp = currentNode.less
                currentNode = None
                return temp
            temp = self.getMaxValue(currentNode.less)
            currentNode.key = temp.key
            currentNode.value = temp.value
            currentNode.less = self.remove(temp.key, currentNode.less)
        if currentNode == None:
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
    
    def getMaxValue(self, currentNode):
        if currentNode is None or currentNode.greater is None:
            return currentNode
        return self.getMaxValue(currentNode.greater)

if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(0,0)
    tree.insert(-4, 4)
    tree.insert(4, 4)
    tree.insert(-5, 5)
    tree.insert(5, 5)
    tree.insert(-6, 6)
    tree.insert(6, 6)
    tree.insert(-7, 7)
    tree.insert(7, 7)
    tree.insert(-8, 8)
    tree.insert(8, 8)
    tree.insert(-9, 9)
    tree.insert(9, 9)
    tree.insert(-1, 1)
    tree.insert(1, 1)
    tree.insert(-2, 2)
    tree.insert(2, 2)
    tree.insert(-3, 3)
    tree.insert(3, 3)

    #remove test
    tree.remove(0)
    tree.remove(1)
    tree.remove(-4)
    tree.remove(9)
    tree.remove(-3)
    tree.remove(9)

    