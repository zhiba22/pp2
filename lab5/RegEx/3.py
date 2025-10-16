import re
pattern = r'[a-z]+_[a-z]+'
print(re.findall(pattern, "one_two three_four five"))  # Последовательности строчных букв, соединённых подчёркиванием