from datetime import datetime

date_list = ["2024-05-01", "2023-12-20", "2025-01-15", "2024-01-10"]

sorted_dates = sorted(date_list, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))
print("Отсортированные даты:")
for d in sorted_dates:
    print(d)