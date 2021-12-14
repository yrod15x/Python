#Digital root is the recursive sum of all the digits in a number.
#Given n, take the sum of the digits of n. If that value has more than one digit, 
#continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    #intersante como python me permite convertir numeros a carcateres para sacarles los digito

    #Saca los digitigos enteros de un numero entero convertido a string
    lista = [int(num) for num in str(n)]

    suma = 0
    for i in lista:
        suma += i
        if suma > 10:
            suma = (suma % 10) + int(suma / 10)
         

    return suma

print(digital_root(564))
