import re

text = "1234 5678 9012 3456"
digits_only = re.sub(r"\D", "", text)
masked = "*" * (len(digits_only) - 4) + digits_only[-4:]
result = " ".join([masked[i:i+4] for i in range(0, len(masked), 4)])
print(result)
print()