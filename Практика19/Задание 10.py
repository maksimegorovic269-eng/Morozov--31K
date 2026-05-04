import threading
import multiprocessing
import time

def task():
    total = 0
    for i in range(1, 5_000_000):
        total += i
    return total

def threading_test():
    threads = []
    for _ in range(2):
        t = threading.Thread(target=task)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def multiprocessing_test():
    processes = []
    for _ in range(2):
        p = multiprocessing.Process(target=task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    start = time.time()
    threading_test()
    end = time.time()
    print("Threading время:", end - start)

    start = time.time()
    multiprocessing_test()
    end = time.time()
    print("Multiprocessing время:", end - start)