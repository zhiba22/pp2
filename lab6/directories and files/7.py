with open("text.txt", 'r') as file:
    data = file.read()

with open("text2.txt", 'w') as file:
    file.write(data)