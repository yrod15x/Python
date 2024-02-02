#Programa que recorre listas con un ciclo while verificando que esten vacias
#Vaciar lista y romper el ciclo. Ademas de remover un elemento repetido y terminar la iteracion

sanguches_orders = ['pastrami','posho','keso','pastrami','atun']
sanguches_finsihed = []

#sacar un elemento repetido
print("Pilas!!! Se acabo el pastrami !!!")
while 'pastrami' in sanguches_orders:
    sanguches_orders.remove('pastrami')

#vaciar la lista y terminar el ciclo
while sanguches_orders:
    sanguche = sanguches_orders.pop()
    print("El sanguche de " + str(sanguche) + " esta listo!")
    sanguches_finsihed.append(sanguche)

print("Los sanguches hechos son: ")
for sanguchito in sanguches_finsihed:
    print(sanguchito)
