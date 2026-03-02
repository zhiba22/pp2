a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())
a3, b3 = map(int,input().split())
a4, b4 = map(int,input().split())

team1 = a1 + a2 + a3 + a4
team2 = b1 + b2+b3+b4

if team1 > team2:
    print('yerbols team won')
elif team2 > team1: print('aidyns team won')
else: print('its draw')