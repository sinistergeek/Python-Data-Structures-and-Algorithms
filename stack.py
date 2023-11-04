# Define Stack Class
class Stack:
    #Constructor
    def __init__(self,n):
        self.stack = []
        self.size = n
    #push method
    def push(self,element):
        if len(self.stack)==self.size:
            print("no more elemensts can be appended as the stack is full")
        else:
            self.stack.append(element)

    #pop method
    def pop(self):
        if(self.stack == []):
            print("Stack is empty. Nothing to POP!!")
        else:
            self.stack.pop()

s= Stack(3)
s.push(6)
s.push(2)
print(s.stack)
s.pop()
print(s.stack)


