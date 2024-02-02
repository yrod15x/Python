num_task = int(input("Numero de Tareas: "))
xentask = []
yanatask = []

for i in range(0, num_task):
    t = int(input())
    xentask.append(t)

for i in range(0, num_task):
    t = int(input())
    yanatask.append(t)

xensum = 0
yanasum = 0

for i in range(0, num_task):
    if i % 2 == 0:
        xensum += xentask[i]
    else:
        xensum += yanatask[i]

for i in range(0, num_task):
    if i % 2 == 0:
        yanasum += yanatask[i]
    else:
        yanasum += xentask[i]

if xensum < yanasum:
    print(xensum)
else:
    print(yanasum)