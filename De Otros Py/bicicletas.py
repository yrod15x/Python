#CCC '16 S2 - Tandem Bicycle

def velocidades(tamano):
    speeds = input().split()
    speeds = [int(x) for x in speeds]
    return speeds

pregunta = int(input()) 
tamano = int(input())

dmojistan = velocidades(tamano)
pegland = velocidades(tamano)
suma = []
dmojistan.sort(reverse=True)

if pregunta == 1:
    pegland.sort(reverse=True) 
else:
    pegland.sort()

for i in range(tamano):
       suma.append(max(dmojistan[i], pegland[i]))
       
print(sum(suma))