#Crear un ciclo que cuente hasta 20 y mostrarlo
print("**** Muestro los números de 1 a 20 ***")
for num in range(1,21):
    print(num,end=" ")

#crear una lista que almacene los numeros de 1 a 100
print("\n\n**** Muestro los números de 1 a 100 ***")
million = list(range(1,101))
for num in million:
    print(num,end=" ")

#Crear una lista de mil números y mostar el menor, mayor y la suma
print("\n\n**** Muestro el número menor, el mayor y la sumatoria de una sucesión ***")
mil = list(range(1,1001))
print(f"El número menor es {min(mil)}")
print(f"El número mayor es {max(mil)}")
print(f"La sumatoria del número es {sum(mil)}")

#Crear una lista numeros impares del 1 a 20 y mostarlos en un ciclo
print("\n\n**** Muestro los números impares de 1 a 20 ***")
impares = list(range(1,21,2))
for impar in impares:
    print(impar,end=" ")

#Crear una lista de los multiplos de 3 de 1 a 30. Forma 1 con variable
print("\n\n**** Muestro los multiplos de 3 hasta el 30 ***")
multiplos_3 = []
for num in range(1,11):
    multiplo = num * 3
    multiplos_3.append(multiplo)
print(f"Los multiplos de 3 son {multiplos_3}")

#Crear una lista de los multiplos de 4 de 1 a 40. Forma 2 directo al append
print("\n\n**** Muestro los multiplos de 4 hasta el 40 ***")
multiplos_4 = []
for num in range(1,11):
    multiplos_4.append(num*4)
print(f"Los multiplos de 4 son {multiplos_4}")

#Crear una lista de los multiplos de 5 de 1 a 50. Forma 3 Lista de compresion
print("\n\n**** Muestro los multiplos de 5 hasta el 50 ***")
multiplos_5 = [num*5 for num in range(1,11)]
print(f"Los multiplos de 5 son {multiplos_5}")

#Crear e imprimir una lista con los cubos de los 10 numeros naturales
print("\n\n**** Muestro los cubos de los primeros numeros naturales***")
cubos = []
for num in range(1,11):
    cubos.append(num**3)

cont = 1
for cubo in cubos:
    print(f"El cubo de {cont} es {cubo}")
    cont += 1

#Crear e imprimir una lista con los cuadrados de los 10 numeros naturales.Lista de Compresion
print("\n\n**** Muestro los cuadrados de los primeros numeros naturales***")
cuadrados = [num**2 for num in range(1,11)]
cont = 1
for cuadrado in cuadrados:
    print(f"El cuadrado de {cont} es {cuadrado}")
    cont += 1