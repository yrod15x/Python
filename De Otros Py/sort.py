num = int(input())
numeros = []

for i in range(num):
    numeros.append(int(input()))
    
print(sorted(numeros))

for n in sorted(numeros):
    print(n)