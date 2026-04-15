import re

text = "I love Python programming"
result = bool(re.search(r"Python", text))
print(result)
print()