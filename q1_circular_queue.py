

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, x):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        x = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return x

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        items = []
        while True:
            items.append(self.arr[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print(items)


q = CircularQueue(5)
for v in [10, 20, 30, 40, 50]:
    q.enqueue(v)
q.dequeue()
q.dequeue()
q.enqueue(60)
q.enqueue(70)
q.display()