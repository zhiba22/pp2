c1, r1 = int(input()), int(input())
c2, r2 = int(input()), int(input())

if (c1<=8 and c1>=1) and (c2<=8 and c2>=1) and (r1<=8 and r1>=1) and (r2<=8 and r2>=1):
    if c2 - c1 == r2 - r1:
        print("YES")
    else:
        print("NO")
else:
    print('Enter numbers only from 1 to 8')