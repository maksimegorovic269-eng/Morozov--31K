from datetime import datetime

now = datetime.now()
timestamp = now.timestamp()
restored = datetime.fromtimestamp(timestamp)

print("Текущая дата и время:", now)
print("UNIX timestamp:", timestamp)
print("Обратно из timestamp:", restored)