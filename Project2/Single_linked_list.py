class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return f"key = {self.key} value = {self.value}"

class SingleLinkedList:
    def __init__(self, head = None):
        self.head = head

    def __getitem__(self, key):
        item = self.search(key)
        if item == None :
            print("Given key doesn't exists")
        else:
            print(item)
    
    def getMaxLesserElem(self, key):
        currentNode = self.head
        while currentNode.next != None and currentNode.next.key < key:
            currentNode = currentNode.next
        return currentNode

    def search(self, key):
        if self.head == None:
            return None
        currentNode = self.head
        while currentNode != None and currentNode.key != key:
            currentNode = currentNode.next
        return currentNode

    def insert(self, key, value):
        if self.search(key) != None:
            print("Node with given key already exists")
            return
        if self.head == None:
            self.head = Node(key, value)
            return
        if key < self.head.key:
            self.head = Node(key, value, self.head)
            return
        previousNode = self.getMaxLesserElem(key)
        newNode = Node(key, value, previousNode.next)
        previousNode.next = newNode

    def remove(self, key):
        if self.head.key == key:
            self.head = self.head.next
            return
        previousNode = self.getMaxLesserElem(key)
        previousNode.next = previousNode.next.next

if __name__ == '__main__':
    singleLinkedList = SingleLinkedList()

    # insert test
    singleLinkedList.insert(0, 0)
    singleLinkedList.insert(-1, 1)
    singleLinkedList.insert(1, 1)
    singleLinkedList.insert(-2, 2)
    singleLinkedList.insert(2, 2)
    singleLinkedList.insert(-3, 3)
    singleLinkedList.insert(3, 3)
    singleLinkedList.insert(-4, 4)
    singleLinkedList.insert(4, 4)
    singleLinkedList.insert(-5, 5)
    singleLinkedList.insert(5, 5)
    singleLinkedList.insert(-6, 6)
    singleLinkedList.insert(6, 6)
    singleLinkedList.insert(-7, 7)
    singleLinkedList.insert(7, 7)
    singleLinkedList.insert(-8, 8)
    singleLinkedList.insert(8, 8)
    singleLinkedList.insert(-9, 9)
    singleLinkedList.insert(9, 9)
    singleLinkedList[0]
    singleLinkedList[-1]
    singleLinkedList[1]
    singleLinkedList[-2]
    singleLinkedList[2]
    singleLinkedList[-3]
    singleLinkedList[3]
    singleLinkedList[-4]
    singleLinkedList[4]
    singleLinkedList[-5]
    singleLinkedList[5]
    singleLinkedList[-6]
    singleLinkedList[6]
    singleLinkedList[-7]
    singleLinkedList[7]
    singleLinkedList[-8]
    singleLinkedList[8]
    singleLinkedList[-9]
    singleLinkedList[9]

    #remove test
    singleLinkedList.remove(0)
    singleLinkedList.remove(1)
    singleLinkedList.remove(9)
    singleLinkedList[9]
    singleLinkedList[1]
    singleLinkedList[0]