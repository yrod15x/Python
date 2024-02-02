#Programa que ejecuta acciones con tuplas: imprimirlas, recorrerlas y reasignarlas

platos = ('carne','sushi','salchipapa','pizza','sopa')
print("Los platos del buffet son: ")
for plato in platos:
    print(plato)

#reasignación (aunque no puede modificar valor, se deb hacer completamente nueva)
platos = ('huevos fritos','sushi','salchipapa','pollo','sopa')
print("\nLos nuevos platos son: ")
for plato in platos:
    print(plato)
