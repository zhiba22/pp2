def odd_numbers(n):
    for i in range(1, n+1):
        if i%2==1:
            yield i

for num in odd_numbers(15):
    print(num)
    