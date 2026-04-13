import re

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r"\b\w+\b", text.lower())
print("1) Количество уникальных слов:", len(set(words)))
