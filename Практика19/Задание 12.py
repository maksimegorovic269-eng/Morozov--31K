import threading
import time
def download():
    time.sleep(2)
    print("Файл загружен")

threads = []
for _ in range(3):
    t = threading.Thread(target=download)
    threads.append(t)
    t.start()