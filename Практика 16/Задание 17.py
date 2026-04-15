import re

log = "2026-04-01 INFO Program started"
match = re.match(r"(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR)\s+(.+)", log)
if match:
    date, level, message = match.groups()
    print("Дата:", date)
    print("Уровень:", level)
    print("Сообщение:", message)
print()