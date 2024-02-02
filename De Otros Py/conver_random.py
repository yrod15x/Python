from random import randint

class Conversor():
    def __init__(self, num: int = 1) -> None:
        self.num = num
        self.residuo = num
    
    def __repr__(self) -> str:
        return str(self.num)

    def decimal_hexa(self) -> str:
        """recibe un entero y devuelve un string hexadecimal"""
        hexadecimales = [str(num) for num in range(10)]
        for n in range(65, 71):
            hexadecimales.append(chr(n))
        hexa = ""
        if self.num < 16:
            hexa = hexadecimales[self.num]
        else:
            while(self.num > 16):
                cociente = int(self.num / 16)
                residuo = self.num - (cociente*16)
                hexa += hexadecimales[residuo]
                self.num = cociente
                if self.num < 16:
                    hexa += hexadecimales[self.num]

        return hexa[::-1]
    
    def decimal_binario(self):

        list_binario = []
        
        while(self.residuo > 0):
            if self.residuo % 2 == 0:
                list_binario.append('0')
            else:
                list_binario.append('1')
            self.residuo = int(self.residuo / 2)
        
        reversed(list_binario)
        return "".join(list_binario)


numero = randint(1, 1000)
convert = Conversor(numero)
print(f"{numero} en Hexadecimal es {convert.decimal_hexa()}")
print(f"{numero} en Binario es {convert.decimal_binario()}")