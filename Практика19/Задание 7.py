from queue import Queue

q = Queue()

def producer():
    for i in range(5):
        q.put(i)

def consumer():
    while not q.empty():
        print(q.get())

producer()
consumer()