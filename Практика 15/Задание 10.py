with open("input.txt", "r", encoding="utf-8") as file:
    unique_lines = []
    seen = set()

    for line in file:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)

with open("unique_lines.txt", "w", encoding="utf-8") as file:
    file.writelines(unique_lines)

print("Файл unique_lines.txt создан")