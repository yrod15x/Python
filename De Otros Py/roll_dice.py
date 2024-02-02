"""CCC '06 J2 - Roll the Dice"""

def contador_suma(lado1, lado2):
    """Suma elementos en dos listas verificando que den 10"""
    suma = 0
    if len(lado1) > len(lado2):
        lado1 = sorted(lado1, reverse=True)
        for i in range(len(lado2)):
            for j in range(len(lado1)):
                if lado2[i] + lado1[j] == 10:
                    suma += 1
    else:
        lado2 = sorted(lado2, reverse=True)
        for i in range(len(lado1)):
            for j in range(len(lado2)):
                if lado2[j] + lado1[i] == 10:
                    suma += 1 
    return suma

lado_m = int(input())
lado_n = int(input())
digitos_m = [i+1 for i in range(lado_m) if i < 9]
digitos_n = [i+1 for i in range(lado_n) if i < 9]

veces_10 = contador_suma(digitos_m, digitos_n)
if veces_10 == 1:
    print('There is 1 way to get the sum 10.')
else:
    print(f'There are {veces_10} ways to get the sum 10.')
