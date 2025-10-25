import os
p = input("Enter path: ")
print("Exists:", os.access(p, os.F_OK)) 
print("Readable:", os.access(p, os.R_OK))
print("Writable:", os.access(p, os.W_OK))
print("Executable:", os.access(p, os.X_OK))

'''
F_OK - tests the existence of the path
R_OK - Tests the readability of the path
W_OK - Tests the writability of the path
X_OK - Tests the executability of the path'''

# os._exit()	Exits the process with the specified status
# os.abort()	Terminates a running process immediately
# os.access()	Uses the real uid/gid to check access to a path