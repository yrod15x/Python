#Programa que busca información en un archivo json y la muestra por pantalla

import json

archivo = "Archivos Excepciones/usuario.json"
try:
    with open(archivo) as f:
        datos = json.load(f)
except FileNotFoundError:
    print("Archivo no existe!")
else:
    print(f"Su nombre es {datos[0]}")
    print(f"Su edad es {datos[1]}")