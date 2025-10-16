import re

pattern = r'[ ,.]'
print(re.sub(pattern, ':', "Hello, world. Bye"))  # Заменить пробел, запятую или точку на двоеточие
