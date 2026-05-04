import threading
from queue import Queue

def worker(q):
    while not q.empty():
        item = q.get()
        print(f"Обработка {item}")
        q.task_done()

q = Queue()

for i in range(10):
    q.put(i)

threads = []
for _ in range(3):
    t = threading.Thread(target=worker, args=(q,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()