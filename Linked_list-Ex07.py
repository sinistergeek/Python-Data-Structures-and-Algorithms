class Node:
    def __init__(self,data = None):
        self.data = data
        self.refNext = None
        self.refPrev = None
class dLinked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,data):
        new_data = Node(data)
        presentNode = self.head
        while presentNode.refNext != None:
            presentNode = presentNode.refNext
        presentNode.refNext = new_data
        new_data.refPrev = presentNode
        self.tail = new_data
    def traverse(self):
        presentNode = self.head
        while presentNode:
            print("DATA VALuE = ",presentNode.data)
            presentNode = presentNode.refNext
    def traverseReverse(self):
        presentNode = self.tail
        while presentNode:
            print("DATA VALUE = ",presentNode.data)
            presentNode = presentNode.refPrev
    def remove(self,removeObj):
        presentNode = self.head
        presentNodeTail = self.tail
        while presentNode.refNext != None:
            if(presentNode.refNext == removeObj):
                presentNode.refNext = removeObj.refNext
            presentNode = presentNode.refNext
        while presentNodeTail.refPrev != None:
            if(presentNodeTail.refPrev == removeObj):
                presentNodeTail.refPrev = removeObj.refPrev
            presentNodeTail = presentNodeTail.refPrev
objNode1 = Node(1)
objNode2 = Node(2)
objNode3 = Node(3)
objNode4 = Node(4)
dlinkObj = dLinked_list()
#head of the linked list to first object
dlinkObj.head = objNode1
dlinkObj.tail = objNode4
#reference of the first node object to second object
dlinkObj.head.refNext = objNode2
dlinkObj.tail.refPrev = objNode3
objNode2.refNext = objNode3
objNode3.refNext = objNode4
objNode4.refPrev = objNode3
objNode3.refPrev = objNode2
objNode2.refPrev = objNode1
print("Appending Values")
dlinkObj.append(8)
dlinkObj.append(9)
print("traversing forward after Append")
dlinkObj.traverse()
print("traversing reverse after Append")
dlinkObj.traverseReverse()
print("Removing Values")
dlinkObj.remove(objNode2)
print("traversing forward after Remove")
dlinkObj.traverse()
print("traversing reverse after Remove")
dlinkObj.traverseReverse()

