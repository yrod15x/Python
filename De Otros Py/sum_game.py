#CCC '17 S1 - Sum Game

def text_integer(lista):
    enteros = []
    for l in lista:
        enteros.append(int(l))
    return enteros

def comparar_listas(lista1, lista2)->list:
    dias = []
    suma_lista1, suma_lista2 = 0, 0
    for i in range(len(lista1)):
        suma_lista1 += lista1[i]
        suma_lista2 += lista2[i]
        if suma_lista1 == suma_lista2:
            dias.append(i+1)
    return dias

def mayores(lista):
    if len(lista) == 0:
        return 0
    else:
        return max(lista)

total_days = int(input())
swifts_runs = text_integer(input().split())
semaphore_runs = text_integer(input().split())

print(mayores(comparar_listas(swifts_runs, semaphore_runs)))
