from datetime import datetime

dt2 = datetime.strptime("2024-01-01 14:30", "%Y-%m-%d %H:%M")
formatted = dt2.strftime("%d %B %Y, %H:%M")
print(formatted)