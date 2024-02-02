#Programa que recorre una lista con un ciclo FOR y ejecuta varias acciones

pizzas=['cheese','pepperoni','chicken']

#imprime los elementos de la lista
for pizza in pizzas:
    print(pizza)

#imprime mensaje con cada elementos y un solo mensaje al final
for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}")
print("Todas las pizzas son deliciosas")
