from datetime import datetime

message = "Program started"
current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

with open("messages.log", "a", encoding="utf-8") as file:
    file.write(f"{current_time} {message}\n")

print("Сообщение записано в messages.log")