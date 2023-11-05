class Node:
    def __init__(self,data=None):
        self.data = data
        self.reference = None
class Linked_list:
    def __init__(self):
        self.head = None
    def traverse(self):
        presentNode = self.head
        while presentNode:
            print("DATA VALUE =",presentNode.data)
            presentNode = presentNode.reference
objNode1 = Node(1)
objNode2 = Node(2)
objNode3 = Node(3)
objNode4 = Node(4)
linkObj = Linked_list()
linkObj.head = objNode1
linkObj.head.reference = objNode2
objNode2.reference = objNode3
objNode3.reference = objNode4
linkObj.traverse()
