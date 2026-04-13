from datetime import datetime, timedelta

start_date = datetime.strptime("2026-04-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2026-04-10", "%Y-%m-%d").date()

work_days = 0
current = start_date

while current <= end_date:
    if current.weekday() < 5:
        work_days += 1
    current += timedelta(days=1)

print("Количество рабочих дней:", work_days)