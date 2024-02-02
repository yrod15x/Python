from math import sqrt, pow

class Divisores:
    def __init__(self, numero = 1):
        self.__numero = numero
        self.__numero_original = numero
        self.__num_primos = []
        self.__divisores = [1]
        
    def set_numero(self, numero):
        self.__numero = numero
        self.__numero_original = numero
    
    def __criba_erarostenes(self):
        """1. Se maracan todos los numeros hasta el limite como primos: True(self._primos[])
            2. Si el i^2 es menor que el numero se deja de buscar 
            3. Si el numero no se ha marcado como primo (False) buscar multiplos
            4. Buscar desde el i hasta numero partido a la mitad. Ex:  10 / 2 = 5. Cualquier numero
            multiplicado por 2 mayor a 5 se pasa de 10.
            5. Se marca el multiplo del numero i como no primo Falso [i * j]
        """
        self.__primos_bool = [True for i in range(self.__numero + 1)]
        self.__primos_bool[0], self.__primos_bool[1] = False, False
        
        i = 2
        while i * i < self.__numero:
            j = i
            while j * i < self.__numero:
                self.__primos_bool[i * j] = False
                j += 1
            i += 1
                    
        for index, valor in enumerate(self.__primos_bool):
            if valor:
                self.__num_primos.append(index)
             
    def __extraer_factores_primos(self):
        #Se extraen los factores primos hasta el numero limite en una lista
        self.__criba_erarostenes()
        self.__factores_primos = []
        i = 0
        
        while True :
            #Si el numero / un factor primo (de la lista) es 1 se acaba la factorizacion
            if self.__numero / self.__num_primos[i] == 1:
                self.__factores_primos.append(self.__num_primos[i])
                break
            #Si numero es divisible por el 1er (2nd) factor primo de la lista, se encontro un factor 
            # Numero se covierte en el resultado de la division entera por su factor primo
            if self.__numero % self.__num_primos[i] == 0:
                self.__factores_primos.append(self.__num_primos[i])
                self.__numero /= self.__num_primos[i]
            else:
                i += 1       
            
    def extraer_divisores(self):
        """Divisores se pueden obetner mediante el producto de cada factor primo por los divisores previos """
        self.__extraer_factores_primos()
        for factores in self.__factores_primos:
            lista_temp = []
            for divi in self.__divisores:
                if factores * divi not in self.__divisores:
                    lista_temp.append(factores * divi)
            self.__divisores +=  lista_temp
        self.__divisores.sort()    
        
    def es_perfecto(self):
        if sum(self.__divisores[:-1]) == self.__numero_original:
            print(f"{self.__numero_original} es un numero perfecto")
        else:
            print(f"{self.__numero_original} No es un numero perfecto")
        print(self.__divisores[:-1])
        