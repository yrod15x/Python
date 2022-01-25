#Representa la busqueda de un elemento en una lista. Los elementos enteros de la lista representan usuarios de un sistema

def binaria(perdido:int, elementos:list)->bool:
  """Dada una lista ordenada, se evalua si un elemento se encuentra en la lista. Cada intento de busqueda se hace reduciendo la lista a la mitad. Devuelve un booleano"""
    bajo = 0
    alto = len(elementos) - 1
    elementos.sort()
    while bajo < alto:
        mitad = int((alto + bajo) / 2)
        intento = elementos[mitad]
        if intento > perdido:
            alto = mitad - 1
        elif intento < mitad:
            bajo = mitad -1
        else:
            return True
    return False
            
user = 24
elementos = [2, 4, 3, 6, 8, 93, 24, 35, 67, 1, 8]
if binaria(user, elementos):
    print(f"Bienvenido usuario {user} !!! ")
else:
    print(f"usuario {user} no esta registrado")
    
