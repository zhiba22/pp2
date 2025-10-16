import re

pattern = r'[A-Z][a-z]+'
print(re.findall(pattern, "MyNameIsGPT"))  # Одна заглавная + строчные
