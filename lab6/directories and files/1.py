
# A directory is a collection of files and subdirectories. Python has os module that provides

import os
path = "."
print("Dirs:", [d for d in os.listdir(path) if os.path.isdir(d)])
print("Files:", [f for f in os.listdir(path) if os.path.isfile(f)])


'''
print(getcwd()) - prints current directory
os.chdir('C:\Python') - change directory
files = os.listdir(os.getcwd()) - list all elements of a directory 
print(files)

os.mkdir('Pictures')
os.makedirs('Pictures\Pics\November', exist_ok = True)
os.rmdir('Pictures') - remove directory


current_directory = os.getcwd()
file1 = 'text1.txt'

combined = os.path.join(current_directory, 'Folder1', 'One More Folder', file1)
print(combined)
print(os.path.exists(combined)) - will return True or False
print(os.path.isfile(combined))
print(os.path.isdir(combined))

os.stat(combined) - gives us statistics
'''