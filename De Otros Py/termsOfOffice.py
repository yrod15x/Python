alcalde, tesorero, programador, perrero = True, True, True, True
cont_alcalde, cont_tesorero, cont_programador, cont_perrero = 0, 0, 0, 0
inicio = int(input())
limite = int(input())

def contador(contador, anos):
    datos = []
    if contador == anos:
        datos.append(True)
        datos.append(0)
    else:
        datos.append(False)
        datos.append(contador)
    return datos
    

for i in range(inicio, limite + 1):
    if alcalde and tesorero and programador and perrero:
        print(f'All positions change in year {i}')
    cont_alcalde += 1
    cont_tesorero += 1
    cont_programador += 1
    cont_perrero += 1
    
    datos_alc = contador(cont_alcalde, 4)
    alcalde = datos_alc[0]
    cont_alcalde = datos_alc[1]
    
    datos_tes = contador(cont_tesorero, 2)
    tesorero = datos_tes[0]
    cont_tesorero = datos_tes[1]
    
    datos_per = contador(cont_perrero, 5)
    perrero = datos_per[0]
    cont_perrero = datos_per[1]
    
    datos_pro = contador(cont_programador, 3)
    programador = datos_pro[0]
    cont_programador = datos_pro[1]
    
