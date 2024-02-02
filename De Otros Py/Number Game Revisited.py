import random

def cousins(n):
    primos = []
    primos.append(False)
    primos.append(False)

    for i in range(2, n):
        primos.append(True)

    i = 2
    while i * i < n:
        j = i
        while j * i < n:
            primos[i * j] = False
            j += 1
        i += 1

    lospri = []
    for i in range(2, n):
        if primos[i] == True:
            lospri.append(i)

    return lospri

n = int(input())
primes = []
primes = cousins(n)


while n > 0:
    bob = random.randint(1, len(primes))
    n -= bob
    if( n <= 0):
        print("BOB")
        break
    alice = random.randint(1, len(primes))
    n -= alice
    if (n <= 0):
        print("ALICE")
        break


