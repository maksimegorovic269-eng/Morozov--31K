from datetime import datetime

date_str = "2024-12-31"
dt = datetime.strptime(date_str, "%Y-%m-%d")

print("День:", dt.day)
print("Месяц:", dt.month)
print("Год:", dt.year)