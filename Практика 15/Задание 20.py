error_by_date = {}

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
            parts = line.split()
            log_date = parts[0]
            error_by_date[log_date] = error_by_date.get(log_date, 0) + 1

print("\nОшибки по дням:")
for log_date, count in error_by_date.items():
    print(f"{log_date}: {count}")