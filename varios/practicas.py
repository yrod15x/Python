#Programa que devuelve el número mayor y el menor de una cadena de texto
numbers = "4 7 9 -3 64"

numbers = list(numbers.split(" "))
int_numbers = []

for num in numbers:
    int_numbers.append(int(num))

int_numbers.sort()
numbers = ""
numbers += str(int_numbers[len(int_numbers) - 1])
numbers += str(" ")
numbers += str(int_numbers[0])

print(numbers)