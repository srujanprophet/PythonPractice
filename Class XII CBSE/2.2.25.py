class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def display(self):
        return self.items

Q = Queue()
n = int(raw_input("Enter No. of Customers : "))
for i in range(n):
    x = raw_input("Enter Customer Name : ")
    Q.enqueue(x)

print Q.display()
