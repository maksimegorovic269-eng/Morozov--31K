with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

longest_line = max(lines, key=len).rstrip("\n")
print("Длина самой длинной строки:", len(longest_line))
print("Самая длинная строка:", longest_line)