class MaxHeap:
    def __init__(self):
        self.heap = []
    def push(self,value):
        self.heap.append(value)
        self.float_up(len(self.heap)-1)
    def float_up(self,index):
        if index==0:
            return
        else:
            if index%2==0:
                parent_of_index=(index//2)-1
                if self.heap[index]>self.heap[parent_of_index]:
                    self.swap(index,parent_of_index)
                else:
                    parent_of_index = index//2
                    if self.heap[index]> self.heap[parent_of_index]:
                        self.swap(index,parent_of_index)
                    self.float_up(parent_of_index)
    def peek(self):
        print(self.heap[0])

    def pop(self):
        if len(self.heap)>2:
            temp = self.heap[0]
            self.heap[0]=self.heap[len(self.heap)-1]
            self.heap[len(self.heap)-1]
            self.heap.pop()
            self.down_adj()
        elif len(self.heap)==1:
            self.heap.pop()
        else:
            print("Nothing to pop")
    def swap(self,index1,index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp


H = MaxHeap()
print("*****Pushing Values***")
print("pushing 165")

H.push(165)
print(H.heap)
print("Pushing 60")

H.push(60)
print(H.heap)
print("Pushing 179")

H.push(179)
print(H.heap)
print("pushing 400")

H.push(400)
print(H.heap)
print("pushing 6")

H.push(6)
print(H.heap)
print("Pushing 275")
H.push(275)
print(H.heap)
