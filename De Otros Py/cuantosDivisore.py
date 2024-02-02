"""CCC '05 J2 - RSA Numbers"""

def numeros_primis(limite):
    """Devuelve una lista con números primos"""
    primos = [True] * limite
    prime_numbers = []

    for i in range(2, int(limite / 2)):
        j = 2
        while i * j < limite:
            if not primos[i*j]:
                j += 1
                continue
            else:
                primos[i*j] = False
                j += 1

    primos[0] = False
    primos[1] = False

    for indice, valor in enumerate(primos):
        if valor:
            prime_numbers.append(indice)
    
    return prime_numbers

def factores_primos(num):
    lospri = []
    lospri = numeros_primis(num)
    factores = []
    i = 0
    while num > 1 and num > i:
        if num % lospri[i] == 0:
            factores.append(lospri[i])
            num = int(num / lospri[i])
        else:
            i = i + 1
            if i >= len(lospri):
                break
    return factores

def contar_exponentes(fact_primos):
    expos = []
    c = 1
    for i in range(len(fact_primos)):
        if i < len(fact_primos) - 1:
            if  fact_primos[i] == fact_primos[i+1]:
                c += 1
            else:
                expos.append(c)
                c = 1
        else:
           if fact_primos[-1] != fact_primos[-2]:
               expos.append(1) 
    if c > 1:
        expos.append(c)
    
    expos = [x+1 for x in expos]

    num_divisores  = 1
    for e in expos:
        num_divisores *= e
    
    return num_divisores

n1 = int(input())
n2 = int(input())
c = 0
for i in range(n1, n2 + 1) :
    if contar_exponentes(factores_primos(i)) == 4:
        c += 1

print(f"The number of RSA numbers between {n1} and {n2} is {c}")