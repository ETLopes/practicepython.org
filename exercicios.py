import os

nome = input('Qual o seu nome? ')
idade = input('Qual é a sua idade? ')
pergunta = input('Você já fez aniversário esse ano? ').lower()
idade = int(idade)
idade2 = (100 - idade + 2018)

if pergunta == 'sim':
	pass
else:
	idade2 = idade2 - 1


print(('Seu nome é ' + nome + '\n' + 'E você tem ' + str(idade) + ' anos.' + '\n' 'Em ' + str(idade2) + " anos você completará 100 anos.\n" + '\n') * idade)

