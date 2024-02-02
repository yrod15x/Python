ROW = 8
COLUMN = 4

lista = []

for i in range(ROW):
    columna = []
    for j in range(COLUMN):
        if j % 2 == 0:
            columna.append("#")
        else:
            columna.append('*')
    lista.append(columna)

for i in range(ROW):
    for j in range(COLUMN):
        print(lista[i][j], end="")
    print()