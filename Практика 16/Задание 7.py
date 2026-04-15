import re

text = "+37112345678"
result = bool(re.fullmatch(r"\+371\d{8}", text))
print(result)
print()