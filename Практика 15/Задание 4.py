import csv


ages = []

with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        ages.append(int(row["age"]))

average_age = sum(ages) / len(ages)
print("Средний возраст:", average_age)
