count = 0

with open("text.txt", "r") as data:
    for i in data:
        count += 1
print(count)