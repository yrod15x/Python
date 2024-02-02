def cousins(num):
    primos = [True for i in range(num+1)]
    primos[0] = False
    primos[1] = False

    i = 2

    while i * i < num:
        j = i
        while j * i < num:
            primos[i * j] = False
            j += 1
        i += 1

    primates = []

    for i in range(2, num):
        if primos[i] == True:
            primates.append(i)

    return primates

def factores_primos(num):
    lospri = []
    lospri = cousins(num)
    factores = []
    i = 0
    while num > 1 and num > i:
        if(num % lospri[i] == 0):
            factores.append(lospri[i])
            num = int(num / lospri[i])
        else:
            i = i + 1
    return factores

num = int(input())
facts = []
facts = factores_primos(num)
print(facts)









