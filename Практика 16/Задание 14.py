import re

text = "hello hello world"
result = re.findall(r"\b(\w+)\s+\1\b", text)
print(result)
print()