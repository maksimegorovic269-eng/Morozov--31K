from multiprocessing import Pool

def heavy(x):
    return sum(i*i for i in range(1000000))

if __name__ == "__main__":
    with Pool(4) as p:
        print(p.map(heavy, range(4)))