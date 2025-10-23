lst = ["apple", "banana", "cherry"]       
with open("out.txt", "w") as f:        
    f.writelines("\n".join(lst))          
