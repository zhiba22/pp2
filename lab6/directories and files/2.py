import os
p = input("Enter path: ")
print("Exists:", os.access(p, os.F_OK))
print("Readable:", os.access(p, os.R_OK))
print("Writable:", os.access(p, os.W_OK))
print("Executable:", os.access(p, os.X_OK))