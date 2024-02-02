#You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years 2014, 2015, 2016, 2017, 2018, 2019 each have distinct #digits. 2012 does not have distinct digits, since the digit 2 is repeated.
#Given a year, what is the next year with distinct digits?

def sacar_digitos(numero):
    digitos = []
    while numero > 0:
        digitos.append(numero % 10)
        numero = int(numero / 10)
    digitos.reverse()
    return digitos

def unicos_digitos(lista_numeros):
    for num in lista_numeros:
        if lista_numeros.count(num) > 1:
            return False
    return True


num = int(input())
num += 1

while True:
    lista_num = sacar_digitos(num)
    if unicos_digitos(lista_num):
        break
    else:
        num += 1

print(num)