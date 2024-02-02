juegos = []

for i in range(6):
    juegos.append(input())
    
ganados = juegos.count('W')

if ganados >= 5:
    print(1)
elif ganados >= 3 and ganados <= 4:
    print(2)
elif ganados >= 1 and ganados <= 2:
    print(3)
else:
    print(-1)       