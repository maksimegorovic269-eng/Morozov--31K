import re
from collections import Counter

logs = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

error_lines = re.findall(r"^.*ERROR.*$", logs, flags=re.MULTILINE)
print("Строки с ERROR:")
for line in error_lines:
    print(line)

dates = re.findall(r"(\d{4}-\d{2}-\d{2})\s+ERROR", logs)
print("\nДаты с ошибками:")
print(dates)

counter = Counter(dates)
print("\nКоличество ошибок по датам:")
for date, count in counter.items():
    print(date, ":", count)