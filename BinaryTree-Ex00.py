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
                parent_of_index = (index//2)-1
                if self.heap[index]>self.heap[parent_of_index]:
                    temp = self.heap[parent_of_index]
                    self.heap[parent_of_index] = self.heap[index]
                    self.heap[index] = temp
                else:
                    parent_of_index = index//2
                    if self.heap[index]> self.heap[parent_of_index]:
                        temp = self.heap[parent_of_index]
                        self.heap[parent_of_index] = self.heap[index]
                        self.heap[index] = temp
                    self.float_up(parent_of_index)
    def peek(self):
        print(self.heap[0])
    def pop(self):
        if len(self.heap)>=2:
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
    def down_adj(self):
        index = 0
        for i in range(len(self.heap)//2):
            left_child = index*2+1
            if left_child > len(self.heap)-1:
                print(self.heap)
                print("End Point")
                print("Heap value after pop() = ",self.heap)
                return
            right_child = index*2+2
            if right_child > len(self.heap)-1:
                print("right child does not exist")
                if self.heap[index]<self.heap[left_child]:
                    self.swap(index,left_child)
                    index = left_child
                    print("Heap value after pop() = ",self.heap)
                return
            if self.heap[index]<self.heap[left_child]:
                if self.heap[left_child]<self.heap[right_child]:
                    self.swap(index,right_child)
                    index = right_child
                else:
                    self.swap(index,left_child)
                index = left_child
            elif self.heap[index] < self.heap[right_child]:
                self.swap(index,right_child)
                index = right_child
            else:
                print("No change required")
        print("heap value after pop() = ",self.heap)

H = MaxHeap()
print("******pushing values*****")

H.push(165)
print(H.heap)

H.push(60)
print(H.heap)

H.push(179)
print(H.heap)

H.push(400)
print(H.heap)

H.push(6)
print(H.heap)

H.push(275)
print(H.heap)
print("*******poping values*****")

H.pop()
H.pop()
H.pop()
H.pop()
H.pop()
H.pop()
H.pop()
