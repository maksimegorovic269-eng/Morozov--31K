from collections import Counter
from datetime import datetime, date, timedelta
import csv
import re
import string

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()
    words = text.translate(str.maketrans("", "", string.punctuation)).split()
    word_count = Counter(words)

for word, count in word_count.most_common():
    print(word, "-", count)