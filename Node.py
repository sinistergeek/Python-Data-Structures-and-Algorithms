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

print("DATA VALUE = ",objNode1.data,"REFERENce = ",objNode1.reference)
print("DATA VALUE = ",objNode2.data,"ReFERENCE = ",objNode2.reference)
print("DATA VALUE = ",objNode3.data,"REFERENCE = ",objNode3.reference)
print("DATA VALUE = ",objNode4.data,"REFERENCE = ",objNode3.reference)
