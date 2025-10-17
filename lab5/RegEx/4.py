import re

pattern = r'[A-Z][a-z]+'
print(re.findall(pattern, "ThisIsLab5"))  # Одна заглавная + строчные
