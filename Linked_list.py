class Node:
    def __init__(self,data=None):
        self.data = data
        self.reference = None
objNode1 = Node(1)
objNode2 = Node(2)
objNode3 = Node(3)
objNode4 = Node(4)
objNode1.reference = objNode2
objNode2.reference = objNode3
objNode3.reference = objNode4
objNode4.reference = None
presentNode = objNode1
while presentNode:
    print("DATA VALUE = ",presentNode.data)
    presentNode = presentNode.reference
