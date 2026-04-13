from datetime import datetime, date

birth_date_str = "2005-05-15"
birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
today = date.today()

age_in_days = (today - birth_date).days
print("Возраст в днях:", age_in_days)