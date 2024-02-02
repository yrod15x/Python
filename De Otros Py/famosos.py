#Genera una lista de personas famosas e imprime un mensaje
#f-string para imprimir elementos de una lista
famosos = ['dennis ritchie', 'albert einstein', 'richard feynman']
mensaje = f"Querido {famosos[0].title()}, ¿Desearías venir a cenar conmigo?" 
print(mensaje)
mensaje = f"Estimado {famosos[1].title()}, ven a cenar!"
print(mensaje)
mensaje = f"{famosos[2].title()}, si tienes hambre, ven a casa!"
print(mensaje)

#modifica la lista y remplazar un valor de algun elemento
print(f"{famosos[1].title()} no puede venir a la casa")
famosos[1] = 'Nicola Tesla' #remplazo el valor del segundo elemento
mensaje = f"Querido {famosos[0].title()}, ¿Desearías venir a cenar conmigo?" 
print(mensaje)
mensaje = f"Estimado {famosos[1].title()}, ven a cenar!"
print(mensaje)
mensaje = f"{famosos[2].title()}, si tienes hambre, ven a casa!"
print(mensaje)

#add more elements to a list. Using insert() y append()
print("Hay más espacio para más invitados... Vengan!")
famosos.insert(0,'rene descartes')
famosos.insert(2,'isaac newton')   #inserta en el 3er indice el nuevo elemento
famosos.append('gottfried leibniz')
mensaje = f"Querido {famosos[0].title()} ven a comer"
print(mensaje)
mensaje = f"Querido {famosos[1].title()} ven a comer"
print(mensaje)
mensaje = f"Querido {famosos[2].title()} ven a comer"
print(mensaje)
mensaje = f"Querido {famosos[3].title()} ven a comer"
print(mensaje)
mensaje = f"Querido {famosos[4].title()} ven a comer"
print(mensaje)

#eliminar de la lista algunos elemnetos usando pop() y del
print("Lo siento! Solo hay espacio para dos personas")
elminado = famosos.pop(1)  #elimino el segundo elemento y lo almaceno para usarlo despues POP()
print("Sr " + elminado.title() + " no puede venir a cenar!")
elminado = famosos.pop()   #elimino el ultimo elemento y almaceno
print("Sr " + elminado.title() + " no puede venir a cenar!")
del famosos[0]
del famosos[0]
del famosos[0]
del famosos[0]
print(famosos)