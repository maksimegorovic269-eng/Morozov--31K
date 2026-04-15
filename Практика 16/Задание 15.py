import re

text = "hello world python"
result = re.sub(r"\b\w", lambda m: m.group().upper(), text)
print(result)
print()