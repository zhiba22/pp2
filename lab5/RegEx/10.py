import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

camel_case_input = input()
snake_case_output = camel_to_snake(camel_case_input)    
print("Converted snake_case string:", snake_case_output)
