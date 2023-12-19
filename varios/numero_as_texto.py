#Programa que convierte una entrada de un numero en sus digitos en forma de texto

def entrada():
	digitos = '0123456789'
	cont = 0
	while True:
		num = list(input('Ingrese un numero: '))
		for n in num:
			if n not in digitos:
				print(f'No es {n} un digito')
				break
			else:
				cont += 1
		if cont == len(num):
			return num

def num_as_text():
	num_texto = ['cero','uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
	num = entrada()
	print(num)
	numero = ''
	for n in num:
		numero += num_texto[int(n)] + ' '
	return numero.upper()
		
	
print(num_as_text())