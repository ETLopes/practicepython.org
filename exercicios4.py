

pergunta = int(input('Me diga um número: '))
list_a = range(1,pergunta+1)
list_b = []

for i in list_a:
	if pergunta % i ==0:
		list_b.append(i)

print(list_b)



