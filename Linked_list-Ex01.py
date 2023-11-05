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
            print("DATA VALUE = ",presentNode.data)
            presentNode = presentNode.reference
    def insert_at_Beginning(self,data):
        new_data = Node(data)
        new_data.reference = self.head
        self.head = new_data
objNode1 = Node(1)
objNode2 = Node(2)
objNode3 = Node(3)
objNode4 = Node(4)
linkObj = Linked_list()

#head of the linked list to first object
linkObj.head = objNode1
#reference of the first node object to second object
linkObj.head.reference = objNode2
objNode2.reference = objNode3
objNode3.reference = objNode4
linkObj.insert_at_Beginning(5)
linkObj.traverse()
