count_upper = 0

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        stripped = line.strip()
        if stripped and stripped[0].isupper():
            count_upper += 1

print("Строк с заглавной буквы:", count_upper)