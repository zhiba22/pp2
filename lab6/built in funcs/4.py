import time
number = int(input())
milisecond = int(input()) / 1000
time.sleep(milisecond)
print(f"Square root of {number} after {milisecond * 1000} miliseconds is {number ** 0.5}")