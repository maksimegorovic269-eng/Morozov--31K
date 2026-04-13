import string

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

clean_text = text.translate(str.maketrans("", "", string.punctuation))

with open("clean.txt", "w", encoding="utf-8") as file:
    file.write(clean_text)

print("Файл clean.txt создан")