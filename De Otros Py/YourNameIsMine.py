import sys

def si_es_substring (human1, human2):
    if len(human1) > len(human2):
        hombre = human1
        mujer = human2
    else:
        hombre = human2
        mujer = human1

    nuevo_hombre = []
    nueva_mujer = []

    for i in hombre:
        nuevo_hombre.append(i)
    for j in mujer:
        nueva_mujer.append(j)

    for i in range(0, len(hombre)):
        c = 0
        for j in range(0, len(mujer)):
            if nuevo_hombre[i] == nueva_mujer[j]:
                continue
            else:
                c += 1
        if c == len(mujer): #no esta llegando al total de letras
            nuevo_hombre[i] = '-1'

    for i in range(0, len(hombre) - 1):
        if nuevo_hombre[i] == '-1':
            del(nuevo_hombre[i])
    este_hombre = ''.join(nuevo_hombre)
    if este_hombre == mujer:
        print('YES')
    else:
        print('NO')


hombre = "john"
mujer = "johana"


if hombre == mujer:
    print("YES")
else:
    if len(hombre) == len(mujer):
        for i in range(0, len(hombre)):
            for j in range(i, len(hombre)):
                if mujer[i] != hombre[j]:
                    print("NO")
                    exit(0)
    else:
        si_es_substring(hombre,mujer)





