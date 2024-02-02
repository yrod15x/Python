#ECOO12R1P2 - Decoding DNA

def entrada():
    '''Recoge 5 lineas de datos y los amanecena en una lista'''
    cadenas = []
    for i in range(5):
        cadenas.append(input()) 
    return cadenas

def rerversar_cadena(cadena):
    return cadena[::-1]

def conversor_ADN(cadena):
    adn_converso = []
    for cad in cadena:
        if cad == 'A':
            adn_converso.append('T')
        elif cad == 'T':
            adn_converso.append('A')
        elif cad == 'C':
            adn_converso.append('G') 
        elif cad == 'G':
            adn_converso.append('C')
    return ''.join(adn_converso)

def encontrar_iniciador(cadena):
    '''Busca la subcadena TATAAT en la cadena argumento - Devuelve indice para buscar el terminador'''
    
    indice =  0
    terminador = ''
    
    if 'TATAAT' in cadena:
        indice =  cadena.find('TATAAT') + 10
    
    indice_conservado = indice
    indice_terminador = 0
    
    for i in range(indice+6, len(cadena)-6):
        terminador = conversor_ADN(rerversar_cadena(cadena[i:i+6]))
        if terminador in cadena[i:len(cadena)]:     
            indice_terminador = i
            break
 
    rna = []
    
    for j in range(indice_conservado, indice_terminador):
        rna.append(cadena[j])
    
    rna = "".join(rna)
    rna = conversor_ADN(rna)    
    rna = rna.replace('T', 'U')
    return rna
        

#cadenas = entrada()
cadenas =['AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC',
          'AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA',
          'TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT']

print(encontrar_iniciador(cadenas[0]))

#CCUAAAUCUAACUGGG