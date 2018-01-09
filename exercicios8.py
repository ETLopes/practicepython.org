
while True:
	a = input('Jogador 1: Pedra, Papel ou Tesoura? ').lower()
	b = input('Jogador 2: Pedra, Papel ou Tesoura? ').lower()
	if a == b:
		print('Empate')
		if str(input('Deseja jogar novamente? ')) == 'sim':
			continue
		else:
			break
	elif a == 'pedra':
		if b == 'papel':
			print('Jogador 2 venceu!')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
		elif b == 'tesoura':
			print('Jogador 1 venceu!')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
		else:
			print('Escolha uma opcao valida')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
	elif a == 'papel':
		if b == 'pedra':
			print('Jogador 1 venceu!')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
		elif b == 'tesoura':
			print('Jogador 2 venceu!')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
		else:
			print('Escolha uma opcao valida')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
	elif a == 'tesoura':
		if b == 'papel':
			print('Jogador 1 venceu!')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
		elif b == 'pedra':
			print('Jogador 2 venceu!')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
		else:
			print('Escolha uma opcao valida')
			if str(input('Deseja jogar novamente? ')) == 'sim':
				continue
			else:
				break
	else:
		print('Escolha uma opcao valida')
		if str(input('Deseja jogar novamente? ')) == 'sim':
			continue
		else:
			break



"""def jogodavelha(a,b)
	o1 = 'pedra'
	o2 = 'papel'
	o3 = 'tesoura'"""

