#Programa que convierte una cantidad determinada de un ingrediente a su total en medidas 
# imperiales(cup, tablespoons, teaspoon). Se tiene una funcion cuyo primer argumento(str) es una de las medidas
# y el segundo es la cantidad de esta (float). Esta devuelve la cantidad dividida en las 3 medidas. Ex: 59 teaspoons ->
# 1 cup, 3 tablespoons, 2 teaspoons

def med_imperiales(tipo: str, cantidad: float)->None:
    """Convierte la cantidad de ingrediente del tipo dado su equivalecia dentro de las medidas imperiales"""
    tab_spoon = 0
    tea_spoon = 0
    cups = 0
    residuo = 0

    if tipo == "1":
        tab_spoon = cantidad * 16
        tea_spoon = tab_spoon * 3
        print(f"{cantidad} tazas son {tab_spoon} tablespoons o {tea_spoon} teaspoons")
    elif tipo == "2":
        cup = int(cantidad / 16)
        residuo = cantidad % 16
        while(residuo >= 3):
            tea_spoon += 1
            residuo -= 3
        print(f"{cantidad} tablespoons hacen {cup} tazas, {residuo} tabspoons, {tea_spoon} teaspoons  ")
    elif tipo == '3':
        if cantidad > 48:
            cup = int(cantidad / 48)
            residuo = cantidad % 48
            if residuo > 16:
                tab_spoon = int(residuo / 16)
                tea_spoon = residuo % 16
            else:
                tab_spoon = int(residuo / 3)
                tea_spoon = residuo % 3
        else:
            if cantidad > 3:
                tab_spoon = int(cantidad / 3)
                tea_spoon = cantidad % 3
            else:
                tea_spoon = cantidad
                tab_spoon, cup = 0, 0
        print(f"{cantidad} tablespoons hacen {cup} tazas, {tab_spoon} tabspoons, {tea_spoon} teaspoons  ")
            
    return None

med_imperiales("3", 59)