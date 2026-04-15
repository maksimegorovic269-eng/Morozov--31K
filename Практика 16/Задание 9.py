import re

text = "pass1234"
result = bool(re.fullmatch(r"(?=.*\d).{8,}", text))
print(result)
print()