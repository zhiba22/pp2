'''A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.'''

'''Функция	                    Назначение	                           Пример
re.search(pattern, string)	    Ищет первое совпадение	               re.search("cat", "my cat")
re.findall(pattern, string)	    Возвращает все совпадения списком	   re.findall("\d+", "age 15 and 20") → ['15', '20']
re.match(pattern, string)	    Проверяет совпадение в начале строки   re.match("Hi", "Hi there!")
re.sub(pattern, repl, string)	Заменяет все совпадения	               re.sub("\s+", "_", "hello world") → "hello_world"
re.split(pattern, string)	    Делит строку по шаблону	               re.split("\s+", "one two three") → ['one','two','three']      '''

import re
pattern = r'ab*'
print(bool(re.fullmatch(pattern, "abbb"))) #a с нулём или более b
