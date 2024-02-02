#Programa que ordena, reversa listas. 
locations = ['Seatle','San Francisco','Munich','Tokyo','Patagonia']
print("Lista inicial -->" + str(locations))

#organizar alfabeticamente sin modificarla
print("Lista ordenada -->" + str(sorted(locations)))  
print("Lista inicial -->" + str(locations))

#organizar en orden ascendente alfabeticamente
print("Al reves -->" + str(sorted(locations,reverse = True)))
print("Lista inicial -->" + str(locations))

#modificar la lista en imprimirla en orden reverso. Se debe ordenar 1ero y luego mostrar
locations.reverse()
print("Al reves --> " + str(locations))
locations.reverse()
print("Lista incial --> " + str(locations))

#Ordenar la lista en orden alfabetico y modificarla
locations.sort()
print("Lista ordenada -->" + str(locations))
locations.sort(reverse = True)
print("Al reves alfabetica --> " + str(locations))

#Saber cual es el tamaño de una lista se usa la funcion len()
print("El tamaño de la lista es " +str(len(locations)))

#Más ejemplos para organización y modificación alfabetica de listas
colores = ['rojo','azul','negro']
print("La lista tiene " + str(len(colores)))
print("EL orden alfabetica sin modificar es " + str(sorted(colores)))
print('La lista alfabetica sin modificar inversa ' + str(sorted(colores,reverse=True)))
colores.reverse()
print('La lista mostrada y modificada en orden inverso ' + str(colores))
colores.sort()
print("La lista ordenada de forma alfabetica modificada " + str(colores))
