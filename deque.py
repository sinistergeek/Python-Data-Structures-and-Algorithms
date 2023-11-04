class Deque:
    def __init__(self):
        self.deque = []
    def addFront(self,element):
        self.deque.append(element)
        print("After adding from front the deque value is :",self.deque)
    def addRear(self,element):
        self.deque.insert(0,element)
        print("After adding from end the deque value is : ",self.deque)
    def removeFront(self):
        self.deque.pop()
        print("After removing from the front the deque value is : ",self.deque)
    def removeRear(self):
        self.deque.pop(0)
        print("After removing from the end the deque value is : ",self.deque)
d = Deque()
print("Adding from front")
d.addFront(1)
print("Adding from front")
d.addFront(2)
print("Adding from Rear")
d.addRear(3)
print("Adding from Rear")
d.addRear(4)
print("Removing from Front")
d.removeFront()
print("Removing from Rear")
d.removeRear()
