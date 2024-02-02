rondas = int(input())
dados = []
antonia, david = 100, 100

for i in range(rondas):
    dados.append(input().split())

for dice in dados:
    if int(dice[0]) > int(dice[1]):
        david -= int(dice[0])
    elif int(dice[0]) < int(dice[1]):
         antonia -= int(dice[1])
 
print(antonia)
print(david)