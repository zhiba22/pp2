''' 
A directory is a collection of files and subdirectories. Python has os module that provides'''

import os
path = "."
print("Dirs:", [d for d in os.listdir(path) if os.path.isdir(d)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])
