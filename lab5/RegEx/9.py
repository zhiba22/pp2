import re

upper_words = re.findall(r"[A-Z][a-z]+", input())
print(*upper_words)
