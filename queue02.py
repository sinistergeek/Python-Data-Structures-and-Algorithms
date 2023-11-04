class Queue:
    def __init__(self):
        self.inputStack=Stack()
        self.outputStack=Stack()
    def enqueue(self,element):
        self.inputStack.push(element)
    def dequeue(self):
        if self.outputStack.isEmpty():
            for i in range(len(self.inputStack.stack)-1):
                x=self.inputStack.pop()
                self.outputStack.push(x)
            print("popping out value=",self.inputStack.pop())
        else:
            print("popping out value=",self.outputStack.pop())
#Define Stack Class
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return self.stack == []
Q=Queue()
print("insert value 1")
Q.enqueue(1)
print("insert value 2")
Q.enqueue(2)
print("insert value 3")
Q.enqueue(3)
print("insert value 4")
Q.enqueue(4)
print("dequeue operation")
Q.dequeue()
Q.dequeue()
print("insert value 7")
Q.enqueue(7)
Q.enqueue(8)
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
