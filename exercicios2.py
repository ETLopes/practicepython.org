numero = int(input('Me diga um número: '))
numero2 = numero % 2
multiplo = numero % 4

if numero2 != 0:
	print('\n'+'Esse número é impar'+'\n')
elif multiplo == 0:
	print('\n'+'Esse número é múltiplo de 4'+'\n')
else:
	print('\n' +'Esse número é par'+ '\n')


num = int(input('Me diga um numerador: '))
div = int(input('Me diga um denominador: '))
total = num % div


if total == 0:
	print('\nEsse numerador é divisível pelo denominador\n')
else:
	print('\nEsse numerador não é divisível pelo denominador\n')
