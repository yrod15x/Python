#Progrma que transforma números hexadecimales a números en base 10 y viceversa. Enteros positivos

def conversor_base10_hexadecimal(numero:int)-> str:
    """Función que transforma un número decimal a uno en base 10 - recibe un entero y devuelve un string hexadeicmal"""
    hexadecimales = [str(num) for num in range(10)]
    for n in range(65, 71):
        hexadecimales.append(chr(n))

    hexa = ""

    if numero < 16:
        hexa = hexadecimales[numero]
    else:
        while(numero > 16):
            cociente = int(numero / 16)
            residuo = numero - (cociente*16)
            hexa += hexadecimales[residuo]
            numero = cociente
            if numero < 16:
                hexa += hexadecimales[numero]

    return hexa[::-1]

def conversor_hexadecimal_base10(num_hexa:str)-> int:
    """Función que transforma un número hexadecimal a uno en base 10 - recibe un string y devuelve un entero positivo"""
    
    potencias_16 = [16**num for num in range(len(num_hexa))]
    hexadecimales = [str(num) for num in range(10)]
    for n in range(65, 71):
        hexadecimales.append(chr(n)) 

    #diccionario con coversion de hexadecimal a decimal
    tabla_conversora = {}

    for elemenents in hexadecimales:
        if ord(elemenents) >= 48 and ord(elemenents) < 58:
            tabla_conversora[elemenents] = int(ord(elemenents)) - 48
        else:
            tabla_conversora[elemenents] = int(ord(elemenents)) - 55

    num_decimal = 0
    cont = 0

    for num in num_hexa[::-1]:
        num_decimal += tabla_conversora[num] * (potencias_16[cont])
        cont += 1

    return num_decimal

print(conversor_base10_hexadecimal(255))
print(conversor_hexadecimal_base10("C921"))
