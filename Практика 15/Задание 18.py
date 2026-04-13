from datetime import datetime, date

deadline = datetime.strptime("2026-04-01", "%Y-%m-%d").date()
today = date.today()

if deadline < today:
    print("Дедлайн просрочен")
else:
    print("Дедлайн не просрочен")