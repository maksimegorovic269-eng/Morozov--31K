import re

text = "192.168.1.1"
pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\." \
          r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\." \
          r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\." \
          r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
result = bool(re.fullmatch(pattern, text))
print(result)
print()