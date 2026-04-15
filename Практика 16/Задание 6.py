import re

text = "Apple and banana are amazing"
result = re.findall(r"\b[aA]\w*", text)
print(result)
print()