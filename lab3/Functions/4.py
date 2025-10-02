#PRIME NUMS
def is_it_prime(number):
    for i in range(2, int(number**0.5) + 1):
        if i == 1:
            continue
        elif number % i == 0:
            return False
    return True