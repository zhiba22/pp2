import re

def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))

print(snake_to_camel("python_regex_exercises"))  # Конвертировать snake_case → CamelCase
