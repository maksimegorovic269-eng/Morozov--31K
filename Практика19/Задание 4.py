import time
import threading

def worker():
    for i in range(5):
        print(threading.current_thread().name)
        time.sleep(1)

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()