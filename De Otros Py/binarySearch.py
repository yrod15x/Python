'''Programa que pone en practica el algoritmo de busqueda binaria'''

from random import randint

def bin_search(lista, elemento):
    """Toma una lista, la ordena y devuelve la posicion del elemento a buscar. Si no lo encuentra devuelve None.
    La busquea binaria intenta buscar un elemento dividiendo la lista en rangos o sectores. Siempre conrtando a 
    la mitad cada uno de ellos a medida que se establece que elemento buscado sea mayor o menor a los mismos.
    La primera busqueda se hace con la mitad de la lista si el elemento es mayor a esta el proximo rango a buscar 
    es mitad hasta el final de la lista, si por el contrario es menor el ramgo seria desde el inicio hasta la mitasd
    Todo el proceso se repite hasta hallar o no lo que se busca"""
    
    #Se establecen las posiciones iniciales del los rangos a buscar
    min = 0
    max = len(lista) - 1
    
    #mientras haya rangos en que buscar
    while min <= max:
        #encuentra siempr la nueva mitad del rango
        mitad = int((max + min) / 2)
        #mitad del rango sera el punto a comparar con el elemneto a buscar
        intento = lista[mitad]
        if intento == elemento:
            return mitad
        #dependiendo si el elemento es mayor o menor se ajustan los rangos
        if intento > elemento:
            max = mitad - 1
        else:
            min = mitad + 1
        return None

numeros = [5, 7, 21, 8, 89, 23, 45, 67, 2]
numeros.sort()
print(numeros)

if bin_search(numeros, 21) == None:
    print("EL elemento no esta en la lista")
else:
    print(bin_search(numeros, 21))

