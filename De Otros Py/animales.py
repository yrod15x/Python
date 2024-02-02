#Programa que recorrer una lista y muestra diferentes mensajes

animales=['perro','gato','conejo']

#imprimir cada elemento
for animal in animales:
    print(animal)

#imprime mensajes con cada elemento y un mensaje general
for animal in animales:
    print(f"El {animal} es una gran mascota")
print("Me encantan todas estas mascotas!")
