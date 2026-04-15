import re

text = "Visit https://google.com and http://example.org for more info"
result = re.findall(r"https?://[^\s]+", text)
print(result)
print()