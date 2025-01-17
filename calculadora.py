n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
opt = str(input('A - Soma | B - Subtração | C - Multiplicação | D - Divisão\n')).upper()

if opt == 'A':
	resultado = n1 + n2
	print(f'O resultado é {resultado}')
elif opt == 'B':
	resultado = n1 - n2
	print(f'O resultado é {resultado}')
elif opt == 'C':
	resultado = n1 * n2
	print(f'O resultado é {resultado}')
elif opt == 'D':
	if n2 == 0:
		print('Erro')
	else:
		resultado = n1 / n2
		print(f'O resultado é {resultado}')
else:
	print('Opção inválida')
