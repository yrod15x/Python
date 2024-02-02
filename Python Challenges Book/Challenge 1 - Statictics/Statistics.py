
class Statistics:
    """Clase que muestra numeros divisibles por 2 y 7. Muestra la cantidad de multiplos de ambos. 
    La suma de todos esos multiplos en conjunto. Escribe por pantalla y registra en un archivo todos
    los datos recogidos."""
    
    def __init__(self, cant_number = 1):
       self.__cant_number = cant_number
    
    def set_divisible_by_2(self):
        self.__divisibles_x_2 = [x for x in range(1, self.__cant_number + 1) if x % 2 == 0]
    
    def get_set_divisible_by_2(self):
        return self.__divisibles_x_2
    
    def set_divisible_by_7(self):
        self.__divisibles_x_7 = [x for x in range(1, self.__cant_number + 1) if x % 7 == 0]
        
    def get_set_divisible_by_7(self):
        return self.__divisibles_x_7
        
    def amount_divisibles_by_7(self):
        return len(self.__divisibles_x_7)
    
    def amount_divisibles_by_2(self):
        return len(self.__divisibles_x_2)
    
    def sum_amounts(self):
        return sum(self.__divisibles_x_2) + sum(self.__divisibles_x_7)
    
    def get_datos(self):
        self.datos = ''
        self.datos += '----------------------------------------------------------------------------------\n'
        self.datos += f"Rango-> {self.__cant_number}\n"
        self.datos += f"Divisible 2 ->  {self.__divisibles_x_2}\n"
        self.datos += f"Divisible 3 ->  {self.__divisibles_x_7}\n"
        self.datos += f"Amount ->   {self.amount_divisibles_by_2() + self.amount_divisibles_by_7()}\n"
        self.datos += f"Sum ->  {self.sum_amounts()}\n"
        self.datos += '----------------------------------------------------------------------------------\n'
        return self.datos
        
    def infile_register(self):
        file = 'resultados.txt'
        with open(file, 'a') as file_object:
            file_object.write(self.get_datos())
            
    def print_information(self):
        print(self.get_datos())
        