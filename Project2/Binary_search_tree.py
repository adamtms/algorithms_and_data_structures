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
    
    def searchParent(self, key):
        prevNode = None
        currentNode = self.head
        while currentNode != None:
            if currentNode.key == key:
                return prevNode
            prevNode = currentNode
            if key > currentNode.key:
                currentNode = currentNode.greater
            else:
                currentNode = currentNode.less
        return None

    def insert(self, key, value):
        if self.search(key) != None:
            print("Node with given key already exists")
            return 
        if self.head == None:
            self.head = Node(key, value)
            return
        prevNode = None
        currentNode = self.head        
        while currentNode != None:
            prevNode = currentNode
            if key > currentNode.key:
                currentNode = currentNode.greater
            else:
                currentNode = currentNode.less
        if key > prevNode.key:
            prevNode.greater = Node(key, value)
        else:
             prevNode.less = Node(key, value)
    
    def findGreatestElemInSubtree(self, currentNode):
        while currentNode.greater != None:
            currentNode = currentNode.greater
        return currentNode

    def remove(self, key):
        nodeToRemove = self.search(key)
        if nodeToRemove == None:
            print("Node with given key doesn't exists")
            return
        if nodeToRemove.less == None:
            if nodeToRemove.greater == None:
                if self.head.key == key:
                    self.head = None
                    return
                parentOfNodeToRemove = self.searchParent(key)
                if key > parentOfNodeToRemove.key:
                    parentOfNodeToRemove.greater = None
                else:
                    parentOfNodeToRemove.less = None
            else:
                nodeToRemove.copyValuesFromAnotherNode(nodeToRemove.greater)

        elif nodeToRemove.greater == None:
            nodeToRemove.copyValuesFromAnotherNode(nodeToRemove.less)
        else:
            nodeToSwitch = self.findGreatestElemInSubtree(nodeToRemove.less)
            parentOfNodeToSwitch = self.searchParent(nodeToSwitch.key)
            if parentOfNodeToSwitch.key == nodeToRemove.key:
                parentOfNodeToSwitch.less = nodeToSwitch.less
            else:
                parentOfNodeToSwitch.greater = nodeToSwitch.less
            nodeToRemove.value = nodeToSwitch.value
            nodeToRemove.key = nodeToSwitch.key

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
    