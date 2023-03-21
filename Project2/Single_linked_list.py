
class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return f"key = {self.key} value = {self.value}"

    def getNodeByKey(self, key):
        if(self.key == key):
            return self
        elif(self.key > key or self.next == None):
            return None
        return self.next.getNodeByKey(key)

    def getMaxLesserElem(self, key):
        if(self.next == None or self.next.key >= key):
            return self
        return self.next.getMaxLesserElem(key)

class SingleLinkedList:
    def __init__(self, head):
        self.head = head

    def __getitem__(self, key):
        item = self.search(key)
        if(item == None):
            print("Given key doesn't exists")
        else:
            print(item)
    
    def search(self, key):
        return self.head.getNodeByKey(key)

    def insert(self, key, value):
        if(self.search(key) != None):
            print("Node with given key already exists")
            return
        if(key < self.head.key):
            self.head = Node(key, value, self.head)
            return
        previousNode = self.head.getMaxLesserElem(key)
        newNode = Node(key, value, previousNode.next)
        previousNode.next = newNode

    def remove(self, key):
        if(self.head.key == key):
            self.head = self.head.next
            return
        previousNode = self.head.getMaxLesserElem(key)
        previousNode.next = previousNode.next.next

if __name__ == '__main__':
    head = Node(0, 0)
    singleLinkedList = SingleLinkedList(head)

    # insert test
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
    singleLinkedList[0]
    singleLinkedList.remove(-9)
    singleLinkedList[-9]
    singleLinkedList[-8]
    singleLinkedList[-1]
    singleLinkedList[1]
    