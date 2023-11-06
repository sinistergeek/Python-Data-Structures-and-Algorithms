class Node:
    def __init__(self,data=None):
        self.data = data
        self.reference = None
class Linked_list:
    def __init__(self):
        self.head = None
    def find_middle(self,list):
        counter = 0
        presentNode = self.head
        while presentNode:
            presentNode = presentNode.reference
            counter = counter + 1
        print("size of linked list = ",counter)
        presentNode = self.head

        for i in range((counter-1)//2):
            presentNode = presentNode.reference
        if(counter%2 == 0):
            nextNode =  presentNode.reference
            print("Since the length of linked list is an even number two midle element are : ")
            print(presentNode.data,nextNode.data)
        else:
            print("Since the length of the linked list is an odd number, the middle element is : ")
            print(presentNode.data)
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
linkObj.find_middle(linkObj)
