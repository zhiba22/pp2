import string                             # Модуль string содержит ascii_uppercase = 'A'...'Z'
for c in string.ascii_uppercase:          
    open(f"{c}.txt", "w").close()         
