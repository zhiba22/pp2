import os
p = input("Enter path: ")
if os.path.exists(p):
    print("Filename:", os.path.basename(p))
    print("Dirname:", os.path.dirname(p))