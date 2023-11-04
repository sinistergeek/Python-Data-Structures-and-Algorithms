class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if self.queue ==[]:
            print("Queue is Empty")
        else:
            print("Queue is not empty")
    def enqueue(self,element):
        self.queue.insert(0,element)

    def dequeue(self):
        self.queue.pop()

    def size(self):
        print("size of queue is",len(self.queue))

#Code Execution
q=Queue()
q.isEmpty()
#insterting elements
print("instering element no.1")
q.enqueue("apple")
print("instering element no.2")
q.enqueue("banana")
print("insterting element no.3")
q.enqueue("orange")
print("the queue elements are as follows:")
print(q.queue)
print("check if queue is empty?")
q.isEmpty()
#removing elemnts
print("remove first element")
q.dequeue()
print("what is the size of the queue?")
q.size()
print("print contents of the queue")
print(q.queue)
