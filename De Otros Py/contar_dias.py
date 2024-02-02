#Programa que determina cuantos dias van de un determinado anio

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


if is_leap(1992):
    print("Bisiesto")
else:
    print("No Bisiesto")