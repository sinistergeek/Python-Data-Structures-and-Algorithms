class Stack_from_Queue:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        if self.queue == []:
            print("Queue is Empty")
        else:
            print("Queue is not empty")
    def enqueue(self,element):
        self.queue.insert(0,element)
    def dequeue(self):
        return self.queue.pop()
    def size(self):
        print("size of queue is",len(self.queue))
    def pop(self):
        for i in range(len(self.queue)-1):
            x=self.dequeue()
            print(x)
            self.enqueue(x)
        print("element removed is",self.dequeue())
sq = Stack_from_Queue()
sq.isEmpty()
print("insterting element apple")
sq.enqueue("apple")
print("instering element banana")
sq.enqueue("banana")
print("instering element orange")
sq.enqueue("orange")
print("instering element 0")
sq.enqueue("0")
for i in range(len(sq.queue)):
    print("The queue elements are as follows:")
    print(sq.queue)
    sq.pop()
    print("check if queue is empty?")
    sq.isEmpty()
    print("remove the last in element")
    print(sq.queue)
