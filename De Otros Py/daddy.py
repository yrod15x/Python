numero =  int(input())
base = numero
menor  = 0
veces = 0

while numero + menor == base and numero >= menor:
    if numero > 5:
        menor = numero - 5
        numero = 5
    veces += 1
    numero -= 1
    menor += 1

print(veces)