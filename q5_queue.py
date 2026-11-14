
MAX = 5          
queue = []

def enqueue(x):
    if len(queue) == MAX:
        print("Queue Overflow")
        return
    queue.append(x)
    print("Enqueued:", x)

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
        return None
    x = queue.pop(0)
    print("Dequeued:", x)
    return x

def display():
    print("Queue:", queue)

enqueue(10)
enqueue(20)
enqueue(30)
display()
dequeue()
display()