#Programa que analiza una función que tira una moneda 100 veces  al aire. se graban C (cara) o S (sello) #en una lista de acuerdo a cada tiro. Se busca una secuencia de 6 sellos o caras. Se saca un promedio
#de estas series al ejecutar la función de moneda al aire 1000 veces

from random import randint

def cara_sello():
    """Aleatoriamente genera un lanzamineto de moneda cara o sello"""
    lanzamientos = []
    for i in range(100):
        moneda = randint(0, 1)
        if moneda == 0:
            lanzamientos.append("C")
        else:
            lanzamientos.append("S")
    return lanzamientos

def secuencia_sello(lanzamientos):
    """Mide si una moneda cae en sello de una lista se repite 6 veces"""
    cont_sellos = 0
    contador_general = 0
    for probabilidad in lanzamientos:
        if probabilidad == 'S':
            cont_sellos += 1
            if cont_sellos == 6:
                contador_general += 1
        else:
            cont_sellos = 0
    return contador_general

def secuencia_cara(lanzamientos):
    """Mide si una moneda cae en cara de una lista se repite 6 veces"""
    cont_caras = 0
    contador_general = 0
    for probabilidad in lanzamientos:
        if probabilidad == 'S':
            cont_caras += 1
            if cont_caras == 6:
                contador_general += 1
        else:
            cont_caras = 0
    return contador_general

suma_sellos = 0
suma_caras = 0

for i in range(1000):
    lanzamientos = cara_sello()
    suma_caras += secuencia_cara(lanzamientos)
    suma_sellos += secuencia_sello(lanzamientos)


print(f"El promedio de ocurencia en 6 de sellos en mil repeticiones es {(suma_sellos * 100) / 1000} %")
print(f"El promedio de ocurencia en 6 de caras en mil repeticiones es {(suma_caras * 100) / 1000} %")