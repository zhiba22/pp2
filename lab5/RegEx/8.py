import re

pattern = r'[A-Z][^A-Z]*'
print(re.findall(pattern, "SplitAtUpperCase"))  # Разделить строку по заглавным буквам
