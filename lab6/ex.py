import os
inp = str(input())
with open('text.txt', 'a') as f:
    f.writelines(os.path.join(inp))
