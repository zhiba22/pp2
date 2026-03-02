a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    if b>c:
        print(a-c)
    else: 
        print(a-b)
elif b>a and b>c:
    if a>c:
        print(b-c)
    else: 
        print(b-a)
elif a>b:
    print(c-b)
else: print(c-a)