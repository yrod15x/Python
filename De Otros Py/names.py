#Imprime los nombres en una lista, uno a la vez.
amigos = ['andres', 'carlos','luis']
print (amigos[0])
print (amigos[1])
print (amigos[2])

print ("\n")
#Imprime mensaje con elementos de la lista usando variables
mensaje = f"{amigos[0].title()} es un profesor"
print (mensaje)
mensaje = f"Este es {amigos[1].title()} quien vive en Lexington"
print (mensaje)
mensaje = f"Mi hermano y mi amigo es {amigos[2].title()}"
print (mensaje)

print ("\n")
#Imprime mensaje con elementos de listas sin usar variables
transportes = ['moto','carro','barco']
print (f"Yo usaba una {transportes[0]} para moverme")
print (f"Honda es una marca de {transportes[1]}")
print (f"Me encanta ir en {transportes[2]}")
