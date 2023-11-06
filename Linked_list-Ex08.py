class Node:
    def __init__(self,data = None):
        self.data = data
        self.refNext = None
class Linked_list:
    def __init__(self):
        self.head = None
    def reverse(self):
        previous = None
        presentNode = self.head
        nextval = presentNode.refNext
        while nextval != None:
            presentNode.refNext = previous
            previous = presentNode
            presentNode = nextval
            nextval = nextval.refNext
        presentNode.refNext = previous
        self.head = presentNode
    def traverse(self):
        presentNode = self.head
        while presentNode:
            print("DATA VALUE = ",presentNode.data)
            presentNode = presentNode.refNext

objNode1 = Node(1)
objNode2 = Node(2)
objNode3 = Node(3)
objNode4 = Node(4)
linkObj = Linked_list()
#head of the linked list to first object
linkObj.head = objNode1
#reference of the first node object to second object
linkObj.head.refNext = objNode2
objNode2.refNext = objNode3
objNode3.refNext = objNode4
print("traverse before reversing")
linkObj.traverse()
linkObj.reverse()
print("traverse after reversing")
linkObj.traverse()
