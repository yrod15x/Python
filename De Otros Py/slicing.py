#Programa que ejecuta instrucciones con listas y ciclos

#create a list and print the 1st 3 elements
sabores = ['acido','dulce','salado','agrio','picante','descompuesto','fresco']
print("\nLos 3 primeros sabores son: ")
for sabor in sabores[:3]:
    print(sabor)
   
#imprimir 3 elementos empezando desde la mitad de la lista
print("\nLos 3 elementos de la mitad hacia delante")
for sabor in sabores[int(len(sabores)/2):int(len(sabores)/2)+3]:
    print(sabor)
   
#imprimir los ultimos 3 elementos de la lista
print("\nLos ultimos 3 elementos de la lista son: ")
for sabor in sabores[-3:]:
    print(sabor)

#crear una lista y copiarla en otra
posiciones = ['arquero','defensa','delantero','volante']
otras_posiciones = posiciones[:]

#anadir diferentes elemetos a cada una de las listas
posiciones.append('marcador')
otras_posiciones.append('libero')

#imprimir el contenido de cada lista
print("\nLas posiciones de la lista original son: ")
for posicion in posiciones:
    print(posicion)

print("\nLa posiciones de la nueva lista son: ")
for posicion in otras_posiciones:
    print(posicion)
