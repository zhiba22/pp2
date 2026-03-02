a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
    if (b^2+c^2) == a^2:
        print('yes')
    else: 
        print("no")
elif b>a and b>c:
    if (a^2+c^2)==b^2:
        print("yes")
    else:
        print("no")
elif c>b and c>a:
    if (a^2+b^2)==c^2:
        print("yes")
    else: 
        print("no")