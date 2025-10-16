import re
pattern = r'ab{2,3}'
print(bool(re.fullmatch(pattern, "abb")))  # a с двумя-тремя b
