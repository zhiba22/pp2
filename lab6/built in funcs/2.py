
s = input("Enter string: ")
u = sum(c.isupper() for c in s)
l = sum(c.islower() for c in s)
print("Uppercase:", u, "Lowercase:", l)

