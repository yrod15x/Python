#programa que toma una lista como una función y devuelva una cadena de texto con los elementos
#separados por comas y espacios y la conjunción (y) antes del ultimo elemento

def comma_code(lista):
    phrase = ""
    #si la lista no esta vacia
    if not lista == []:
        for elemento in lista:
            if elemento != lista[-1] :
                phrase += elemento + ", "
            else:
                phrase += "y " + elemento
    else:
        print("Lista vacia. Nose puede codificar")
    return phrase
    

lista = ["Sony", "Microsoft", "Nintendo", "Google"]

print(comma_code(lista))