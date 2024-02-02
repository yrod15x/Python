#CCC '20 J2 - Epidemiology

def dias_infectados(pac_zero, rate_infectados, lim_infecatdos):
    infectados = pac_zero 
    dias = 0
    while True:
        if infectados > lim_infecatdos:
            break
        infectados += pac_zero * rate_infectados
        pac_zero *= rate_infectados
        dias += 1
    return dias
        
limite_infectados = int(input()) 
pac_zero = int(input())
rate = int(input())         
        
print(dias_infectados(pac_zero, rate, limite_infectados))