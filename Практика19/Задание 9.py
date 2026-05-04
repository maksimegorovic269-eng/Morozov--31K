from multiprocessing import Process

def calc():
    s = sum(range(1, 100000))
    print(s)

if __name__ == "__main__":
    p1 = Process(target=calc)
    p2 = Process(target=calc)

    p1.start()
    p2.start()

    p1.join()
    p2.join()