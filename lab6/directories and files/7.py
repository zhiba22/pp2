import os
with open("text.txt", 'r') as file:
    data = file.read()

with open("text2.txt", 'w') as file:
    file.write(data)

#open(... , 'r') - 'r' for read, 'w' for write, 'a' for append, 'b' for binary, 't' for text