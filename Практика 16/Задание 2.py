import re

text = "There are 12 apples and 5 bananas"
result = re.findall(r"\d+", text)
print(result)
print()