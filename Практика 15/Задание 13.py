from datetime import datetime, timedelta

given_date = datetime.strptime("2026-04-08", "%Y-%m-%d").date()

days_ahead = (7 - given_date.weekday()) % 7
if days_ahead == 0:
    days_ahead = 7

next_monday = given_date + timedelta(days=days_ahead)
print("Следующий понедельник:", next_monday)