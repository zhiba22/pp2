import os
p = "delete_me.txt"                       
if os.path.exists(p) and os.access(p, os.W_OK): 
    os.remove(p)                          
