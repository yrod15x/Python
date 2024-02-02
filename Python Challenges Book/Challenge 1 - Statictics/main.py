#Programa que muestra los numeros divisibles por 2 y 7. La cantidad de los mismos y su suma 
#global. Hace uso de la clase Statics. 
from Statistics import *

numeros = [Statistics(x+1) for x in range(15)]


for i in range(15):
    numeros[i].set_divisible_by_2()
    numeros[i].set_divisible_by_7()
    numeros[i].print_information()
    numeros[i].infile_register()
    
    
