import threading
import time
def daemon_task():
    while True:
        print("Работаю в фоне")
        time.sleep(1)

t = threading.Thread(target=daemon_task, daemon=True)
t.start()

time.sleep(3)
print("Главный поток завершен")