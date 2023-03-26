import sys

sys.setrecursionlimit(int(1e8))

class Node:
    def __init__(self, key, value, less = None, greater = None):
        self.key = key
        self.value = value
        self.less = less
        self.greater = greater

    def __str__(self):
        return f"key = {self.key} value = {self.value}"
    
    def copyValuesFromAnotherNode(self, node):
        self.key = node.key
        self.value = node.value
        self.less = node.less
        self.greater = node.greater

class BinarySearchTree:
    def __init__(self, head=None):
        self.head = head

    def __getitem__(self, key):
        item = self.search(key)
        if item == None:
            print("Given key doesn't exists")
        else:
            print(item)

    def printInOrder(self, currentNode):
        if currentNode == None:
            return 
        self.printInOrder(currentNode.less)
        print(currentNode.key , end=' ')
        self.printInOrder(currentNode.greater)
    
    def printAll(self):
        self.printInOrder(self.head)

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
        return currentNode
    
    def getMaxValue(self, currentNode):
        if currentNode is None or currentNode.greater is None:
            return currentNode
        return self.getMaxValue(currentNode.greater)

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
        return currentNode

if __name__ == "__main__":
    tree = BinarySearchTree()
    # insert test
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
    