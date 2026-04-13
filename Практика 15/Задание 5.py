import csv


with open("data.csv", "r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    rows = [row for row in reader if int(row["age"]) > 25]

with open("over25.csv", "w", encoding="utf-8", newline="") as outfile:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Файл over25.csv создан")