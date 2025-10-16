import re

pattern = r'a.*b$'
print(bool(re.match(pattern, "axyzb")))  # a + что угодно + b в конце
