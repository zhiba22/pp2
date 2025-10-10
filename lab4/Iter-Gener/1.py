def squares_up_to_n(n):
    for i in range(1, n + 1):
        yield i * i 

for square in squares_up_to_n(5):
    print(square)





'''return — просто возвращает одно значение и завершает функцию.

yield — возвращает значение и запоминает место, где остановился.'''

# Обычная функция возвращает сразу список (всю память тратим сразу)
def squares_list(n):
    return [i*i for i in range(n)]

# Генератор возвращает по одному элементу
def squares_gen(n):
    for i in range(n):
        yield i*i
