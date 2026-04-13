with open("file1.txt", "r", encoding="utf-8") as f1, \
     open("file2.txt", "r", encoding="utf-8") as f2, \
     open("result.txt", "w", encoding="utf-8") as result:
    result.write(f1.read())
    result.write("\n")
    result.write(f2.read())

print("Файл result.txt создан")