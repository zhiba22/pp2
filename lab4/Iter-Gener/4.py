def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for value in squares(3, 7):
    print(value)
